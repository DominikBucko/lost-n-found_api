from models.image import Image
from models.item import Item
from models.category import Category
from sqlalchemy.orm import sessionmaker

from db import Base, engine

import json

Session = sessionmaker(bind=engine)

def get_categories():
    session = Session()
    return [category.name for category in session.query(Category)]

