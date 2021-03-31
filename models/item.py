from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import Schema, fields
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
        item = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        item["images"] = [image.id for image in item["images"]]


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
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))


class ItemSchema(Schema):

    class Meta:
        fields = ('id', 'title', 'description', 'latitude', 'longitude', 'type',
                  'images', 'category', 'status', 'owner_id')


