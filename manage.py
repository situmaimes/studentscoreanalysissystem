#!/usr/bin/env python
import os
from flask_script import Manager, Shell
from app import create_app, db
from app.models import Student, Score
from app.prepare import processDB

app=create_app("testing")

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
    app.run("0.0.0.0",port=5000,debug=True)
    #manager.run()
