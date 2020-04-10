from flask import Flask, jsonify, request
import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f"No such user_id {user_id}"


class NoSuchStoreError(Exception):
    def __init__(self, store_id):
        self.message = f"No such store_id {store_id}"


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
@app.errorhandler(NoSuchStoreError)
def my_id_error_handler(e):
    return jsonify({"error": e.message}), 404


@app.route("/users", methods=["POST"])
def create_user():
    db = inject.instance("DB")
    user_id = db.users.add(request.json)

    return jsonify({"user_id": user_id}), 201


@app.route("/users/<int:user_id>")
def get_user(user_id):
    db = inject.instance("DB")
    user = db.users.get_user_by_id(user_id)

    return jsonify(user)


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    db = inject.instance("DB")
    db.users.update_user_by_id(user_id, request.json)

    return jsonify({"status": "success"})


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db = inject.instance("DB")
    db.users.remove_user_by_id(user_id)

    return jsonify({"status": "success"})


@app.route("/goods", methods=["POST"])
def create_good():
    db = inject.instance("DB")
    goods = db.goods.add(request.json)

    return jsonify({"numbers_of_items_created": len(goods)}), 201


@app.route("/goods/<int:good_id>")
def get_one_good(good_id):
    db = inject.instance("DB")
    good = db.goods.get_good_by_id(good_id)

    return jsonify(good)


@app.route("/goods")
def get_all_goods():
    db = inject.instance("DB")
    good = db.goods.get_goods()

    return jsonify(good)


@app.route("/goods/<int:good_id>", methods=["PUT"])
def update_one_good(good_id):
    db = inject.instance("DB")
    db.goods.update_good_by_id(good_id, request.json)

    return jsonify({"successfully_updated": 1})


@app.route("/goods", methods=["PUT"])
def update_some_goods():
    db = inject.instance("DB")
    update_count, error_count = db.goods.update_goods(request.json)
    if error_count:
        return jsonify(
            {
                "successfully_updated": update_count,
                "errors": {"no such id in goods": error_count},
            }
        )
    else:
        return jsonify({"successfully_updated": update_count})


@app.route("/goods/<int:good_id>", methods=["DELETE"])
def delete_good(good_id):
    db = inject.instance("DB")
    db.goods.remove_good_by_id(good_id)

    return jsonify({"status": "success"})


@app.route("/goods", methods=["DELETE"])
def delete_some_goods():
    db = inject.instance("DB")
    update_count, error_count = db.goods.remove_goods(request.json)
    if error_count:
        return jsonify(
            {
                "successfully_deleted": update_count,
                "errors": {"no such id in goods": error_count},
            }
        )
    else:
        return jsonify({"successfully_deleted": update_count})


@app.route("/stores", methods=["POST"])
def create_store():
    db = inject.instance("DB")
    store_id = db.stores.add(request.json)

    return jsonify({"store_id": store_id}), 201


@app.route("/stores/<int:store_id>")
def get_store(store_id):
    db = inject.instance("DB")
    store = db.stores.get_store_by_id(store_id)

    return jsonify(store)


@app.route("/stores/<int:store_id>", methods=["PUT"])
def update_store(store_id):
    db = inject.instance("DB")
    db.stores.update_store_by_id(store_id, request.json)

    return jsonify({"status": "success"})


@app.route("/stores/<int:store_id>", methods=["DELETE"])
def delete_store(store_id):
    db = inject.instance("DB")
    db.stores.remove_store_by_id(store_id)

    return jsonify({"status": "success"})
