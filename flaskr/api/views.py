from flask import Blueprint, request

api = Blueprint('api', __name__)


@api.route("/all", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return "Test"
    if request.method == "POST":
        return "Post test"
