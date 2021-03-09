from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from db import Base
from .category import Category
from .tag import Tag


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    images = relationship("image")
    category_id = Column(String, ForeignKey("category.name"))
    # tag_id = Column(String, ForeignKey("tags.name"))
    tags = relationship(
        "tags",
        secondary="tag_item",
        back_populates="items")
    status = Column(String)
