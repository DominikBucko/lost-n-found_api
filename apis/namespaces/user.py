from flask import request, json
from auth.auth import authenticate
from flask_restx import Namespace, Resource, reqparse, fields, Model, fields, marshal_with, abort, marshal
import logging


logger = logging.getLogger(__name__)
ns = Namespace("user", description="Endpoints for user management", url_prefix="/api")

messageModel = ns.model(
    "message",
    {
        "message": fields.String,
    },
)
