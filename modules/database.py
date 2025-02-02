from pony.orm import Database, PrimaryKey, Required

db = Database("sqlite", "../afterapi.db", create_db=True)


class Channel(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    manifest = Required(str)
    stream_id = Required(str)
    stream_key = Required(str)


db.generate_mapping(create_tables=True)


if __name__ == '__main__':
    from sys import argv
    from pony.orm import db_session

    if len(argv) != 5:
        print(f"Usage: python3 {argv[0]} <name> <manifest> <stream_id> <stream_key>")
        exit(1)

    with db_session:
        Channel(name=argv[1], manifest=argv[2], stream_id=argv[3], stream_key=argv[4])
        print(f"Added {argv[1]}")
