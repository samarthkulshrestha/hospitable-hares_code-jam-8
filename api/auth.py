import secrets
import uuid
from functools import wraps
from typing import Callable

import redis
from flask import Response, jsonify, request

from api import app

redinst = redis.Redis()


def verify_decorator(f: Callable) -> Callable:
    """Verifies the token for routes that only logged-in users are permitted to access."""

    @wraps(f)
    def decorated(*args, **kwargs) -> Response:
        if "Auth-Token" in request.headers:
            token = request.headers["Auth-Token"]
        else:
            return jsonify({"message": "auth token missing"})

        try:
            uid = redinst.get(token)
            # print(uid)
            if not uid:
                return jsonify({"message": "invalid token"}), 401
        except Exception:
            return jsonify({"message": "invalid token"}), 401

        return f(uid, *args, **kwargs)

    return decorated


@app.route("/join")
def join() -> Response:
    """Token generation function for join route."""
    token = secrets.token_hex(64)
    _id = uuid.uuid1().int
    redinst.set(token, _id)
    return jsonify({"token": token})


@app.route("/protected")
@verify_decorator
def protected(uid: str) -> Response:
    """Test route."""
    uid = uid.decode("utf-8")
    return jsonify({"uid": uid})
