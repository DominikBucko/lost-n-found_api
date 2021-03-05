from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging


logger = logging.getLogger(__name__)
ns = Namespace("files", description="Endpoints for upload of binary files", url_prefix="/api")

messageModel = ns.model(
    "message",
    {
        "message": fields.String,
    },
)


@ns.route("/upload")
class Upload(Resource):
    @ns.doc(
        description="Upload a binary file.",
        params={},
        responses={
            200: "OK",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", messageModel)
    @authenticate
    def put(self):
        pass

@ns.route("/download/<name>")
class Download(Resource):
    @ns.doc(
        description="Download a binary file on a given path.",
        params={},
        responses={
            200: "OK",
            404: "Not found",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", messageModel)
    @authenticate
    def get(self, name):
        pass