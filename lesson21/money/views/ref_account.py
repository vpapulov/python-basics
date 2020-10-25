from flask import Blueprint, render_template, request, url_for, redirect, jsonify

from db import session, RefAccount

ref_account_app = Blueprint("ref_account_app", __name__)


@ref_account_app.route("/", methods=['GET'])
def list():
    list = session.query(RefAccount).all()
    return render_template('ref_account/list.html', list=list)


@ref_account_app.route("/<int:id>", methods=['GET', 'POST'])
def detail(id):
    item = session.query(RefAccount).filter_by(id=id).one()
    if request.method == 'GET':
        return render_template(
            'ref_account/detail.html',
            item=item
        )
    elif request.method == 'POST':
        item.name = request.values['name']
        session.add(item)
        session.commit()
        return jsonify(ok=True)


@ref_account_app.route("new", methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('ref_account/new.html')
    elif request.method == 'POST':
        new_item = RefAccount(
            name=request.values['name']
        )
        session.add(new_item)
        session.commit()
        return jsonify(ok=True)
