from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "<h1>Учет денеждных средств</h1>"

@app.route("/account/<string:name>", methods=['GET'])
@app.route("/account/<int:id>", methods=['GET'])
def account(id = None, name = None):
    # TODO проверить существование кошелька с данным id/name
    print(request, id, name)
    return f"<h1>Кошелек {id}</h1>"