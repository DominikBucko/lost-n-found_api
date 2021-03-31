from functools import wraps
from .encode_decode_token import decode, encode
import os
from flask import request, abort, g

print(encode({"email": "test_user1@email.com"}))
print(encode({"email": "test_user2@email.com"}))

def authenticate(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # PLACEHOLDER
        try:
            decoded = decode(request.headers.get("Authorization").split("Bearer ")[-1])
            g.user_id = decoded["email"]
        except Exception:
            abort(401)
        return f(*args, **kwargs)
    return wrap


