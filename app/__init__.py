from flask import Flask
from flask_migrate import Migrate

from .config import config # dictionary with 'development' key
from .urls import api, db
# from .models import db

from flask_marshmallow import Marshmallow

# Application Factory: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)
    migrate = Migrate()
    ma = Marshmallow()

    # init_app is common in application factories. It's a way of 
    # constructing an instance of the particular package to your application
    app.config.from_object(config['development'])
    db.init_app(app)
    migrate.init_app(app,db)
    ma.init_app(app)
    api.init_app(app)

    return app