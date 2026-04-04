from flask_cors import CORS
from pymongo import MongoClient

cors = CORS()

def init_cors(app):
    cors.init_app(app)

def init_mongo(app):
    client = MongoClient(app.config["MONGO_URI"])
    db = client[app.config["MONGO_DB_NAME"]]

    app.extensions["mongo_client"] = client
    app.extensions["mongo_db"] = db
    app.extensions["users_collection"] = db["users"]
    
    return db

def get_db(app):
    return app.extensions.get("mongo_db")

def get_users_collection(app):
    return app.extensions.get("users_collection")