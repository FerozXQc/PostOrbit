from fastapi import APIRouter, Form, Cookie, Response, HTTPException, Request
from schemas import loginUser, registerUser
from database import db_createUser,db_loginUser,db_checkEmail
from sessions import create_sessions,get_user_id,delete_session
from decouple import config




router = APIRouter(tags=["auth"])

@router.post('/register')
def register(user:registerUser):
    if len(user.username)<8 or len(user.username)<8 or not user.username[0].isalpha():
        return f"minimum length of username and password:8. Username cant start with a special character."
    else:
        if db_checkEmail(user):
            return 'email already exists! try again w a different one.'
        result = db_createUser(user)
        return {'result':result}


@router.post('/login')
def login(user:loginUser,response:Response):
    result = db_loginUser(user)
    session_id = create_sessions(user.username)
    response.set_cookie(key='session_id', value=session_id, httponly=True)
    return {'message': 'login successful', 'session_id': session_id}


@router.post('/logout')
def logout(response:Response,request:Request):
    session_id = request.cookies.get('session_id')
    if session_id:
        delete_session(session_id)
        response.delete_cookie('session_id')
    return {'message':'logged out'}