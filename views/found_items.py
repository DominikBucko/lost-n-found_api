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
        items = session.query(Item).all()
        items_schema = ItemSchema(many=True)
    except Exception:
        return {}

    return items_schema.dump(items)



def create_new(data):
    session = Session()

    # title = request.form.get('title')
    # category = request.form.get('category')
    # description = request.form.get('description', None)
    # latitude = request.form.get('latitude', None)
    # longitude = request.form.get('longitude', None)
    # images = request.form.getlist('images')
    # data["category"] = session.query(Category).get(data["category"])
    data["type"] = "lost"
    data["status"] = "open"
    item = Item(**data)

    # if description is not None:
    #     item.description = description
    #
    # if latitude is not None and longitude is not None:
    #     item.latitude = latitude
    #     item.longitude = longitude
    #
    # for image in images:
    #     # TODO, update item_id-s in image
    #     pass

    session.add(item)
    session.commit()
    find_matches(item)
    return item.as_dict()
    # return item_schema.dump(item)


def get_id(id):
    session = Session()
    item = session.query(Item).get(id)
    return item.as_dict()


def find_matches(item):
    session = Session()
    res = session.query(Item).filter(Item.category == item.category,
                                     Item.status == ItemStatus.open,
                                     Item.type == ItemType.found)
    for row in res:
        distance = get_distance(item.latitude, item.longitude, row.latitude, row.longitude)
        if distance < 500:
            match = Matches(item1_id=row.id, item2_id=item.id, percentage=(100 - distance/10))
            session.add(match)

    session.commit()