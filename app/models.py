from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.String, nullable=False)
    participants = db.Column(db.String, default=1)
    price = db.Column(db.String, default=0)
    link = db.Column(db.String)
    key = db.Column(db.String)
    accessibility = db.Column(db.String)

    def __init__(self, activity, type, participants, price, link, key, accessibility):
        self.activity = activity
        self.type = type
        self.participants = participants
        self.price = price
        self.link = link
        self.key = key
        self.accessibility = accessibility

    def __repr__(self):
        return f'<Activity: {self.activity}>'