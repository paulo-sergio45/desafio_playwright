import operator
import re
from typing import List

from fastapi import HTTPException
from playwright.async_api import async_playwright, Page, Locator, TimeoutError

from app.config import URL_SCRAPER


async def get_laptops_lenovo() -> List:
    async with async_playwright() as pw:
        try:
            browser = await pw.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1280, 'height': 1024}
            )
            page: Page = await context.new_page()
            await page.goto(URL_SCRAPER)
            pages_to_scraper: Locator = page.locator(".thumbnail").filter(has_text="Lenovo")
            n_pages: int = await pages_to_scraper.count()
        except (Exception, TimeoutError) as e:
            raise HTTPException(status_code=500, detail="Not available resource")

        list_laptops = []
        if n_pages == 0:
            return list_laptops

        for i in range(n_pages):
            list_laptops.append({
                "price": float((await pages_to_scraper.nth(i).locator(".price").inner_text()).replace("$", "")),
                "image-url": await pages_to_scraper.nth(i).locator(".img-responsive").get_attribute("src"),
                "title": await pages_to_scraper.nth(i).locator(".title").get_attribute("title"),
                "description": await pages_to_scraper.nth(i).locator(".description").inner_text(),
                "review": await pages_to_scraper.nth(i).locator("p.pull-right").inner_text(),
                "rating": await pages_to_scraper.nth(i).locator("p:nth-child(2)").get_attribute("data-rating")
            })
        sorted_list_laptops = sorted(list_laptops, key=operator.itemgetter('price'), reverse=False)

        return sorted_list_laptops


async def get_laptops(laptop_brand: str) -> List:
    async with async_playwright() as pw:
        try:
            browser = await pw.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1280, 'height': 1024}
            )
            page: Page = await context.new_page()
            await page.goto(URL_SCRAPER)
            pages_to_scraper: Locator = page.locator(".thumbnail").filter(has_text=re.compile(laptop_brand,re.IGNORECASE))
            n_pages: int = await pages_to_scraper.count()
        except (Exception, TimeoutError) as e:
            raise HTTPException(status_code=500, detail="Not available resource")

        list_laptops = []
        if n_pages == 0:
            return list_laptops

        for i in range(n_pages):
            list_laptops.append({
                "price": float((await pages_to_scraper.nth(i).locator(".price").inner_text()).replace("$", "")),
                "image-url": await pages_to_scraper.nth(i).locator(".img-responsive").get_attribute("src"),
                "title": await pages_to_scraper.nth(i).locator(".title").get_attribute("title"),
                "description": await pages_to_scraper.nth(i).locator(".description").inner_text(),
                "review": await pages_to_scraper.nth(i).locator("p.pull-right").inner_text(),
                "rating": await pages_to_scraper.nth(i).locator("p:nth-child(2)").get_attribute("data-rating")
            })
        sorted_list_laptops = sorted(list_laptops, key=operator.itemgetter('price'), reverse=False)

        return sorted_list_laptops
