from flask import Blueprint, request, jsonify, render_template
welcome_blueprint = Blueprint('welcome', __name__)

@welcome_blueprint.route("/welcome", methods = ["POST", "GET"])
def welcome():
    return render_template('welcome.html')
        

