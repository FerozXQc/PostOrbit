import secrets
from decouple import config
import redis

redis_client=redis.Redis.from_url(config('REDIS_URL'),decode_responses=True)

def create_sessions(user_id:str):
    session_id = secrets.token_hex(20)
    redis_client.setex(f'session:{session_id}',config('EXPIRY'),user_id)
    return session_id

def get_user_id(session_id:str):
    return redis_client.get(f'session:{session_id}')

def delete_session(session_id:str):
    return redis_client.delete(f'session:{session_id}')