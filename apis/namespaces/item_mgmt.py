from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging


logger = logging.getLogger(__name__)
ns = Namespace("items", description="API for management of lost & found items", url_prefix="/api")

messageModel = ns.model(
    "message",
    {
        "message": fields.String,
    },
)


@ns.route("/lost")
class LostItems(Resource):
    @ns.response(code=200, model=messageModel, description="OK")
    @ns.doc(description="Fetch owners lost items.")
    @authenticate
    def get(self):
        pass


@ns.route("/found")
class FoundItems(Resource):
    pass
