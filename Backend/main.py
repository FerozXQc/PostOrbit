from fastapi import FastAPI, Form, Cookie, Response, HTTPException, Request
from auth import router as auth_router
from sessions import create_sessions,get_user_id,delete_session
from decouple import config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config('SVELTE_URL')],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router,prefix='/auth')

@app.get("/")
def home():
    return "hello"
