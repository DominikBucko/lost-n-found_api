from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging
from .lost_items import itemFetchModel

logger = logging.getLogger(__name__)
ns = Namespace("matches", description="API for management of found items", url_prefix="/api")

# @ns.route("/found")
matchesFetchModel = ns.model(
    "match",
    {
        "item 1": fields.Nested(itemFetchModel),
        "item 2": fields.Nested(itemFetchModel),
        "status": fields.String(),
        "percentage": fields.Float()
    }
)

matchesBulkFetchModel = ns.model(
    "items",
    {
        "items": fields.List(fields.Nested(matchesFetchModel))
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
        pass

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
        pass

    @ns.doc(
        description="Update record of item.",
        params={},
        responses={
            200: "OK",
            404: "Not found",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", matchesFetchModel)
    @ns.expect(matchesFetchModel)
    @authenticate
    def patch(self, item_id):
        pass

ns.add_resource(MatchItem, "/matches")
ns.add_resource(MatchSingleItem, "/matches/<item_id>")