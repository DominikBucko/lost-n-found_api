from models.lost_item import LostItem
from models.item import Item
from models.category import Category
from flask import make_response, abort
from sqlalchemy.orm import sessionmaker
from db import Base, engine

Session = sessionmaker(bind=engine)
session = Session()


def get_all():
    items = session.query(Item).first()
    print(items)


def post():
    # category = Category(name="Category name")
    # session.add(category)
    # category = session.query(Category).first()
    # item = Item(id="1", title="Test", category_id=category.name, status="Tested")
    # session.add(item)
    # session.commit()
    get_all()
