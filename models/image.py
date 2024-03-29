from sqlalchemy import Column, Integer, String, ForeignKey, Binary
from sqlalchemy.orm import relationship
from db import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Image(Base):
    __tablename__ = "image"
    id = Column(String, primary_key=True)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id", ondelete='CASCADE'), nullable=True)

