from flask import Flask, render_template
from flask_migrate import Migrate
import config

from views import ref_account_app
from views import doc_income_app
from models import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
)
app.register_blueprint(ref_account_app, url_prefix='/accounts')
app.register_blueprint(doc_income_app, url_prefix='/income')

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')
