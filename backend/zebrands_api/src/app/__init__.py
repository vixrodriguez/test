from flask import Flask
# from flask_jwt_extended import JWTManager
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5433/zebrands"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['JWT_TOKEN_LOCATION'] = ['cookies', 'headers']

# SQL Alchemy
db = SQLAlchemy(app)

# JWT
from .jwt import autenticate, identity
jwt = JWT(app=app,
          authentication_handler=autenticate,
          identity_handler=identity)




