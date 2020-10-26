from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from werkzeug.exceptions import BadRequest
from datetime import datetime

from models import db, DocIncome, RefAccount

doc_income_app = Blueprint("doc_income_app", __name__)


@doc_income_app.route("/", methods=['GET'])
def list():
    data = DocIncome.query.join(RefAccount).order_by(DocIncome.date).all()
    return render_template('doc_income/list.html', data=data)


@doc_income_app.route("new", methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        account_list = RefAccount.query.order_by(RefAccount.name).all()
        return render_template(
            'doc_income/detail.html',
            is_new=True,
            account_list=account_list
        )
    elif request.method == 'POST':
        new_doc = DocIncome(
            date=datetime.strptime(request.values['date'], '%Y-%m-%d'),
            account_id=int(request.values['account_id']),
            sum=float(request.values['sum']),
            comment=request.values['comment']
        )
        db.session.add(new_doc)
        db.session.commit()
        return jsonify(ok=True)


@doc_income_app.route("/<int:doc_id>", methods=['GET', 'POST'])
def detail(doc_id):
    doc = DocIncome.query.filter_by(id=doc_id).one_or_none()
    if doc is None:
        raise BadRequest(f"Invalid id #{doc_id}")
    if request.method == 'GET':
        account_list = RefAccount.query.order_by(RefAccount.name).all()
        return render_template(
            'doc_income/detail.html',
            is_new=False,
            doc=doc,
            account_list=account_list
        )
    elif request.method == 'POST':
        doc.date = datetime.strptime(request.values['date'], '%Y-%m-%d')
        doc.account_id = int(request.values['account_id'])
        doc.sum = float(request.values['sum'])
        doc.comment = request.values['comment']
        db.session.add(doc)
        db.session.commit()
        return jsonify(ok=True)
