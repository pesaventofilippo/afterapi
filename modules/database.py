from pony.orm import Database, PrimaryKey, Required, Set

db = Database("sqlite", "../afterapi.db", create_db=True)


class Channel(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    manifest = Required(str)
    stream_id = Required(str)
    stream_key = Required(str)
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
            "manifest": self.manifest,
            "stream_id": self.stream_id,
            "stream_key": self.stream_key,
            "category": self.category.id
        }


class Category(db.Entity):
    id = PrimaryKey(str)
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


db.generate_mapping(create_tables=True)
