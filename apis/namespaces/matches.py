from flask import request, json
from auth.authentication import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging
from .lost_items import itemFetchModel
from views.matches import get_all, get_id, patch

logger = logging.getLogger(__name__)
ns = Namespace("items/matches", description="API for management of found items", url_prefix="/api")

# @ns.route("/found")
matchesFetchModel = ns.model(
    "match",
    {
        "id": fields.String(),
        "lost": fields.Nested(itemFetchModel),
        "found": fields.Nested(itemFetchModel),
        "status": fields.String(),
        "percentage": fields.Float()
    }
)

matchesBulkFetchModel = ns.model(
    "matches",
    {
        "matches": fields.List(fields.Nested(matchesFetchModel))
    }
)

matchesPatchModel = ns.model(
    "patch_status",
    {
        "status": fields.String(),
    }
)


class MatchItem(Resource):
    @ns.doc(
        description="Fetch matches",
        params={},
        responses={
            200: "OK",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", matchesBulkFetchModel)
    # @ns.response(code=200, model=messageModel, description="OK")

    @authenticate
    def get(self):
        matches = get_all()
        print(matches)
        if not matches:
            return {"matches": []}
        return marshal({"matches": matches}, matchesBulkFetchModel), 200


class MatchSingleItem(Resource):
    @ns.doc(
        description="Fetch match.",
        params={},
        responses={
            200: "OK",
            404: "Not found",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", matchesFetchModel)
    @authenticate
    def get(self, item_id):
        match = get_id(item_id)
        if not match:
            return {"matches": []}
        return marshal(match, matchesFetchModel), 200

    @ns.doc(
        description="Update record of match.",
        params={},
        responses={
            200: "OK",
            404: "Not found",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", matchesFetchModel)
    @ns.expect(matchesPatchModel)
    @authenticate
    def patch(self, item_id):
        match = patch(item_id, request.get_json()["status"])
        if not match:
            return {"matches": []}
        return marshal(match, matchesFetchModel), 200


ns.add_resource(MatchItem, "")
ns.add_resource(MatchSingleItem, "/<item_id>")