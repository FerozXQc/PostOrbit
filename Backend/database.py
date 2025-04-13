import mysql.connector as mysql
from decouple import config
from contextlib import contextmanager
from passlib.context import CryptContext
from schemas import registerUser,loginUser,Taskschema
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
        cursor.execute("insert into users(username,email,password) values(%s,%s,%s);",(user.username,user.email,hashed,))
        db.commit()
    return f'{hashed}, user created sucessfully.'  #threw in hashed passwd for debugging

def db_checkEmail(user:registerUser):
    with openDB() as db:
        cursor = db.cursor()
        cursor.execute('SELECT 1 FROM users WHERE email = %s LIMIT 1',(user.email,))
        res = cursor.fetchone()
        if res:
            return res is not None

def db_fetchUser(user:loginUser):
    with openDB() as db:
        cursor = db.cursor()
        cursor.execute('select * from users where username=%s', (user.username,))
        User = cursor.fetchone()
        return User

def db_addTask(task:Taskschema, user_id:int):
    with openDB() as db:
        cursor = db.cursor()
        cursor.execute('insert into tasks(user_id,title,scheduled_time) values(%s,%s,%s,)',(user_id,task.title,task.scheduled_time))
        return "task added successfully."
    db.commit()

def db_editTaskName(task:Taskschema, new_task:str, user_id:int):
    with openDB() as db:
        cursor = db.cursor()
        cursor.execute("update tasks set task=%s where task_no=%s and user_id=%s;",(new_task,task.id,user_id,))
    db.commit()

def db_editTaskTime(task:Taskschema, new_time:str, user_id:int):
    with openDB() as db:
        cursor = db.cursor()
        cursor.execute("update tasks set scheduled_time=%s where task_no=%s and user_id=%s;",(new_time,task.id,user_id,))
    db.commit()

def db_deleteTask(task_no:int):
    with openDB() as db:
        cursor = db.cursor()
        cursor.execute("delete from tasks where task_no=%s",(task_no,))
    db.commit()

def db_getUserTasks(user_id:int):
    with openDB() as db:
        cursor = db.cursor()
        cursor.execute('select * from tasks where user_id=%s',(user_id,))

