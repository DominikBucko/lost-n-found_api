# from sqlalchemy.orm import relationship
# from sqlalchemy import Column, Integer, String, ForeignKey, Binary, Table
# from db import Base
# # from tag_item import tag_item
#
#
# class Tag(Base):
#     __tablename__ = "tags"
#     name = Column(String, primary_key=True)
#     # item = relationship("items")
#
#     items = relationship(
#         "Item",
#         secondary='tag_item',
#         back_populates="tags")