from .item import Item
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Binary



class FoundItem(Item):
    __tablename__ = "found"
    uid = Column(String, ForeignKey('items.id'), primary_key=True)
    owner_id = Column(String, ForeignKey("users.email"))
    # test_field = Column(Integer)
    # matches = relationship("lost")
