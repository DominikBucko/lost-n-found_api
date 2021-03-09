import config
from app import app, initialize_api
from db import Base, engine
from models import user, image, item, found_item, lost_item


def migrate():
    import alembic.config
    alembicArgs = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembicArgs)


def make_migrations():
    import alembic.config
    alembicArgs = [
        'revision',
        '--autogenerate',
    ]
    alembic.config.main(argv=alembicArgs)


def create_db():
    tables = Base.metadata.sorted_tables
    Base.metadata.create_all(engine)
    print(engine.has_table("users"))


if __name__ == '__main__':
    config.load_config("config.yaml")

    create_db()

    # TODO zakomentuj ked nechces pustat migrations
    # make_migrations()
    # migrate()

    initialize_api()
    app.run(host="::", port=config.config.port)
