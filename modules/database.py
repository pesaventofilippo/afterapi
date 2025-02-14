from pony.orm import Database, PrimaryKey, Required, Optional, Set

db = Database("sqlite", "../afterapi.db", create_db=True)


class Channel(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    type = Required(str, default="m3u")
    manifest = Required(str)
    stream_id = Optional(str)
    stream_key = Optional(str)
    category = Required("Category")

    def __str__(self):
        return self.name

    @property
    def json_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.id
        }

    @property
    def json_full(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "manifest": self.manifest,
            "stream_id": self.stream_id,
            "stream_key": self.stream_key,
            "category": self.category.id
        }


class Category(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    color = Required(str, default="#FFFFFF")
    channels = Set(Channel)

    def __str__(self):
        return self.name

    @property
    def json_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color
        }

    @property
    def json_full(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "channels": [ch.json_info for ch in self.channels.order_by(Channel.id)]
        }


db.generate_mapping(create_tables=True)
