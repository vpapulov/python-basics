from flask import Blueprint, render_template

accounts_app = Blueprint("accounts_app", __name__)

ACCOUNTS = {
    1: 'Наличные',
    2: 'Карта Сбер',
    3: 'Вклад Сбер',
    4: 'Карта ВТБ'
}


@accounts_app.route("/", methods=['GET'])
def list():
    return render_template('accounts/list.html', accounts=ACCOUNTS)


@accounts_app.route("/<string:name>", methods=['GET'])
@accounts_app.route("/<int:id>", methods=['GET'])
def detail(id=None, name=None):
    # TODO проверить существование кошелька с данным id/name
    name = ACCOUNTS[id]
    return render_template(
        'accounts/detail.html',
        account_id=id,
        account_name=name
    )
