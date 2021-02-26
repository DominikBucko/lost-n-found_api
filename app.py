from flask import Flask
from apis.api_v1 import init
from flask_restx import Api, Resource, fields
from config import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def initialize_api():
    init(app)
