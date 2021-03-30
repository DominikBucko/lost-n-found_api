from apis.api_v1 import init
from config import config
from flask_cors import CORS
import os
from flask import Flask, redirect, url_for, session

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = '/oauth2callback'

app = Flask(__name__)
app.secret_key = "bobojesmutny"
CORS(app)

def apply_configuration():
    app.config["UPLOAD_FOLDER"] = config.upload_folder
    app.config["MAX_CONTENT_LENGTH"] = config.max_upload_size


def initialize_api():
    apply_configuration()
    init(app)

