from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from sqlalchemy_serializer import SerializerMixin
from .config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)
jwt = JWTManager()

