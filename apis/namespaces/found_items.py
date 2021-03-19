from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging
from .lost_items import LostItems, LostSingleItem


logger = logging.getLogger(__name__)
ns = Namespace("found_items", description="API for management of found items", url_prefix="/api")


# @ns.route("/found")
class FoundItems(LostItems):
    def __init__(self):
        super(FoundItems, self).__init__()


class FoundSingleItem(LostSingleItem):
    def __init__(self):
        super(FoundSingleItem, self).__init__()


ns.add_resource(FoundItems, "")
ns.add_resource(FoundSingleItem, "/<item_id>")
