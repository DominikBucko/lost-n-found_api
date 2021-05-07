import config
from app import app, initialize_api
from apis.api_v1 import init
from sockets import socketio
from db import Base, engine
import os
from fill_db import fill_db
from models import user, image, item, matches


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
    create_db()

    # TODO zakomentuj ked nechces pustat migrations
    # make_migrations()
    # migrate()
    #
    # # DB FILL
    # fill_db()

    initialize_api()
    init(app)
    socketio.run(app, host="0.0.0.0", port=config.config.port, debug=True)
    # socketio.run(app, port=8088, debug=True)

