# Controllers are effectively callbacks that run for a particular URL, and they tend to be where a lot of the logic is. 
# Separating the functions into its own class isn't necessary, but a way to better organize our code and make it more readable

from flask import request
from flask_restful import Resource

from .data import activities

class ActivityList(Resource):
	# GET /activities => returns our list of dictionaries from models.py file
    def get(self):
        return {'results': activities}, 200

class ActivityCreate(Resource):
	# POST /activities => appends new item to the data list
    def post(self):
        new_item = request.json
        activities.append(new_item)

        return {'results': activities}, 201

class ActivityDetail(Resource):
    # GET /activity => Grabs a specific item (by finding the key requested) from the data list
    def get(self, key):
            for i, result in enumerate(activities):
                if result['key'] == key:
                    return result
    
            return 'Key does not exist', 404

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
