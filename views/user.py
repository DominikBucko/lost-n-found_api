from sqlalchemy.orm import sessionmaker
from db import Base, engine
from models.user import User, UserSchema

Session = sessionmaker(bind=engine)


def create_new(data):
    session = Session()
    user_schema = UserSchema(many=False)

    user = User(**data)
    session.add(user)
    session.commit()
    return user_schema.dump(user)


def get_id(id):
    session = Session()
    user_schema = UserSchema(many=False)

    user = session.query(User).get(id)
    return user_schema.dump(user)


def update(id, data):
    session = Session()
    user_schema = UserSchema(many=False)

    user = session.query(User).get(id)
    user.email = data['email']
    user.name = data['name']
    user.nickname = data['nickname']
    user.telephone = data['telephone']
    session.commit()
    return user_schema.dump(user)
