from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from pymongo import MongoClient

from .routes.pacientes import pacientes_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    db = client.get_default_database()

    app.extensions["mongo_db"] = db

    app.register_blueprint(pacientes_bp, url_prefix="/pacientes")

    @app.get("/")
    def home():
        return {"mensagem": "API funcionando"}, 200

    return app