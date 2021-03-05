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

itemCreateModel = ns.model(
    "createdItem",
    {
        "title": fields.String,
        "description": fields.String,
        "latitude": fields.Float,
        "longitude": fields.Float,
        "category": fields.String,
        "tags": fields.List(fields.String),
        "images": fields.List(fields.String),
    }
)


itemFetchModel = ns.model(
    "fetchItem",
    {
        "id": fields.String,
        "title": fields.String,
        "description": fields.String,
        "latitude": fields.Float,
        "longitude": fields.Float,
        "category": fields.String,
        "tags": fields.List(fields.String),
        "images": fields.List(fields.Url),
    }
)

itemBulkFetchModel = ns.model(
    "items",
    {
        "items": fields.List(fields.Nested(itemFetchModel))
    }
)


# @ns.route("/lost")
class LostItems(Resource):
    # @ns.marshal_with(messageModel)
    @ns.doc(
        description="Fetch owners lost items.",
        params={},
        responses={
            200: "OK",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", itemBulkFetchModel)
    # @ns.response(code=200, model=messageModel, description="OK")

    @authenticate
    def get(self):
        pass

    # @ns.marshal_with(itemFetchModel)
    @ns.doc(
        description="Create record of a lost item",
        params={},
        responses={
            200: "OK",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", itemFetchModel)
    @ns.expect(itemCreateModel)
    @authenticate
    def post(self):
        pass


# @ns.route("/lost/<item_id>")
class LostSingleItem(Resource):
    # @ns.marshal_with(itemFetchModel)
    @ns.doc(
        description="Fetch owners lost items.",
        params={},
        responses={
            200: "OK",
            404: "Not found",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", itemFetchModel)
    @authenticate
    def get(self, item_id):
        pass

    @ns.doc(
        description="Update record of a lost item.",
        params={},
        responses={
            200: "OK",
            404: "Not found",
            400: "Bad request",
            401: "Unauthorized",
        },
    )
    @ns.response(200, "OK", itemFetchModel)
    @ns.expect(itemCreateModel)
    @authenticate
    def patch(self, item_id):
        pass

    @ns.doc(
        description="Delete record of a lost item.",
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
    def delete(self, item_id):
        pass




@ns.route("/found")
class FoundItems(Resource):
    pass


ns.add_resource(LostItems, "/lost")
ns.add_resource(LostSingleItem, "/lost/<item_id>")