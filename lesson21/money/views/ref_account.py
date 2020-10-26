from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

from models import db, RefAccount

ref_account_app = Blueprint("ref_account_app", __name__)


@ref_account_app.route("/", methods=['GET'])
def list():
    list = RefAccount.query.order_by(RefAccount.name).all()
    return render_template('ref_account/list.html', list=list)


@ref_account_app.route("/<int:item_id>", methods=['GET', 'POST'])
def detail(item_id):
    item = RefAccount.query.filter_by(id=item_id).one_or_none()
    if item is None:
        raise BadRequest(f"Invalid id #{item_id}")
    if request.method == 'GET':
        return render_template(
            'ref_account/detail.html',
            item=item
        )
    elif request.method == 'POST':
        item.name = request.values['name']
        db.session.add(item)
        db.session.commit()
        return jsonify(ok=True)


@ref_account_app.route("new", methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('ref_account/detail.html', is_new=True)
    elif request.method == 'POST':
        new_item = RefAccount(
            name=request.values['name']
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify(ok=True)
