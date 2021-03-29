from flask import Flask
from apis.api_v1 import init
from flask_restx import Api, Resource, fields
from config import config
from flask_cors import CORS
# from flask_marshmallow import Marshmallow
# from flask_oauthlib.client import OAuth
import os

from os.path import join, dirname

from flask import Flask, redirect, url_for, session

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = '/oauth2callback'

app = Flask(__name__)
app.secret_key = "bobojesmutny"
CORS(app)

# oauth = OAuth()
#
# google = oauth.remote_app(name="google",
#                           base_url='https://www.google.com/accounts/',
#                           authorize_url='https://accounts.google.com/o/oauth2/auth',
#                           request_token_url=None,
#                           request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
#                                                 'response_type': 'code'},
#                           access_token_url='https://accounts.google.com/o/oauth2/token',
#                           access_token_method='POST',
#                           access_token_params={'grant_type': 'authorization_code'},
#                           consumer_key=GOOGLE_CLIENT_ID,
#                           consumer_secret=GOOGLE_CLIENT_SECRET)
#
#
# @app.route('/')
# def index():
#     access_token = session.get('access_token')
#     if access_token is None:
#         return redirect(url_for('login'))
#
#     access_token = access_token[0]
#     from urllib.request import Request, urlopen
#     from urllib.error import URLError, HTTPError
#
#     headers = {'Authorization': 'OAuth ' + access_token}
#     req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
#                   None, headers)
#     try:
#         res = urlopen(req)
#     except HTTPError as e:
#         if e.code == 401:
#             # Unauthorized - bad token
#             session.pop('access_token', None)
#             return redirect(url_for('login'))
#
#     return res.read()
#
#
# @app.route('/login')
# def login():
#     callback = url_for('authorized', _external=True)
#     return google.authorize(callback=callback)
#
#
# @app.route(REDIRECT_URI)
# @google.authorized_handler
# def authorized(resp):
#     access_token = resp['access_token']
#     session['access_token'] = access_token, ''
#     return redirect(url_for('index'))
#
#
# @google.tokengetter
# def get_access_token():
#     return session.get('access_token')
#
#
# # ma = Marshmallow(app)


def initialize_api():
    init(app)
