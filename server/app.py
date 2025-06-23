from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models.__init__ import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
app.json.compact = False

migrate = Migrate(app, db)
jwt = JWTManager()
db.init_app(app)

@app.route('/')
def index():
    return f'<h1>Welcome to my header right now</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)