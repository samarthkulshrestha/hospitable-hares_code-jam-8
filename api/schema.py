# import os

import datetime

from peewee import (
    DateTimeField, ForeignKeyField, Model, SqliteDatabase, TextField
)

# db = PostgresqlDatabase(
#     str(os.environ.get("DB_NAME", "hospitable-hares_code-jam-8")),
#     user=str(os.environ.get("DB_USER", "postgres")),
#     password=str(os.environ.get("DB_PASSWORD")),
#     host=str(os.environ.get("DB_HOST", "localhost")),
#     port=int(os.environ.get("DB_PORT", "5432"))
# )

db = SqliteDatabase("data.db")


class BaseTable(Model):
    """Base table."""

    class Meta:
        database = db


class User(BaseTable):
    """User schema."""

    _id = TextField(index=True, primary_key=True)
    nametag = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    last_login_at = DateTimeField(null=True)


class Box(BaseTable):
    """Box schema."""

    _id = TextField(index=True, primary_key=True)
    name = TextField(index=True)
    creator = ForeignKeyField(User, backref="boxes")
    created_at = DateTimeField(default=datetime.datetime.now)


class Post(BaseTable):
    """Posts Schema"""

    _id = TextField(index=True, primary_key=True)
    body = TextField()
    creator = ForeignKeyField(User, backref="posts")
    box = ForeignKeyField(Box, backref="posts")
    created_at = DateTimeField(default=datetime.datetime.now)
