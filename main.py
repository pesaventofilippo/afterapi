from fastapi import FastAPI
from pony.orm import db_session
from fastapi.middleware.cors import CORSMiddleware
from modules import settings
from modules.database import Channel, Category

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/categories")
async def get_categories():
    with db_session:
        return [cat.json_info for cat in Category.select().order_by(Category.id)]


@app.get("/categories/{category_id}")
async def get_category(category_id: int):
    with db_session:
        if category := Category.get(id=category_id):
            return category.json_full
    return {}


@app.get("/channels")
async def get_channels():
    with db_session:
        return [ch.json_info for ch in Channel.select().order_by(Channel.id)]


@app.get("/channels/{channel_id}")
async def get_channel(channel_id: int):
    with db_session:
        if channel := Channel.get(id=channel_id):
            return channel.json_full
    return {}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT, root_path=settings.API_PATH)
