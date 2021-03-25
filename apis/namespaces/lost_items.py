from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging
from views import *
from views import lost_items
from sqlalchemy.exc import *
from sqlalchemy.orm.exc import NoResultFound

logger = logging.getLogger(__name__)
ns = Namespace("items/lost", description="API for management of lost items", url_prefix="/api")

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
    @ns.marshal_with(itemFetchModel)
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

    @ns.marshal_with(itemFetchModel)
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
        try:
            return lost_items.create_new(request.get_json())
        except SQLAlchemyError:
            abort(400, "Bad request")
        except NoReferenceError:
            abort(400, "Non-existent category")


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
        try:
            return lost_items.get_id(item_id)
        except SQLAlchemyError:
            abort(404, "No result.")


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