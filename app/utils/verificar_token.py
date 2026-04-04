from flask import request, jsonify
import jwt
import os
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"message": "Token não fornecido"}), 401

        try:
            parts = auth_header.split(" ")
            if len(parts) != 2 or parts[0] != "Bearer":
                return jsonify({"message": "Formato do token inválido"}), 401

            token = parts[1]

            payload = jwt.decode(
                token,
                os.getenv("JWT_SECRET_KEY", "secret"),
                algorithms=["HS256"]
            )

            request.user = payload

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido"}), 401
        except Exception:
            return jsonify({"message": "Erro na autenticação"}), 401

        return f(*args, **kwargs)

    return decorator