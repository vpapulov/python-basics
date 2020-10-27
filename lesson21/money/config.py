import os

PG_HOST = os.environ["PG_HOST"]
PG_USER = os.environ["PG_USER"]
PG_PWD = os.environ["PG_PWD"]

SQLALCHEMY_DATABASE_URI = f"postgres+psycopg2://{PG_USER}:{PG_PWD}@{PG_HOST}:5432/money"
