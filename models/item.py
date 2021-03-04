from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from .category import Category


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    images = relationship("image")
    category_id = Column(String, ForeignKey("category.id"))
    latitude = Column(Float)
    longitude = Column(Float)

