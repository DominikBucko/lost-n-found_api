from flask import g
from sqlalchemy import or_
from models.category import Category
from models.item import Item
from models.user import User
from models.matches import Matches
from sqlalchemy.orm import sessionmaker

from db import Base, engine


Session = sessionmaker(bind=engine)


def check_write_permissions(item):
    session = Session()
    item = session.query(Item).get(item)
    if item:
        if item.owner_id == g.user_id:
            return True

    return False


def check_read_permissions(item):
    session = Session()
    matches = session.query(Matches).filter(or_(Matches.found_id == item, Matches.lost_id == item))
    for match in matches:
        if match.found_id == g.user_id or match.lost_id == g.user_id:
            return True

    return False
