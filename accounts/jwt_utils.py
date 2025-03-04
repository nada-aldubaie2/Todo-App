import django.utils
import jwt
from datetime import datetime, timedelta
from django.conf import settings


SECRET_KEY = settings.SECRET_KEY

def create_token(user_id, username):
    payload={
        'user_id': user_id,
        'username':username,
        'exp':datetime.utcnow() + timedelta(days=1),
        'iat':datetime.utcnow(),
    }
    
    token=jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        return 'Token expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'