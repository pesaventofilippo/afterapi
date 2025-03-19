import json
from pony.orm import db_session
from modules.database import Channel, Category


with db_session:
    categories = [cat.json_full for cat in Category.select().order_by(Category.id)]
    channels = [ch.json_full for ch in Channel.select().order_by(Channel.id)]

    with open("dump.json", "w") as f:
        json.dump({"categories": categories, "channels": channels}, f, indent=4)
