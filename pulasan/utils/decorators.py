from functools import wraps

from pulasan.configs import settings
from pulasan.utils.log_util import logger

app_env = settings.env


def log4p(func_name):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            if app_env == 'dev':
                log_func = getattr(logger, func_name, None)
                if callable(log_func):  # 对象是否可调用
                    log_func(*args, **kwargs)
            return await func(self, *args, **kwargs)
        return wrapper
    return decorator
