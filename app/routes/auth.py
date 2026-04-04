from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, login_user

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/registro", methods=["POST"])

def register():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "")
    email = data.get("email", "")
    password = data.get("password", "")

    response, status_code = register_user(name, email, password)
    return jsonify(response), status_code

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    email = data.get("email", "")
    password = data.get("password", "")

    response, status_code = login_user(email, password)
    return jsonify(response), status_code