from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from db import Base
from .category import Category
# from .tag import Tag


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    images = relationship("Image")
    category_id = Column(String, ForeignKey("category.name"))
    # tag_id = Column(String, ForeignKey("tags.name"))
    # tags = relationship(
    #     "Tag",
    #     secondary="tag_item",
    #     back_populates="items")
    status = Column(String)
