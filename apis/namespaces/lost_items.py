from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging
from views import *
from views import lost_items

logger = logging.getLogger(__name__)
ns = Namespace("lost_items", description="API for management of lost items", url_prefix="/api")

# messageModel = ns.model(
#     "item", {
#         "category": fields.String,
#         "brand": fields.String,
#         "title": fields.String,
#         "description": fields.String,
#         "GPS-lat": fields.Float,
#         "GPS-lon": fields.Float,
#         "images": fields.List(fields.String, description='image')
#         # "images": fields.List(fields.Nested(image)),
#     }
# )

messageModel = ns.model(
    "message",
    {
    "message": fields.String
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
        "images": fields.List(fields.Url),
    }
)

itemBulkFetchModel = ns.model(
    "fetchItems",
    {
        "items": fields.List(fields.Nested(itemFetchModel))
    }
)


# @ns.route("/lost")
class LostItems(Resource):
    @ns.marshal_with(itemBulkFetchModel)
    @ns.doc(
        description="Fetch owners items.",
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
        return lost_items.get_all()

    # @ns.marshal_with(itemFetchModel)
    @ns.doc(
        description="Create record of item",
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
        return lost_items.post()


# @ns.route("/lost/<item_id>")
class LostSingleItem(Resource):
    @ns.marshal_with(itemFetchModel)
    @ns.doc(
        description="Fetch owners items.",
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
        return lost_items.get_id(item_id)

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
    @ns.response(200, "OK", messageModel)
    @ns.expect(itemCreateModel)
    @authenticate
    def patch(self, item_id):
        pass

    @ns.doc(
        description="Delete record of item.",
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


ns.add_resource(LostItems, "")
ns.add_resource(LostSingleItem, "/<item_id>")