# -*- coding:utf-8 -*-
from flask.ext.script import Manager, Server
from app import app
from app import models


manager = Manager(app)

@manager.command
def save_todo():
    todo = models.Todo(content="My first todo")
    todo.save()

manager.add_command("runserver",
                    Server(host='127.0.0.1', port=5000, use_debugger=True))


if __name__ == "__main__":
    manager.run()

