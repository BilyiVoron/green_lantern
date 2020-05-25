import csv
import logging
import os
from random import randint, choice, sample

from flask_script import Command

from grocery_store.config import FIXTURES_DIR
from grocery_store.models import User, Good, Store, Order, OrderLine

USERS_DIR = os.path.join(FIXTURES_DIR, "users.csv")
GOODS_DIR = os.path.join(FIXTURES_DIR, "goods.csv")
STORES_DIR = os.path.join(FIXTURES_DIR, "stores.csv")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-6s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    # filename="logfile.log",  # if you want!!!
)


def get_users():
    with open(USERS_DIR, "r") as f:
        reader = csv.DictReader(f)
        users = [user for user in reader]
        for user in users:
            user[
                "password"
            ] = "sha256$TlFrkAzh$807b3e82dd1b2c6ee26e64ab8ad1ad55fc462d37e9a3b6b5bdd387530867864f"
    return users


def get_goods():
    with open(GOODS_DIR, "r") as f:
        reader = csv.DictReader(f)
        goods = [good for good in reader]
    return goods


def get_stores():
    with open(STORES_DIR, "r") as f:
        reader = csv.DictReader(f)
        stores = [store for store in reader]
    return stores


class Populate(Command):
    def run(self):
        from grocery_store import app, db

        with app.app_context():
            users = get_users()
            goods = get_goods()
            stores = get_stores()
            for user in users:
                db.session.add(User(**user))
            db.session.commit()
            for good in goods:
                db.session.add(Good(**good))
            db.session.commit()
            for store in stores:
                db.session.add(Store(**store))
            db.session.commit()
            logging.info("Data added to database successfully")


class PopulateOrders(Command):
    def run(self):
        from grocery_store import app, db

        with app.app_context():
            users = User.query.all()
            goods = Good.query.all()
            stores = Store.query.all()
            for user in users:
                number_of_orders = randint(1, 5)
                for _ in range(number_of_orders):
                    number_of_goods = randint(1, 10)
                    order = Order()
                    order_lines = [
                        OrderLine(good=good) for good in sample(goods, number_of_goods)
                    ]
                    order.order_lines = order_lines
                    order.user = user
                    order.store = choice(stores)
                    db.session.add(order)
            db.session.commit()
