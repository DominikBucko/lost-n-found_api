from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Binary, Float
from db import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Matches(Base):
    __tablename__ = "match"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item1_id = Column(UUID(as_uuid=True), ForeignKey("items.id"))
    item2_id = Column(UUID(as_uuid=True), ForeignKey("items.id"))
    percentage = Column(Float)
    status = Column(String)
