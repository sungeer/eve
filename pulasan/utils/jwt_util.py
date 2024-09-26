from datetime import datetime, timedelta

import bcrypt  # python -m pip install bcrypt
import jwt  # python -m pip install pyjwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from pulasan.configs import settings
from pulasan.utils.log_util import logger


def set_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def validate_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def generate_token(data: dict):
    token_data = data.copy()  # data = {'id': 3}
    expiration_delta = timedelta(minutes=settings.access_token_expire_minutes)
    expiration_time = datetime.now() + expiration_delta
    token_data.update({'exp': expiration_time.timestamp()})
    encoded_token = jwt.encode(token_data, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_token


def extract_uid(token: str):
    secret_key = settings.jwt_secret_key
    jwt_algorithm = settings.jwt_algorithm
    decoded_payload = jwt.decode(token, secret_key, algorithms=[jwt_algorithm])
    user_id = decoded_payload.get('id')
    return user_id


def verify_token(request):
    authorization_header = request.headers.get('Authorization')
    if authorization_header and authorization_header.startswith('Bearer '):
        jwt_token = authorization_header[len('Bearer '):]
        if not jwt_token:
            return None, 'token is missing'
    else:
        return None, 'Authorization header is missing or does not contain a Bearer token'
    try:
        user_id = extract_uid(jwt_token)
    except (ExpiredSignatureError,):
        return None, 'token has expired'
    except (InvalidTokenError,):
        return None, 'invalid token'
    except Exception as e:
        logger.error(f'token verification error: {str(e)}')
        return None, 'token verification error'
    if not user_id:
        return None, 'user does not exist'
    return user_id, None
