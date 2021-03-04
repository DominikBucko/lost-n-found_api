from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    images = relationship("image")
    latitude = Column(Float)
    longitude = Column(Float)

