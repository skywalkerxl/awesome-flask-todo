from app import app
import flask
from flask import render_template
from app import models

@app.route("/index")
def index():
    todos = models.Todo.objects.all()
    return render_template("index.html", todos = todos)


@app.route("/add", method=["POST",])
def add():
    content = flask.request.form.get("content");
    todo = models.Todo(content = content)
    todo.save()
    todos = flask.Todo.objects.all()
    return render_template("index.html", todos=todos)