from decouple import config
from fastapi import FastAPI, Form, Cookie, Response, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from schemas import UserLogin
from sessions import create_sessions,get_user_id,delete_session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config('SVELTE_URL')],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = [{
'name':'feroz',
'password':'123'},
]

@app.post('/login')
def login(response:Response,user:UserLogin):
       for u in users:
        if u['name'] == user.name and u['password'] == user.password:
            session_id = create_sessions(user.name)
            response.set_cookie(key='session_id', value=session_id, httponly=True)
            return {'message': 'login successful', 'session_id': session_id}

@app.get('/me')
def me(session_id:str = Cookie(None)):
    if not session_id:
        raise HTTPException(status_code=403,detail='login expired/unauthorized')
    user_id = get_user_id(session_id)
    if user_id:
        return {'user':user_id}
    raise HTTPException(status_code=403,detail='login expired/unauthorized')

@app.post('/logout')
def logout(response:Response,request:Request):
    session_id = request.cookies.get('session_id')
    if session_id:
        delete_session(session_id)
        response.delete_cookie('session_id')
    return {'message':'logged out'}