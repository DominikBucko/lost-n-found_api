from sqlalchemy import Column, Integer, String
from db import Base
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import Schema, fields

class User(Base):

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String)
    name = Column(String)
    nickname = Column(String)
    telephone = Column(String)
    item = relationship("Item")

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'email', 'name', 'nickname', 'telephone')



