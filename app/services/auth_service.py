from flask import current_app
from datetime import datetime
from app.utils.seguranca import hash_password, verify_password, create_token


def register_user(name, email, password):
    users_collection = current_app.extensions["users_collection"]

    if not name or not email or not password:
        return {"message": "Preencha nome, email e senha"}, 400

    email = email.strip().lower()

    existing_user = users_collection.find_one({"email": email})
    if existing_user:
        return {"message": "Email já cadastrado"}, 400

    user = {
        "name": name.strip(),
        "email": email,
        "password": hash_password(password),
        "created_at": datetime.utcnow()
    }

    result = users_collection.insert_one(user)

    return {
        "message": "Usuário cadastrado com sucesso",
        "user_id": str(result.inserted_id)
    }, 201


def login_user(email, password):
    users_collection = current_app.extensions["users_collection"]

    if not email or not password:
        return {"message": "Preencha email e senha"}, 400

    email = email.strip().lower()

    user = users_collection.find_one({"email": email})

    if not user:
        return {"message": "Credenciais inválidas"}, 401

    if not verify_password(password, user["password"]):
        return {"message": "Credenciais inválidas"}, 401

    token = create_token(user)

    if isinstance(token, bytes):
        token = token.decode("utf-8")

    return {
        "message": "Login realizado com sucesso",
        "token": token,
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        }
    }, 200