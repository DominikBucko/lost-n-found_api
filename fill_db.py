from sqlalchemy.orm import sessionmaker
from db import Base, engine
from models.category import Category
from models.item import Item, ItemType
from models.matches import Matches
from models.user import User

Session = sessionmaker(bind=engine)
session = Session()


def fill_db():

    # CATEGORY
    categories = ["Mobile phone", "Wallet", "Keys", "Accessory", "Laptop", "Camera", "Other"]
    for c in categories:
        category = Category(name=c)
        session.add(category)

    # # USER
    # user = User(email="bobo@bobo.sk", nickname="Bobuso", name="Robo")
    # session.add(user)
    #
    # # ITEMS
    # lost_item = Item(title="LOST TEST", category=category.name, status="Tested", type=ItemType.lost)
    # session.add(lost_item)
    #
    # found = Item(title="FOUND TEST", category=category.name, status="Tested", type=ItemType.found)
    # session.add(found)
    #
    # session.commit()
    #
    # # MATCHES
    # match = Matches(lost_id=lost_item.id, found_id=found.id, percentage=90, status="Tested")
    # session.add(match)
    session.commit()
