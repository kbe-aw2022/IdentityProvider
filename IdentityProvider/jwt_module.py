import time
import jwt
import sys
from decouple import config

JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")

def encode_jwt(user_id:str):
    payload={
        "user_id": user_id
        # "exp": time.time() + 12000
    }
    token = jwt.encode(payload, JWT_SECRET,JWT_ALGORITHM)
    print(token)
    return token


def decode_jwt(token:str):
    try:
        decoded_token = jwt.decode(jwt=token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}

def validate_jwt(token:str):
    print(token)
    try:
        decoded_token = jwt.decode(jwt=token, key=JWT_SECRET, algorithms=['HS256', ])
        return True
    except:
        print(sys.exc_info())
        return False