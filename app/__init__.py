import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{basedir}"
app.config["SECRET_KEY"] = b'\xed\xf4\x83\xac\x92\x948\x10\xed\x04r\x94\x90\x058\xec\xf5\x84\x8bV\xfe\xceb\xea'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app, prefix="/api/v1")
db = SQLAlchemy(app)
CORS(app)

from app.resources.auth import LoginRouter, RegisterRouter
api.add_resource(RegisterRouter, "/register")
api.add_resource(LoginRouter, "/login")

from app.resources.contacts import ContactRouter
api.add_resource(ContactRouter, "/contacts")
