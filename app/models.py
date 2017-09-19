from app import db
import datetime


class Todo(db.Document):
    content = db.StringField(requiresd=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)
