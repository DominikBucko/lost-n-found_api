from flask import request, json, send_file
from auth.authentication import authenticate
from auth.authorization import *
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
from werkzeug.utils import secure_filename
from views import files
import uuid
from config import config
import os
import logging


logger = logging.getLogger(__name__)
ns = Namespace("files", description="Endpoints for upload of binary files", url_prefix="/api")

messageModel = ns.model(
    "message",
    {
        "message": fields.String,
    },
)


@ns.route("/upload/<item_id>")
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
    def put(self, item_id):
        if "file" not in request.files:
            abort(400, "No file included.")
        if not item_id:
            abort(400, "Missing item ID")
        if not check_write_permissions(item_id):
            abort(403, "Unauthorized")

        file = request.files["file"]
        if file.filename == '':
            abort(400, "No file selected.")
        if file:
            filename = secure_filename(f"{uuid.uuid4()}.{file.filename.split('.')[-1]}")
            file.save(os.path.join(config.upload_folder, filename))
            files.register_file(filename=filename, item=item_id)
            return {"message": "File uploaded successfully."}

@ns.route("/download/<item_id>/<filename>")
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
    def get(self, item_id, filename):
        if not check_read_permissions(item_id):
            abort(403, "Unauthorized")
        if not files.check_file_ownership(filename, item_id):
            abort(403, "Unauthorized")

        try:
            return send_file(os.path.join(config.upload_folder, filename))
        except FileNotFoundError:
            abort(404, "File not found")
