from flask import request, json
from sqlalchemy.exc import SQLAlchemyError, NoReferenceError

from auth.authentication import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
from views.user import get_id, create_new, update
import logging

# # TODO DELETE THIS
# from auth.encode_decode_token import decode, encode


logger = logging.getLogger(__name__)
ns = Namespace("users", description="Endpoints for user management", url_prefix="/api")

messageModel = ns.model(
    "message",
    {
        "message": fields.String,
    },
)

userCreateModel = ns.model(
    "createUser",
    {
        "email": fields.String,
        "name": fields.String,
        "nickname": fields.String,
        "telephone": fields.String,
    }
)

userModel = ns.model(
    "user",
    {
        "id": fields.String,
        "email": fields.String,
        "name": fields.String,
        "nickname": fields.String,
        "telephone": fields.String,
    }
)

@ns.route("/")
class User(Resource):
    @ns.doc(
        description="Create new user.",
        params={},
        responses={
            200: "OK",
            400: "Bad request",
        },
    )
    @ns.expect(userCreateModel)
    @ns.response(200, "OK", messageModel)
    @authenticate
    def post(self):
        try:
            return create_new(request.get_json())
        except SQLAlchemyError as e:
            logging.error(e)
            abort(400, "Bad request")
        except NoReferenceError:
            abort(400, "Non-existent category")


@ns.route("/<uid>")
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
        try:
            # # TODO DELETE THIS
            # payload = {"sub": "1234567890", "id": "test_id2", "iat": 1516239022}
            # token = encode(payload)
            # decode(token)

            user = get_id(uid)
            return marshal(user, userModel), 200
        except SQLAlchemyError:
            abort(404, "No result.")

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
    @ns.expect(userCreateModel)
    @authenticate
    def patch(self, uid):
        try:
            user = update(uid, request.get_json())
            return marshal(user, userModel), 200
        except SQLAlchemyError:
            abort(400, "Bad request")
        except NoReferenceError:
            abort(400, "Non-existent category")