import mysql.connector as mysql
from decouple import config
from contextlib import contextmanager
from passlib.context import CryptContext
from schemas import registerUser,loginUser
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(password:str,hashed:str)->str:
    return pwd_context.verify(password,hashed)

@contextmanager
def openDB(
    host=config('DB_HOST'),
    user=config('DB_USER'),
    password=config('DB_PASSWD'),
    database=config('DB_NAME')
):
    db = mysql.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    try:
        yield db
    finally:
        db.close()



def db_createUser(user:registerUser):
    hashed = hash_password(user.password)
    with openDB() as db:
        cursor = db.cursor()
        query="insert into users(username,email,password) values(%s,%s,%s);"
        inputVal = [user.username,user.email,hashed,]
        cursor.execute(query,inputVal)
        db.commit()
    return f'{hashed}, user created sucessfully.'

def db_checkEmail(user:registerUser):
    with openDB() as db:
        cursor = db.cursor()
        query='SELECT 1 FROM users WHERE email = %s LIMIT 1'
        inputVal = [user.email,]
        cursor.execute(query,inputVal)
        res = cursor.fetchone()
        if res:
            return res is not None

def db_loginUser(user:loginUser):
    with openDB() as db:
        cursor = db.cursor()
        query='select * from users where username=%s'
        inputVal = [user.username,]
        cursor.execute(query,inputVal)
        User = cursor.fetchone()
        hashed = User[3]
    if not User:
        return "user not found!"
    
    isverified=verify_password(user.password,hashed)

    if not isverified:
        return "invalid password. Please try again."
    else:
        return "login successful!"


