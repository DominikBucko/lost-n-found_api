from models.item import Item
from models.category import Category
from flask import Response, request
from sqlalchemy.orm import sessionmaker
from db import Base, engine
import json

Session = sessionmaker(bind=engine)
session = Session()


def get_all():
    items = session.query(Item).all()

    jsondata = []
    for item in items:
        item.id = str(item.id)
        jsondata.append(json.loads(json.dumps(item.__dict__, default=lambda o: "", indent=4)))

    return Response({"items": jsondata}, status=200)


def post():
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
        #TODO, update item_id-s in image
        pass

    session.add(item)
    session.commit()
    return Response(status=200)

def get_id(id):
    item = session.query(Item).get(id)
    item.id = str(item.id)
    return json.loads(json.dumps(item.__dict__, default=lambda o: "", indent=4))
