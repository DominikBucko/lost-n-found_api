from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from .category import Category


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    images = relationship("image")
    category_id = Column(String, ForeignKey("category.name"))

    tags = relationship(
        "tag",
        secondary="tag_item",
        back_populates="items")

