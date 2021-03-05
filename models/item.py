from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from db import Base
from .category import Category
from .tag import Tag


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    images = relationship("image")
    category_id = Column(String, ForeignKey("category.name"))
    # tag_id = Column(String, ForeignKey("tags.name"))
    tags = relationship(
        "tags",
        secondary="tag_item",
        back_populates="items")


# TODO chcel som to dat do vlastneho filu len to nechcelo vytvorit tu tabulku neviem preco tak zatial to je tu
tag_item = Table('tag_item', Base.metadata,
                 Column('tag_id', String, ForeignKey('tags.name')),
                 Column('item_id', String, ForeignKey('items.id'))
                 )
