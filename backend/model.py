from pydantic import BaseModel,Field,EmailStr

class PostSchema(BaseModel):
    id:int
    post:str
    desc:str

class UserSchema(BaseModel):
    name:str = Field(default=None)
    email:EmailStr = Field(default=None)
    password:str = Field(default=None)
    class Config:
        schema = {
            "demo":{
                "name":"some name.",
                "email":"xyz@gmail.com",
                "password":"123"
            }
        }

class UserLoginSchema(BaseModel):
    email:EmailStr = Field(default=None)
    password:str = Field(default=None)
    class Config:
        schema = {
            "demo":{
                "email":"xyz@gmail.com",
                "password":"123"
            }
        }
