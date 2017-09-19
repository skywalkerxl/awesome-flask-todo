from app import app
from flask import render_template
from app import models

@app.route("/index")
def index():
    todos = models.Todo.objects.all()
    return render_template("index.html", todos = todos)
