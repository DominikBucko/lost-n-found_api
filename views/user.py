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

    # for key in data:
    #     user.__dict__[key] = data[key]

    if 'email' in data.keys():
        user.email = data['email']
    if 'name' in data.keys():
        user.name = data['name']
    if 'nickname' in data.keys():
        user.nickname = data['nickname']
    if 'telephone' in data.keys():
        user.telephone = data['telephone']

    session.commit()
    return user_schema.dump(user)
