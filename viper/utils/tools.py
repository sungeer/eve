import hashlib
import uuid
from datetime import datetime


def generate_uuid():
    random_uuid = str(uuid.uuid4())
    md5 = hashlib.md5()
    md5.update(random_uuid.encode('utf-8'))
    return md5.hexdigest().lower()


def current_time():
    return datetime.now()
