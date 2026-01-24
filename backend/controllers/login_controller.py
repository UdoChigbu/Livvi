from flask import Blueprint, request, jsonify, render_template
login_blueprint= Blueprint('login', __name__)

@login_blueprint.route("/login", methods=["POST","GET"])
def login_route():
    return render_template('login.html')

    
