from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


app = Flask("__main__")
app.config['SECRET_KEY'] = os.environ["LANGTRAINER_SECRET_KEY"]
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["LANGTRAINER_DB_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from langtrainer import routes

