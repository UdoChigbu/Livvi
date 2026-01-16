from flask import Blueprint, request
welcome_blueprint = Blueprint('welcome', __name__)

@welcome_blueprint.route("/welcome", methods = ["POST"])
def welcome():
    return "welcome page"
        

