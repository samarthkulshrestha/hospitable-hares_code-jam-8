# import os

from peewee import DateField, Model, SqliteDatabase, TextField

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

    _id = TextField(index=True)
    nametag = TextField()
    created_at = DateField()
    last_login_at = DateField(null=True)
