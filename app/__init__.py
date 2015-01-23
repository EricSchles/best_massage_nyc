from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

production = False
if 'ON_HEROKU' in os.environ:
        production = True

if production:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
        db = SQLAlchemy(app)

else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///foo.db"
        db = SQLAlchemy(app)
#http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku

import models, views


