# Controllers are effectively callbacks that run for a particular URL, and they tend to be where a lot of the logic is. 
# Separating the functions into its own class isn't necessary, but a way to better organize our code and make it more readable

from flask import request
from flask_restful import Resource
from .serializers import *

from .data import activities

class ActivityList(Resource):
	# GET /activities => returns our list of dictionaries from data.py file
    def get(self):
        try :
            activities = Activity.query.all()
            return activities_schema.dump(activities), 200
        except Exception as e:
            return {'message': str(e)}, 418

        

class ActivityCreate(Resource):
	# POST /activities => appends new item to the data list
    def post(self):
        try:
            new_item = request.json
            new_activity = Activity(**new_item)
            db.session.add(new_activity)
            db.session.commit()
            return activity_schema.dump(new_activity), 201

        except Exception as e:
            return {'message': str(e)}, 418  

class ActivityDetail(Resource):
    # GET /activity => Grabs a specific item (by finding the key requested) from the data list
    def get(self, id):

        try:
            activity = Activity.query.get_or_404(id)
            return activity_schema.dump(activity), 200

        except Exception as e:
            return {'message': str(e)}, 418

            # for i, result in enumerate(activities):
            #     if result['key'] == key:
            #         return result
    
            # return 'Key does not exist', 404

class ActivityUpdate(Resource):
    # PUT /activity => Updates the item and returns the dictionary with the updated items set by the user
    def put(self, id):
        try:
            item_data = request.json
            Activity.query.filter_by(id=id).update(item_data)
            updated_activity = Activity.query.get_or_404(id)
            db.session.commit()
            return activity_schema.dump(updated_activity), 201
        except Exception as e:
            return {'message': str(e)}, 418

class ActivityDelete(Resource):
    # DELETE /activity => Deletes an item by key
     def delete(self, id):

        try:
            activity = Activity.query.get_or_404(id)
            deleted_activity = {**activity_schema.dump(activity)}
            db.session.delete(activity)
            db.session.commit()
            deleted_activity['deleted'] = True
            return deleted_activity, 200

        except Exception as e:
            return {'message': str(e)}, 418
