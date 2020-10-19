from tortoise import Tortoise, fields
from tortoise.models import Model


class DocIncome(Model):
    id = fields.IntField(pk=True)
    account_id = fields.IntField()
    sum = fields.FloatField()


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['db']}
    )
    await Tortoise.generate_schemas()
