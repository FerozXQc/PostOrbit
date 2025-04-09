from pydantic import BaseModel


class User(BaseModel):
    name:str
    password:str
    class Config:
        user = {
            'name':"pasha",
            'password':"123"
        }
