from flask_cors import CORS
from pymongo import MongoClient

cors = CORS()


def init_mongo(app):
    client = MongoClient(app.config["MONGO_URI"])
    db = client[app.config["MONGO_DB_NAME"]]
    app.extensions["mongo_db"] = db
    return db