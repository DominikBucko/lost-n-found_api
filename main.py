import config
from app import app, initialize_api
from db import Base, engine
from models import user, item, image, lost_item, found_item


def create_db():
    tables = Base.metadata.sorted_tables
    Base.metadata.create_all(engine)
    print(engine.has_table("users"))


if __name__ == '__main__':
    config.load_config("config.yaml")

    create_db()

    initialize_api()
    app.run(host="::", port=config.config.port)
