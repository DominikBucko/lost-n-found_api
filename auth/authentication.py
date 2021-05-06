from functools import wraps
import requests
from config import config
import json
import os
from flask import request, abort, g


def authenticate(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            jwt = request.headers.get("Authorization").split("Bearer ")[-1]

            payload = json.dumps({"token": jwt})
            headers = {
                'Authorization': config.auth_server_token,
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", config.auth_server_url, headers=headers, data=payload)
            data = response.json()
            g.user_id = data["email"]

        except Exception:
            abort(401)
        return f(*args, **kwargs)

    return wrap


def check_jwt(jwt):
    try:
        payload = json.dumps({"token": jwt})
        headers = {
            'Authorization': config.auth_server_token,
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", config.auth_server_url, headers=headers, data=payload)
        data = response.json()
        return data["email"]
    except Exception:
        return None
