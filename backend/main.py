import os
import mysql.connector as mysql
from dotenv import load_dotenv
from fastapi import FastAPI
load_dotenv()
app = FastAPI(title="PostOrbit")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

if(db_name):
    print("database exists")
else:
    print("database doesnt exists")