from flask import Flask, render_template

from views import accounts_app
from views import doc_income_app

app = Flask(__name__)
app.register_blueprint(accounts_app, url_prefix='/accounts')
app.register_blueprint(doc_income_app, url_prefix='/income')

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

