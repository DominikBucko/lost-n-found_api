# from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
# from sqlalchemy.orm import relationship
# from db import Base
#
# tag_item = Table('tag_item', Base.metadata,
#                  Column('tag_id', String, ForeignKey('tags.name')),
#                  Column('item_id', String, ForeignKey('items.id'))
#                  )