import jwt
from config import key


def encode(payload):
    token = jwt.encode(payload, key)
    # print(token)
    return token


def decode(token):
    decoded = jwt.decode(token, options={"verify_signature": False}, key=key)
    # print(decoded)
    return decoded
