from flask import Blueprint, render_template
from flask_login import current_user, login_required

from grocery_store.models import Good

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile():
    return render_template(
        "profile.html", user=current_user.name, email=current_user.email,
    )


@main.route("/user_orders_list")
@login_required
def orders():
    user_orders_list = []
    for order in current_user.orders:
        data = {
            "store": order.store.name,
            "date": order.created_time,
            "price": sum([good.good.price for good in order.order_lines]),
            "goods": {good.good.name: good.good.price for good in order.order_lines},
        }
        user_orders_list.append(data)
    return render_template("orders.html", orders=user_orders_list)


@main.route("/manage_stores")
@login_required
def stores():
    return render_template("stores.html", stores=current_user.manage_stores)


@main.route("/price-list")
def price_list():
    return render_template("price_list.html", goods=Good.query.all())
