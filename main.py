from fastapi import FastAPI
from pony.orm import db_session
from modules import settings
from modules.database import Channel

app = FastAPI()

@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.get("/channels")
async def get_channels():
    with db_session:
        return [c.to_dict() for c in Channel.select()]


@app.get("/channels/{channel_id}")
async def get_channel(channel_id: int):
    with db_session:
        if channel := Channel.get(id=channel_id):
            return channel.to_dict()
    return {"error": "Channel not found"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT, root_path=settings.API_PATH)
