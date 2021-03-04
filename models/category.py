from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Binary
from db import Base


class Category(Base):
    __tablename__ = "category"
    name = Column(String, primary_key=True)
    item = relationship("items")
