from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    first_name:str = Field(default=None)
    last_name:str = Field(default=None)
    user_name:str = Field(default=None)
    email:EmailStr = Field(default=None)
    password:str = Field(default=None)
    class Config:
        schema = {
            "demo":{
                "first_name":"first name",
                "last_name":"last name",
                "user_name":"user_name",
                "email":"email@mail.com",
                "password":"123"
            }
        }

class UserLoginSchema(BaseModel):
    user_name:str = Field(default=None)
    email:EmailStr = Field(default=None)
    password:str = Field(default=None)
    class Config:
        schema = {
            "demo":{
                "user_name":"user_name",
                "email":"email@mail.com",
                "password":"123"
            }
        }

class TokenValidateSchema(BaseModel):
    token:str = Field(default=None)
    class Config:
        schema = {
            "demo":{
                "token":"string"
            }
        }