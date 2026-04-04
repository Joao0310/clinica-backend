from flask import Flask
from dotenv import load_dotenv

from app.utils.extensions import init_mongo, init_cors
from .routes.pacientes import pacientes_bp
from .routes.auth import auth_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    init_cors(app)
    init_mongo(app)

    app.register_blueprint(pacientes_bp, url_prefix="/pacientes")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.get("/")
    def home():
        return {"mensagem": "API funcionando"}, 200

    return app