from sqlalchemy import Column, Integer, String, ForeignKey, Binary
from sqlalchemy.orm import relationship
from db import Base


class Image(Base):
    __tablename__ = "image"
    id = Column(String, primary_key=True)
    item_id = Column(String, ForeignKey("items.id"))
    content = Column(Binary)

