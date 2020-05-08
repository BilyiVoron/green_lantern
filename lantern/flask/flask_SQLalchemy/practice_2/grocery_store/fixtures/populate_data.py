import csv
import os

from grocery_store import app, db
from grocery_store.models import User, Good, Store
from grocery_store.config import FIXTURES_DIR
from sqlalchemy_utils import create_database, drop_database, database_exists

USERS_DIR = os.path.join(FIXTURES_DIR, "users.csv")
GOODS_DIR = os.path.join(FIXTURES_DIR, "goods.csv")
STORES_DIR = os.path.join(FIXTURES_DIR, "stores.csv")


def get_users():
    with open(USERS_DIR, "r") as f:
        reader = csv.DictReader(f)
        users = [user for user in reader]
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


with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print("\nConnecting to database...")
        print("\nConnection succeeded")
    else:
        print(f"\nDatabase does not exists {db.engine.url}")
        create_database(db.engine.url)
        db.create_all()
        print("\nCreating database...")
        print("\nDatabase successfully created")

with app.app_context():
    users = get_users()
    goods = get_goods()
    stores = get_stores()
    for user in users:
        db.session.add(User(**user))
    for good in goods:
        db.session.add(Good(**good))
    for store in stores:
        db.session.add(Store(**store))
    db.session.commit()
    print("\n\tData added to database successfully")

