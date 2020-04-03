from flask import Flask, jsonify, request
import inject


app = Flask(__name__)


@app.route("/users", methods=["POST"])
def create_user():
    db = inject.instance("DB")
    user_id = db.users.add(request.json)
    # __import__("pdb").set_trace()

    return jsonify({"user_id": user_id})



#
#
# if __name__ == "__main__":
#     app.run()
