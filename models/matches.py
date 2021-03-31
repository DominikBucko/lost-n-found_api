from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, Binary, Float
from db import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import Schema, fields
from .item import ItemSchema


class Matches(Base):

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    __tablename__ = "match"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    percentage = Column(Float)
    status = Column(String)

    lost_id = Column(UUID(as_uuid=True), ForeignKey("items.id", ondelete='CASCADE'))
    lost = relationship("Item", foreign_keys=[lost_id])
    # lost = relationship("Item", foreign_keys=[lost_id], backref=backref('items', cascade='all,delete'))

    found_id = Column(UUID(as_uuid=True), ForeignKey("items.id", ondelete='CASCADE'))
    # found = relationship("Item", foreign_keys=[found_id], backref=backref('items', cascade='all,delete'))
    found = relationship("Item", foreign_keys=[found_id])


class MatchesSchema(Schema):
    lost = fields.Nested(ItemSchema)
    found = fields.Nested(ItemSchema)

    class Meta:
        #     # model = Matches
        fields = ('id', 'lost', 'found', 'percentage', 'status')
