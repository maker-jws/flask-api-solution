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
            return {'results': activities}, 200
        except Exception as e:
            return {'message': str(e)}, 418

        

class ActivityCreate(Resource):
	# POST /activities => appends new item to the data list
    def post(self):
        try:
            new_item = request.json
            new_activity = Activity(**new_item)
            print(new_activity)
            db.session.add(new_activity)
            db.session.commit()
            # activities.append(new_item)

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
    def put(self, key):
        updated_item = request.json
        for i, result in enumerate(activities):
            if result['key'] == key:
                updated_result = {**result, **updated_item}
                activities[i] = updated_result
        
        return activities, 201

class ActivityDelete(Resource):
    # DELETE /activity => Deletes an item by key
    def delete(self, key):
        for i, result in enumerate(activities):
            if result['key'] == key:
                deleted_activity = activities.pop(i)
                return deleted_activity, 200
