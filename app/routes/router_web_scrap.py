from fastapi import APIRouter, Depends

from app.security.json_web_token import get_jwt_user
from app.web_scraper import play_scraper

router_web_scrap = APIRouter()


@router_web_scrap.get("/webscrap/laptops/lenovo", response_model=dict)
async def get_laptops_lenovo(jwt_user: str = Depends(get_jwt_user)):
    laptops: list = await play_scraper.get_laptops_lenovo()
    return {"laptops_lenovo": laptops}


@router_web_scrap.get("/webscrap/laptops/{laptop_brand}", response_model=dict)
async def get_laptops_brand(laptop_brand: str, jwt_user: str = Depends(get_jwt_user)):
    laptops: list = await play_scraper.get_laptops(laptop_brand=laptop_brand.strip())
    return {"laptops_" + laptop_brand.strip().replace(" ","_").lower(): laptops}
