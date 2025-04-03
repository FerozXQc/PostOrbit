# import os
# import mysql.connector as mysql
# from dotenv import load_dotenv

from fastapi import FastAPI,Body, Depends
from model import PostSchema,UserSchema,UserLoginSchema
from jwt_handler import signJWT
from jwt_bearer import jwtBearer
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

@app.get("/",tags=["greet"])
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
        
@app.post("/addpost", dependencies=[Depends(jwtBearer())])
def addpost(post:PostSchema):
     post.id = len(Posts) + 1
     Posts.append(post.dict())
     return f"{post} added successfully"

users=[]

@app.post("/register")
def Register(schema:UserSchema =Body()):
    users.append(schema)
    return f"{schema.name} added successfully."

def check_user(schema:UserLoginSchema =Body()):
    for user in users:
        if user.email == schema.email and user.password == schema.password:
            return True
        else:
            return False

@app.post("/login", tags=["user"])
def user_login(user:UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error":"inavlid creds."
        }