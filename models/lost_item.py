from .item import Item
from sqlalchemy import Column, Integer, String, ForeignKey, Binary
from sqlalchemy.orm import relationship


class FoundItem(Item):
    __tablename__ = "lost"
    uid = Column(String, ForeignKey('items.id'), primary_key=True)
    # matches = relationship("found", ForeignKey("items.uid"))