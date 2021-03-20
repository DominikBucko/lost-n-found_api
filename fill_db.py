from sqlalchemy.orm import sessionmaker
from db import Base, engine
from models.category import Category
from models.item import Item
from models.matches import Matches
from models.user import User

Session = sessionmaker(bind=engine)
session = Session()

def fill_db():

    # CATEGORY
    category = Category(name="Category name")
    session.add(category)

    # USER
    user = User(email="bobo@bobo.sk", nickname="Bobuso", name="Robo")
    session.add(user)

    # ITEMS
    item = Item(title="LOST TEST", category=category.name, status="Tested")
    session.add(item)

    item2 = Item(title="FOUND TEST", category=category.name, status="Tested")
    session.add(item2)

    # MATCHES
    match = Matches(item1_id=item.id, item2_id=item2.id, percentage=90, status="Tested")
    session.add(match)

    session.commit()
