from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Binary, Table
from db import Base


tag_item = Table('tag_item', Base.metadata,
                 Column('tag_id', String, ForeignKey('tag.name')),
                 Column('item_id', String, ForeignKey('items.id'))
                 )