import uuid
from datetime import datetime

from flask import Response, jsonify, request

from api import app
from api.auth import verify_decorator
from api.schema import Box, Post, User


@app.route("/posts", methods=["POST"])
def posts() -> Response:
    """Paginate the posts"""
    limit = 25
    posts = []
    box = Box.get(Box._id == request.json["box_id"])
    if not box:
        return jsonify({"message": "invalid box id"})
    page_no = request.args.get("page_no", "1")
    if not page_no.isnumeric():
        return jsonify({"error": "page_no should be numeric"})

    for post in (
        box.posts.select()
        .order_by(Post.created_at.desc())
        .paginate(int(page_no), limit)
    ):
        posts.append(
            {
                "_id": post._id,
                "body": post.body,
                "creator": post.creator._id,
                "created_at": post.created_at,
            }
        )

    return jsonify(posts)


@app.route("/post", methods=["POST"])
@verify_decorator
def post(uid: str) -> Response:
    """Route for adding a post to the database."""
    user = User.select().where(User._id == uid).get()
    _id = uuid.uuid1().int
    box = Box.select().where(Box._id == request.json["box_id"])
    if not box:
        return jsonify({"message": "invalid box id"})
    post = Post.create(
        _id=str(_id),
        body=request.json["body"],
        creator=user,
        box=box,
        created_at=datetime.now(),
    )
    post.save()
    return Response(status=200)


@app.route("/new-box", methods=["POST"])
@verify_decorator
def new_box(uid: str) -> Response:
    """Route for creating a new box."""
    user = User.select().where(User._id == uid).get()
    _id = uuid.uuid1().int
    box = Box.create(
        _id=str(_id), name=request.json["name"], creator=user, created_at=datetime.now()
    )
    box.save()
    return jsonify({"box_id": box._id, "name": box.name})


@app.route("/boxes", methods=["GET", "POST"])
def boxes() -> Response:
    """Paginate the boxes"""
    limit = 10
    boxes = []
    page_no = request.args.get("page_no", "1")
    if not page_no.isnumeric():
        return jsonify({"error": "page_no should be numeric"})

    for box in (
        Box.select()
        .order_by(Box.created_at.desc())
        .paginate(int(page_no), limit)
    ):
        boxes.append(
            {
                "_id": box._id,
                "name": box.name,
                "creator": box.creator._id,
                "created_at": box.created_at,
            }
        )

    return jsonify(boxes)
