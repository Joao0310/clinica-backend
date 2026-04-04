from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
from datetime import datetime, timedelta

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)

def create_token(user):
    payload = {
        "user_id": str(user["_id"]),
        "email": user["email"],
        "exp": datetime.utcnow() + timedelta(hours=8)
    }

    token = jwt.encode(
        payload,
        os.getenv("JWT_SECRET_KEY", "secret"),
        algorithm="HS256"
    )

    return token