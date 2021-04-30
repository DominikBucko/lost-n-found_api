from sqlalchemy.orm import sessionmaker
from db import Base, engine
from flask import g, abort
from auth.authorization import check_write_permissions, check_read_permissions
from models.matches import MatchesSchema, Matches
from sqlalchemy import or_
Session = sessionmaker(bind=engine)


def get_all():
    session = Session()
    matches = session.query(Matches).filter(Matches.status == "open", or_(Matches.lost.has(owner_id=g.user_id), Matches.found.has(owner_id=g.user_id)))
    matches_schema = MatchesSchema(many=True)

    dump = matches_schema.dump(matches)

    for match in dump:
        if match["lost"]["images"]:
            match["lost"]["images"] = [image.id for image in match["lost"]["images"]]
        if match["found"]["images"]:
            match["found"]["images"] = [image.id for image in match["found"]["images"]]

    return dump

def get_id(id):
    session = Session()
    match = session.query(Matches).get(id)
    if not (match.lost.owner_id == g.user_id or match.found.owner_id == g.user_id):
        abort(404, "Not found")
    matches_schema = MatchesSchema(many=False)
    match = matches_schema.dump(match)
    if match["lost"]["images"]:
        match["lost"]["images"] = [image.id for image in match["lost"]["images"]]
    if match["found"]["images"]:
        match["found"]["images"] = [image.id for image in match["found"]["images"]]

    return match


def patch(id, status):
    session = Session()
    match = session.query(Matches).get(id)
    if match.found.owner_id != g.user_id:
        abort(403, "Unauthorized")
    matches_schema = MatchesSchema(many=False)
    match.status = status
    if match.status == "resolved":
        match.lost.status = status
        match.found.status = status

    session.add(match)
    session.commit()
    match = matches_schema.dump(match)
    if match["lost"]["images"]:
        match["lost"]["images"] = [image.id for image in match["lost"]["images"]]
    if match["found"]["images"]:
        match["found"]["images"] = [image.id for image in match["found"]["images"]]
    return match
