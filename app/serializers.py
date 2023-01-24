from .models import db, Activity

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ActivitySchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Activity
        loadInstance = True

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)

