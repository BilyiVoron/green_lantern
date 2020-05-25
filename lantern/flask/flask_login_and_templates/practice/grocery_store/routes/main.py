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
        "profile.html", user=current_user.name, email=current_user.email
    )


@main.route("/price-list")
def price_list():
    return render_template("price_list.html", goods=Good.query.all())
