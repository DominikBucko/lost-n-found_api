from sqlalchemy.orm import sessionmaker
from db import Base, engine
from flask import g, abort
from auth.authorization import check_write_permissions, check_read_permissions
from models.matches import MatchesSchema, Matches
from sqlalchemy import or_
Session = sessionmaker(bind=engine)


def get_all():
    session = Session()
    try:
        matches = session.query(Matches).filter(or_(Matches.lost.owner_id == g.user_id, Matches.found.owner_id == g.user_id))
        matches_schema = MatchesSchema(many=True)
    except Exception:
        return {}

    return matches_schema.dump(matches)


def get_id(id):
    session = Session()
    match = session.query(Matches).get(id)
    if not (match.lost.owner_id == g.user_id or match.found.owner_id == g.user_id):
        abort(404, "Not found")
    matches_schema = MatchesSchema(many=False)
    return matches_schema.dump(match)


def patch(id, status):
    session = Session()
    match = session.query(Matches).get(id)
    if match.found.owner_id != g.user_id:
        abort(403, "Unauthorized")
    matches_schema = MatchesSchema(many=False)
    match.status = status
    session.commit()
    return matches_schema.dump(match)
