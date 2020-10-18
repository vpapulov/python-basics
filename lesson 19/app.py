from flask import Flask

from views import account_app

app = Flask(__name__)
app.register_blueprint(account_app, url_prefix='/accounts')

@app.route("/", methods=['GET'])
def index():
    return "<h1>Учет денежных средств</h1>"

