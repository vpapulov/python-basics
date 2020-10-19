from flask import Blueprint, request, render_template, jsonify
from tortoise import run_async
import db

doc_income_app = Blueprint("doc_income_app", __name__)


@doc_income_app.route("/", methods=['GET'])
def list():
    # return render_template('accounts/list.html', accounts=ACCOUNTS)
    pass


@doc_income_app.route("new", methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('doc_income/new.html')
    else:
        run_async(create_doc(request.values['account_id'], request.values['sum']))
        return jsonify(ok=True)


async def create_doc(account_id, sum):
    await db.init()
    doc = db.DocIncome(
        account_id=account_id,
        sum=sum
    )
    await doc.save()


@doc_income_app.route("/<int:id>", methods=['GET'])
def detail(id=None):
    # TODO проверить существование документа с данным id
    # name = ACCOUNTS[id]
    # return render_template(
    #     'accounts/detail.html',
    #     account_id=id,
    #     account_name=name
    # )
    pass
