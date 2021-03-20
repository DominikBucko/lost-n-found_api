from sqlalchemy import Column, Integer, String, ForeignKey, Binary
from sqlalchemy.orm import relationship
from db import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Image(Base):
    __tablename__ = "image"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=True)
    content = Column(Binary)

