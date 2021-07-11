import secrets
import uuid

import redis
from flask import Response

from api import app

redinst = redis.Redis()


@app.route("/join")
def join() -> Response:
    """Token generation function for join route."""
    token = secrets.token_hex(64)
    _id = uuid.uuid1().int
    redinst.set(token, _id)
    return token
