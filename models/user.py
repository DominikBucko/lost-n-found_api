from sqlalchemy import Column, Integer, String
from db import Base
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"
    email = Column(String, primary_key=True)
    name = Column(String)
    nickname = Column(String)
    lost_item = relationship("Item")


