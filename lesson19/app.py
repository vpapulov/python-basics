from flask import Flask, render_template

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, DocIncome

from views import ref_account_app
from views import doc_income_app

app = Flask(__name__)
app.register_blueprint(ref_account_app, url_prefix='/accounts')
app.register_blueprint(doc_income_app, url_prefix='/income')

engine = create_engine('sqlite:///money.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')
