from flask import request, json
from auth.authentication import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging
from sqlalchemy.exc import *
from views import found_items
from .lost_items import itemFetchModel, itemCreateModel, itemBulkFetchModel, messageModel

logger = logging.getLogger(__name__)
ns = Namespace("items/found", description="API for management of found items", url_prefix="/api")


# @ns.route("/lost")
class FoundItems(Resource):
    # @ns.marshal_with(itemBulkFetchModel)
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
        items = found_items.get_all()
        if not items:
            return {"items": []}
        return marshal({"items": items}, itemBulkFetchModel), 200

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
        try:
            item = found_items.create_new(request.get_json())
            return marshal(item, itemFetchModel), 200
        except SQLAlchemyError:
            abort(400, "Bad request")
        except NoReferenceError:
            abort(400, "Non-existent category")


# @ns.route("/lost/<item_id>")
class FoundSingleItem(Resource):
    # @ns.marshal_with(itemFetchModel)
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
            item = found_items.get_id(item_id)
            return marshal(item, itemFetchModel), 200
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


ns.add_resource(FoundItems, "")
ns.add_resource(FoundSingleItem, "/<item_id>")

