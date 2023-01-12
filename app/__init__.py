from flask import Flask

from .urls import api

# Application Factory: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)

    # init_app is common in application factories. It's a way of 
    # constructing an instance of the particular package to your application
    api.init_app(app)

    return app