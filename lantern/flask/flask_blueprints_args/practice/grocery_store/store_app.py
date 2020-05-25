import inject
from flask import Flask
from flask_restful import Api

from errors import my_error_handler, NoSuchUserError, NoSuchStoreError, NoSuchGoodError
from fake_storage import FakeStorage
from routes.goods import Good
from routes.stores import Store
from routes.users import User


def configure(binder):
    db = FakeStorage()
    binder.bind("DB", db)


def make_app():
    # configure our database
    inject.clear_and_configure(configure)

    app = Flask(__name__)
    # API
    api = Api(app)
    api.add_resource(User, "/users", "/users/<int:user_id>")
    api.add_resource(Good, "/goods", "/goods/<int:good_id>")
    api.add_resource(Store, "/stores", "/stores/<int:store_id>")
    # error handlers
    app.register_error_handler(NoSuchUserError, my_error_handler)
    app.register_error_handler(NoSuchStoreError, my_error_handler)
    app.register_error_handler(NoSuchGoodError, my_error_handler)
    return app
