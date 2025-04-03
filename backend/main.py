# import os
# import mysql.connector as mysql
# from dotenv import load_dotenv

from fastapi import FastAPI
from model import PostSchema
# load_dotenv()

app = FastAPI(title="PostOrbit")

# db_host = os.getenv("DB_HOST")
# db_user = os.getenv("DB_USER")
# db_password = os.getenv("DB_PASSWORD")
# db_name = os.getenv("DB_NAME")

Posts = [
    {
        "id":1,
        "name":"feroz",
        "desc":"k3tamine super CEO"
    },
    {
        "id":2,
        "name":"taha",
        "desc":"deactivated"
    }
]

@app.get("/")
def greet():
    return "hi"

@app.get("/posts")
def posts():
    return {"posts": Posts}

@app.get("/posts/{id}")
def post(id:int):
    if id>len(Posts):
        return "not found"
    for i in Posts: 
        if id == i["id"]:
            return i
        
@app.post("/addpost")
def addpost(post:PostSchema):
    post.id = len(Posts) + 1
    Posts.append(post.dict())
    return f"{post} added successfully"