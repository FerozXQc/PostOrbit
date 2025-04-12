from pydantic import BaseModel

class loginUser(BaseModel):
    username:str
    password:str

class registerUser(BaseModel):
    id:int
    username:str
    email:str
    password:str

class profileUser(BaseModel):
    id:int
    username:str
    email:str
    password:str