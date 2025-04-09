from pydantic import BaseModel

class UserLogin(BaseModel):
    name:str
    password:str

class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True  
