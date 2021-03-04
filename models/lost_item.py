from .item import Item
from sqlalchemy import Column, Integer, String, ForeignKey, Binary
from sqlalchemy.orm import relationship


class LostItem(Item):
    __tablename__ = "lost"
    uid = Column(String, ForeignKey('items.id'), primary_key=True)
    owner_id = Column(String, ForeignKey("users.email"))
    # matches = relationship("found", ForeignKey("items.uid"))