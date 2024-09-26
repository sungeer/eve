import os
import logging
from logging.handlers import RotatingFileHandler

from pulasan.configs import settings

app_env = settings.env
app_name = settings.app_name

logger = logging.getLogger(app_name)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def create_file_handler():
    basedir = settings.basedir
    log_dir = os.path.join(basedir, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'viper.log')
    file_handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=10, encoding='utf-8')
    return file_handler


# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

if app_env == 'dev':
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
else:
    logger.setLevel(logging.INFO)
    file_handler = create_file_handler()
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
