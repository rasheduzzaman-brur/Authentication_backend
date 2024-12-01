from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_session import Session
from app.config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager
# Initialize Flask app
app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config.from_object(Config)

# MongoDB connection
client = MongoClient(app.config["MONGO_URI"])
db = client[app.config["DATABASE_NAME"]]

# JWT initialization
jwt = JWTManager(app)

# Import routes (avoiding blueprints)
from app import routes