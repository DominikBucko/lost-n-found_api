from flask import Blueprint
from flask_restx import Api, Resource, fields
from apis.namespaces.lost_items import ns as item_mgmt
from apis.namespaces.found_items import ns as found_items
from apis.namespaces.matches import ns as matches
from apis.namespaces.uploads import ns as uploads
from apis.namespaces.user import ns as user

blueprint = Blueprint("v1", __name__, url_prefix="/api")


def init(app):
    api = Api(blueprint, version='1.0', title='Lost & found',
              description='Lost & found application API',
              base_url="/api"
              )
    app.register_blueprint(blueprint)
    api.add_namespace(item_mgmt)
    api.add_namespace(found_items)
    api.add_namespace(matches)
    api.add_namespace(uploads)
    api.add_namespace(user)
