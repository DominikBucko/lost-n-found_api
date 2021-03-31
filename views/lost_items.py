from sqlalchemy.exc import SQLAlchemyError

from models.item import Item\
    , ItemSchema, ItemStatus, ItemType

from models.matches import Matches

from misc import get_distance
from models.category import Category
# from models.category import Category
from flask import Response, request
from sqlalchemy.orm import sessionmaker
from db import Base, engine
import json

Session = sessionmaker(bind=engine)


def get_all():
    session = Session()
    try:
        items = session.query(Item).filter(Item.type == ItemType.lost)
        items_schema = ItemSchema(many=True)
    except Exception:
        return {}

    item_dict = items_schema.dump(items)
    for item in item_dict:
        item["images"] = [image.id for image in item["images"]]

    return item_dict


def create_new(data):
    session = Session()
    item_schema = ItemSchema(many=False)
    data["type"] = "lost"
    data["status"] = "open"
    item = Item(**data)
    #
    # for image in images:
    #     # TODO, update item_id-s in image
    #     pass

    session.add(item)
    session.commit()
    find_matches(item)
    # return item.as_dict()
    return item_schema.dump(item)


def get_id(id):
    session = Session()
    item_schema = ItemSchema(many=False)
    item = session.query(Item).get(id)
    # return item.as_dict()
    return item_schema.dump(item)


def find_matches(item):
    session = Session()
    res = session.query(Item).filter(Item.category == item.category,
                                     Item.status == ItemStatus.open,
                                     Item.type == ItemType.lost
                                     )
    # res = session.query(Item).all()
    for row in res:
        distance = get_distance(item.latitude, item.longitude, row.latitude, row.longitude)
        if distance < 500:
            match = Matches(found_id=row.id, lost_id=item.id, percentage=(100 - distance/10))
            session.add(match)

    session.commit()


def update(id, data):
    session = Session()
    item_schema = ItemSchema(many=False)
    item = session.query(Item).get(id)
    if item.type == ItemType.lost:
        if 'title' in data.keys():
            item.title = data['title']
        if 'description' in data.keys():
            item.description = data['description']
        if 'latitude' in data.keys():
            item.latitude = data['latitude']
        if 'longitude' in data.keys():
            item.longitude = data['longitude']
        if 'category' in data.keys():
            item.category = data['category']
        session.commit()
        return item_schema.dump(item)
    else:
        raise SQLAlchemyError

def delete(id):
    session = Session()
    item = session.query(Item).get(id)
    if item.type == ItemType.lost:
        session.delete(item)
        session.commit()
        return True
    else:
        raise SQLAlchemyError
