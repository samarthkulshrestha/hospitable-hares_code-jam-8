import secrets
import uuid
from datetime import datetime
from functools import wraps
from typing import Callable

import redis
from faker import Faker
from flask import Response, jsonify, request

from api import app
from api.schema import Post, User, db

db.connect()
db.create_tables([User])

redinst = redis.Redis()
faker = Faker()


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
                return jsonify({"message": "invalid auth token"}), 401
        except Exception:
            return jsonify({"message": "invalid auth token"}), 401

        return f(uid.decode("utf-8"), *args, **kwargs)

    return decorated


@app.route("/join")
def join() -> Response:
    """Token generation function for join route."""
    token = secrets.token_hex(64)
    _id = uuid.uuid1().int
    nametag = faker.user_name()

    redinst.set(token, _id)
    user = User.create(_id=_id, nametag=nametag, created_at=datetime.now())
    user.save()

    return jsonify({"nametag": nametag, "token": token})


@app.route("/users")
def users() -> Response:
    """List all users in the database."""
    users = []
    for user in User.select():
        users.append([user.nametag, user._id, user.created_at])
    return jsonify({"users": users})


@app.route("/posts")
def posts() -> Response:
    """Paginate the posts"""
    limit = 25
    posts = []
    page_no = request.args.get('page_no', '1')
    if not page_no.isnumeric():
        return jsonify({
            'error': "page_no should be numeric"
        })

    for post in Post.select().order_by(Post.created_at.desc()).paginate(int(page_no), limit):
        posts.append({
            '_id': post._id,
            'body': post.body,
            'creator': post.creator._id,
            'created_at': post.created_at
        })

    return jsonify(posts)


@app.route("/protected")
@verify_decorator
def protected(uid: str) -> Response:
    """Test route."""
    return jsonify({"uid": uid})
