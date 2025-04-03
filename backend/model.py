from pydantic import BaseModel

class PostSchema(BaseModel):
    id:int
    post:str
    desc:str
