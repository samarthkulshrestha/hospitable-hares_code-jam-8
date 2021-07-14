import uuid
from datetime import datetime

from flask import Response, jsonify, request

from api import app
from api.auth import verify_decorator
from api.schema import Post, User


@app.route("/posts")
def posts() -> Response:
    """Paginate the posts"""
    limit = 25
    posts = []
    page_no = request.args.get("page_no", "1")
    if not page_no.isnumeric():
        return jsonify({"error": "page_no should be numeric"})

    for post in (
        Post.select().order_by(Post.created_at.desc()).paginate(int(page_no), limit)
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
    post = Post.create(
        _id=str(_id), body=request.json["body"], creator=user, created_at=datetime.now()
    )
    post.save()
    return Response(status=200)
