from fastapi import FastAPI, Request, Response, Depends,Form, HTTPException, Cookie
from fastapi.responses import JSONResponse
from schemas import User
from fastapi.middleware.cors import CORSMiddleware
from sessions import create_session,get_user_id,delete_session
from decouple import config

app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = {'feroz':'123'}

@app.post('/login')
def login(response:Response,name:str=Form(...),password:str=Form(...)):
    if name in users and users[name] == password:
        session_id=create_session(name)
        response.set_cookie(key='session_id',value=session_id,httponly=True)
        return {'message':'login successful'}
    else:
        raise HTTPException(status_code:401,detail='invalid creds.')

@app.get('/me')
def me(session_id:str = Cookie(None)):
    if not session_id:
        raise HTTPException(status_code:403,detail='unauthorized')
    user_id = get_user_id(session_id)
    if user_id:
        return {'uid':user_id}
    raise HTTPException(status_code:403,detail='unauthorized')

@app.post('/logout')
def logout(response:Response,session_id:str = Cookie(None)):
    delete_session(session_id)
    response.delete_cookie('session_id')
    return {'message':'logged out successfully'}
