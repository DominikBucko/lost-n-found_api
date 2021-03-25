from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import Schema
from db import Base
import enum
import uuid


class ItemType(enum.Enum):
    found = 1
    lost = 2


class ItemStatus(enum.Enum):
    open = 1
    resolved = 2
    Tested = 3


class Item(Base):

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    __tablename__ = "items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    type = Column(Enum(ItemType))
    images = relationship("Image")
    category = Column(String, ForeignKey("category.name"))
    status = Column(Enum(ItemStatus))
    owner_id = Column(String, ForeignKey("users.email"))


class ItemSchema(Schema):
    class Meta:
        # model = Item
        fields = ('id', 'title', 'description', 'latitude', 'longitude', 'type',
                  'images', 'category', 'status', 'owner_id')


