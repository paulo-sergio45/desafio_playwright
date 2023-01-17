import uvicorn
from fastapi import FastAPI

from app.routes import router_web_scrap, router_user

app = FastAPI(title="test API", version="1")

app.include_router(router_user.router_user)
app.include_router(router_web_scrap.router_web_scrap)


@app.on_event("startup")
async def startup_event():
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    #     await conn.run_sync(Base.metadata.create_all)

    print("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
