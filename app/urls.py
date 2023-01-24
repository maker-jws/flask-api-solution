# urls.py is used to set a route for each controller
# Python classes in controllers.py take the web request from urls.py and returns a JSON response

from flask_restful import Api

from .controllers import *

api = Api()

api.add_resource(ActivityList, '/activities/')
api.add_resource(ActivityCreate, '/activities/')
api.add_resource(ActivityDetail, '/activity/<int:id>')
api.add_resource(ActivityUpdate, '/activity/<int:id>')
api.add_resource(ActivityDelete, '/activity/<int:id>')