from .item import Item
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Binary



class FoundItem(Item):
    __tablename__ = "found"
    uid = Column(String, ForeignKey('items.id'), primary_key=True)
    # matches = relationship("lost")
