from deta import Base,Deta
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from models import UserSchema, UserLoginSchema, TokenValidateSchema
from jwt_module import encode_jwt, decode_jwt, validate_jwt
from decouple import config
import uuid

PROJECT_KEY= config("PROJECTKEY")
deta = Deta(PROJECT_KEY)
usersDB = deta.Base("users")

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

users = []
# users_from_db = usersDB.fetch()
# for user in users_from_db.items:
#     users.append(user)

{
  "first_name": "John",
  "last_name": "Doe",
  "user_name": "John",
  "email": "user@example.com",
  "password": "dummypassword2"
}

@app.post("/users/register")
def register_user(user: UserSchema = Body(default=None)):
    new_user = user.dict()
    print(new_user)
    user_id = str(uuid.uuid1())
    new_user["user_id"] = user_id
    # users.append(new_user)
    usersDB.insert(new_user, key=user_id)
    jwt = encode_jwt(user_id=user_id)
    return {"user_name":new_user["user_name"], "token":jwt}

def get_users():
    users_from_db = usersDB.fetch()
    for us in users_from_db.items:
        print(us)
        users.append(us)

def check_user(user:UserLoginSchema):
    for u in users:
        if (u["user_name"] == user.user_name or u["email"] == user.user_name) and u["password"] == user.password:
            return {"user_id":u["user_id"], "user_name":u["user_name"]}
    return None

@app.post("/users/login")
def login_user(user: UserLoginSchema = Body(default=None)):
    users_from_db = usersDB.fetch()
    for us in users_from_db.items:
        print(us)
        users.append(us)

    user_data = check_user(user)
    if user_data != None:
        jwt = encode_jwt(user_id=user_data["user_id"])
        return {"user_name":user_data.user_name, "token":jwt}
    else:
        return {"error":"invalid login details!"}

@app.post("/validate")
def validate_token(token: TokenValidateSchema  = Body(default=None) ):
    print(token)
    if validate_jwt(token.token) == True:
        return "valid"
    return "invalid"
    
@app.get("/users")
def get_users():
    return usersDB.fetch().items