from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from db import Base
import enum
import uuid


class ItemType(enum.Enum):
    found = 1
    lost = 2


class Item(Base):
    __tablename__ = "items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    type = Column(Enum(ItemType))
    images = relationship("Image")
    category = Column(String, ForeignKey("category.name"))
    status = Column(String)
    owner_id = Column(String, ForeignKey("users.email"))
