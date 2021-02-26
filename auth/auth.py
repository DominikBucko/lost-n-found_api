from functools import wraps
from flask import request, abort, g


def authenticate(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # PLACEHOLDER
        return f(*args, **kwargs)
    return wrap
