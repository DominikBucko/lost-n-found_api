from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging

logger = logging.getLogger(__name__)
ns = Namespace("items", description="API for management of lost & found items", url_prefix="/api")

# BOL SOM NASRATY ZE MI NEJDE TO MANY TO MANY TAK SOM SKUSAL SPRAVIT TOTO ALE ESTE
#  VIAC SOM SA NASRAL LEBO MI NESLO SPRAVIT LIST :D

messageModel = ns.model(
    "item", {
        "category": fields.String,
        "brand": fields.String,
        "title": fields.String,
        "description": fields.String,
        "GPS-lat": fields.Float,
        "GPS-lon": fields.Float,
        "images": fields.List(fields.String, description='image')
        # "images": fields.List(fields.Nested(image)),
    }
)


@ns.route("/lost")
class LostItems(Resource):
    @ns.response(code=200, model=messageModel, description="OK")
    @ns.response(code=500, description="Internal Server Error")
    @ns.doc(description="Fetch owners lost items.")
    @authenticate
    def get(self):
        pass


@ns.route("/found")
class FoundItems(Resource):
    pass
