from sqlalchemy.orm import sessionmaker
from db import Base, engine
from models.matches import MatchesSchema, Matches

Session = sessionmaker(bind=engine)


def get_all():
    session = Session()
    try:
        matches = session.query(Matches).all()
        matches_schema = MatchesSchema(many=True)
    except Exception:
        return {}

    return matches_schema.dump(matches)


def get_id(id):
    session = Session()
    try:
        match = session.query(Matches).get(id)
        matches_schema = MatchesSchema(many=False)
    except Exception:
        return {}
    return matches_schema.dump(match)


def patch(id, status):
    session = Session()
    try:
        match = session.query(Matches).get(id)
        matches_schema = MatchesSchema(many=False)
        match.status = status
        session.commit()
        return matches_schema.dump(match)
    except Exception:
        return {}
