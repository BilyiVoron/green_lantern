from flask import Flask
from sqlalchemy_utils import create_database, database_exists

from .config import Config
from .models import db, User, Good, Store
from .populate_data import get_users, get_goods, get_stores


def get_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

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
        for user in users:
            db.session.add(User(**user))
        db.session.commit()
        print("\n\tUSERS data added to database successfully")

    with app.app_context():
        goods = get_goods()
        for good in goods:
            db.session.add(Good(**good))
        db.session.commit()
        print("\n\tGOODS data added to database successfully")

    with app.app_context():
        stores = get_stores()
        for store in stores:
            db.session.add(Store(**store))
        db.session.commit()
        print("\n\tSTORES data added to database successful\n")

    return app
