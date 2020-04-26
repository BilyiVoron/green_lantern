from flask import Blueprint
from flask_restful import Api
from users.routes import UsersRoutes


users = Blueprint("users", __name__)
api_users = Api(users)

api_users.add_resource(UsersRoutes, "/users", "/users/<user_id>")
