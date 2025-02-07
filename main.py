from fastapi import FastAPI
from pony.orm import db_session
from modules import settings
from modules.database import Channel, Category

app = FastAPI()

@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.get("/categories")
async def get_categories():
    with db_session:
        return [cat.json_info for cat in Category.select()]


@app.get("/categories/{category_id}")
async def get_category(category_id: str):
    with db_session:
        return [ch.json_info for ch in Channel.select(lambda c: c.category.id == category_id)]


@app.get("/channels")
async def get_channels():
    with db_session:
        return [ch.json_info for ch in Channel.select()]


@app.get("/channels/{channel_id}")
async def get_channel(channel_id: int):
    with db_session:
        if channel := Channel.get(id=channel_id):
            return channel.json_full
    return {}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT, root_path=settings.API_PATH)
