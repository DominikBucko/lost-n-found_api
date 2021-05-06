from app import app
from auth.authentication import check_jwt
from flask import request, session
from flask_socketio import send, emit
from flask_socketio import SocketIO
from flask_cors import cross_origin

open_connections = {}

socketio = SocketIO(app)


# @cross_origin
@socketio.on("authenticate")
def authenticate_socket(data):
    email = check_jwt(data)
    if email:
        open_connections[email] = request.sid
        emit("response", {"status": "Authentication successful"})
    else:
        emit("response", {"status": "Authentication unsuccessful"})


# @cross_origin
@socketio.on("message")
def test_event(data):
    print(data)


def notify(uid, json):
    socketio.emit("notification", json, room=open_connections[uid])


# socketio.run(app, port=8085, debug=True)