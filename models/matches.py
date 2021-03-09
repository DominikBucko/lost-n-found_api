from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Binary, Float
from db import Base


class Matches(Base):
    __tablename__ = "match"
    id = Column(String, primary_key=True)

    lost_id = Column(String, ForeignKey("lost.uid"))
    lost = relationship("LostItem", back_populates="matches_l")

    found_id = Column(String, ForeignKey("found.uid"))
    found = relationship("FoundItem", back_populates="matches_f")

    percentage = Column(Float)

    status = Column(String)