import secrets
import uuid
from functools import wraps

import redis
from flask import request, jsonify, Response

from api import app

redinst = redis.Redis()


def verify_decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "Auth-Token" in request.headers:
            token = request.headers["Auth-Token"]

        if not token:
            return jsonify({"message": "auth token missing"})

        try:
            uid = redinst.get(token)
            print(uid)
            if not uid:
                return jsonify({"message": "invalid token"}), 401

        except:
            return jsonify({"message": "invalid token"}), 401

        return f(uid, *args, **kwargs)

    return decorated


@app.route("/join")
def join() -> Response:
    """Token generation function for join route."""
    token = secrets.token_hex(64)
    _id = uuid.uuid1().int
    redinst.set(token, _id)
    return jsonify({'token': token})


@app.route("/protected")
@verify_decorator
def post(uid):
    uid = uid.decode("utf-8")
    return jsonify({"uid": uid})
