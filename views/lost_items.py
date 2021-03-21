from models.item import Item\
    , ItemSchema
# from models.category import Category
from flask import Response, request
from sqlalchemy.orm import sessionmaker
from db import Base, engine
import json

Session = sessionmaker(bind=engine)
session = Session()


def get_all():
    items = session.query(Item).all()
    items_schema = ItemSchema(many=True)
    return items_schema.dump(items)


def post():
    item_schema = ItemSchema()

    title = request.form.get('title')
    category = request.form.get('category')
    description = request.form.get('description', None)
    latitude = request.form.get('latitude', None)
    longitude = request.form.get('longitude', None)
    images = request.form.getlist('images')

    item = Item(title=title, category=category, status="created")

    if description is not None:
        item.description = description

    if latitude is not None and longitude is not None:
        item.latitude = latitude
        item.longitude = longitude

    for image in images:
        # TODO, update item_id-s in image
        pass

    session.add(item)
    session.commit()
    return item_schema.dump(item)


def get_id(id):
    item = session.query(Item).get(id)
    item_schema = ItemSchema()
    return item_schema.dump(item)
