from models.image import Image
from models.item import Item
from sqlalchemy.orm import sessionmaker

from db import Base, engine

import json

Session = sessionmaker(bind=engine)


def register_file(filename, item):
    session = Session()
    file = Image(id=filename, item_id=item)
    session.add(file)
    session.commit()


def check_file_ownership(filename, item):
    session = Session()
    item = session.query(Item).get(item)
    for image in item.images:
        if image.id == filename:
            return True

    return False
