from tortoise import Tortoise, run_async, fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True, )
    name = fields.TextField()
    username = fields.TextField()
    phone = fields.TextField()
    email = fields.TextField()


class Post(Model):
    id = fields.IntField(pk=True, )
    userId = fields.IntField()
    title = fields.TextField()
    body = fields.TextField()


class Comment(Model):
    id = fields.IntField(pk=True, )
    postId = fields.IntField()
    name = fields.TextField()
    email = fields.TextField()
    body = fields.TextField()


async def init():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['mydb']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
