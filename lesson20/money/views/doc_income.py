from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from datetime import datetime
# from lesson19.db import
from db import session, DocIncome, RefAccount

doc_income_app = Blueprint("doc_income_app", __name__)


@doc_income_app.route("/", methods=['GET'])
def list():
    data = session.query(DocIncome).join(RefAccount).all()
    return render_template('doc_income/list.html', data=data)


@doc_income_app.route("new", methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('doc_income/detail.html', is_new=True)
    elif request.method == 'POST':
        new_doc = DocIncome(
            date = datetime.strptime(request.values['date'], '%Y-%m-%d'),
            account_id=int(request.values['account_id']),
            sum=float(request.values['sum']),
            comment=request.values['comment']
        )
        session.add(new_doc)
        session.commit()
        return jsonify(ok=True)


@doc_income_app.route("/<int:id>", methods=['GET', 'POST'])
def detail(id):
    doc = session.query(DocIncome).filter_by(id=id).one()
    if request.method == 'GET':
        return render_template(
            'doc_income/detail.html',
            is_new=False,
            doc=doc
        )
    elif request.method == 'POST':
        doc.date = datetime.strptime(request.values['date'], '%Y-%m-%d')
        doc.account_id = int(request.values['account_id'])
        doc.sum = float(request.values['sum'])
        doc.comment = request.values['comment']
        session.add(doc)
        session.commit()
        return jsonify(ok=True)
