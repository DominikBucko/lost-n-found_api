from flask import request, json, send_file
from auth.authentication import authenticate
from auth.authorization import *
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
from werkzeug.utils import secure_filename
from models.category import Category
from views import metadata
import uuid
from config import config
import os
import logging


logger = logging.getLogger(__name__)
ns = Namespace("metadata", description="Retrieval of metadata needed for application", url_prefix="/api")


@ns.route("")
class Metadata(Resource):
    @ns.doc(
        description="Retrieve metadata",
        params={},
        responses={
            200: "OK",
            401: "Unauthorized",
        },
    )
    @authenticate
    def get(self):
        res = {}
        res["categories"] = metadata.get_categories()
        return res

