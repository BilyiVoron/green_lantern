import inject
from flask import request
from flask_restful import Resource, reqparse


class Good(Resource):
    def get(self):
        db = inject.instance("DB")
        return db.goods.get_all()

    def post(self):
        db = inject.instance("DB")
        number_of_created_goods = db.goods.add_many(request.json)
        return {"number of items created": number_of_created_goods}, 201
