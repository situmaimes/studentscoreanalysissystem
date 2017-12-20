#!/usr/bin/env python
import os
from app import create_app,db
from app.models import Student,Score
from prepare import processDB
from flask_script import Manager, Shell

app=create_app("development")
if not os.path.exists("/"+app.config["SQLALCHEMY_DATABASE_URI"].lstrip("sqlite:///")):
    appContext = app.app_context()
    appContext.push()
    processDB()
    appContext.pop()
manager=Manager(app)
def make_shell_context():
    return dict(app=app, db=db,Student=Student,Score=Score)
manager.add_command("shell", Shell(make_context=make_shell_context))
if __name__=="__main__":
    #app.run("0.0.0.0",port=5000,debug=True)
    manager.run()
