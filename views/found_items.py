from sqlalchemy.exc import SQLAlchemyError

from models.item import Item \
    , ItemSchema, ItemStatus, ItemType

from models.matches import Matches

from misc import get_distance
from models.category import Category
# from models.category import Category
# from .lost_items import refresh_matches
from flask import Response, request, g
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from sockets_calls import notify_both
import json

Session = sessionmaker(bind=engine)


def get_all():
    session = Session()
    try:
        items = session.query(Item).filter(Item.type == ItemType.found, Item.owner_id == g.user_id, Item.status == "open")
        items_schema = ItemSchema(many=True)
        # print(items_schema.dump(items))
    except Exception:
        return {}
    # return [item.as_dict() for item in items]
    item_dict = items_schema.dump(items)
    for item in item_dict:
        item["images"] = [image.id for image in item["images"]]

    return item_dict


def create_new(data):
    session = Session()
    item_schema = ItemSchema(many=False)
    if data.get("id"):
        data.pop("id")
    data["type"] = "found"
    data["status"] = "open"
    data["owner_id"] = g.user_id
    item = Item(**data)

    # for image in images:
    #     # TODO, update item_id-s in image
    #     pass

    session.add(item)
    session.commit()
    find_matches(item)
    # return item.as_dict()
    dump = item_schema.dump(item)
    # dump["images"] = [image.id for image in item.images]
    return dump


def get_id(id):
    session = Session()
    item_schema = ItemSchema(many=False)
    item = session.query(Item).get(id)
    dump = item_schema.dump(item)
    dump["images"] = [image.id for image in item.images]
    return dump


def find_matches(item):
    session = Session()
    matches = session.query(Matches).filter(Matches.found.has(id=item.id))

    for match in matches:
        session.delete(match)

    session.commit()

    session = Session()
    res = session.query(Item).filter(Item.category == item.category,
                                     Item.status == ItemStatus.open,
                                     Item.type == ItemType.lost,
                                     Item.owner_id != item.owner_id)
    for row in res:
        distance = get_distance(item.latitude, item.longitude, row.latitude, row.longitude)
        if distance < 500:
            notify_both(row.owner_id, item.owner_id, item.title, "found")
            match = Matches(lost_id=row.id, found_id=item.id, percentage=(100 - distance / 10), status="open")
            session.add(match)

    session.commit()


def update(id, data):
    session = Session()
    item_schema = ItemSchema(many=False)
    item = session.query(Item).get(id)
    if item.type == ItemType.found:
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
        find_matches(item)
        return item_schema.dump(item)
    else:
        raise SQLAlchemyError


# def refresh_matches(item):
#     session = Session()
#     matches = session.query(Matches).filter(Matches.found.has(id=item.id))
#
#     for match in matches:
#         distance = get_distance(item.latitude, item.longitude, match.found.latitude, match.found.longitude)
#         if distance > 500 or match.found.category != item.category or match.found.category != item.category:
#             session.delete(match)
#         else:
#             match.percentage = (100 - distance / 10)
#             session.add(match)
#
#     session.commit()
#
#
def delete_matches(item):
    session = Session()
    matches = session.query(Matches).filter(Matches.found.has(id=item.id))
    for match in matches:
        session.delete(match)
    session.commit()


def delete(id):
    session = Session()
    item = session.query(Item).get(id)
    if item.type == ItemType.found:
        delete_matches(item)
        session.delete(item)
        session.commit()
        return True
    else:
        raise SQLAlchemyError
