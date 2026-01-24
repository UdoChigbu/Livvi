from flask import Flask, jsonify, render_template
from backend.controllers.upload_controller import upload_blueprint #imports ALL routes from upload controller
from backend.controllers.welcome_controller import welcome_blueprint
from backend.controllers.login_controller import login_blueprint
app = Flask(__name__)

app.register_blueprint(upload_blueprint) #registers all the routes from the upload controller
app.register_blueprint(welcome_blueprint)
app.register_blueprint(login_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)