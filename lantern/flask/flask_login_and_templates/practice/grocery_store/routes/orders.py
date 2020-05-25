from flask import Blueprint, render_template
from flask_login import current_user, login_required
from flask_restful import Resource

from grocery_store.models import User, Order

orders = Blueprint("orders", __name__)


@orders.route("/user_orders_list")
@login_required
class Orders(Resource):
    def get(self, order_id):
        if order_id:
            order = Order.query.filter_by(user_id=current_user.user_id).first()
            # user = User.query.filter_by(user_id=current_user.user_id).first()
            orders = order.order_id
            for order in orders:
                return order.created_time
            return render_template("orders.html", orders=orders)

    # class Users(Resource):
    #     def get(self, user_id=None):
    #         if user_id:
    #             user = User.query.get(user_id)
    #             if user:
    #                 return marshal(user, users_structure)
    #             return f"No such user with id: {user_id}"
    #         return marshal(User.query.all(), users_structure)
