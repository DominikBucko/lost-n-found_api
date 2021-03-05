from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging


logger = logging.getLogger(__name__)
ns = Namespace("user", description="Endpoints for user management", url_prefix="/api")

messageModel = ns.model(
    "message",
    {
        "message": fields.String,
    },
)

userModel = ns.model(
    "User",
    {
        "email": fields.String,
        "name": fields.String,
        "nickname": fields.String,
        "telephone": fields.String,
    }
)

@ns.route("/users")
class User(Resource):
    @ns.doc(
        description="Create new user.",
        params={},
        responses={
            200: "OK",
            400: "Bad request",
        },
    )
    @ns.expect(userModel)
    @ns.response(200, "OK", messageModel)
    @authenticate
    def post(self):
        pass


@ns.route("/users/<uid>")
class SpecificUser(Resource):
    @ns.doc(
        description="Fetch user.",
        params={},
        responses={
            200: "OK",
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found",

        },
    )
    @ns.response(200, "OK", userModel)
    @authenticate
    def get(self, uid):
        pass

    @ns.doc(
        description="Update user.",
        params={},
        responses={
            200: "OK",
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found",

        },
    )
    @ns.response(200, "OK", userModel)
    @ns.expect(userModel)
    @authenticate
    def patch(self, uid):
        pass
