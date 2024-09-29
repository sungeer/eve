import os
import logging
from logging.handlers import RotatingFileHandler, QueueHandler, QueueListener
from queue import Queue
import time

from pulasan.configs import settings

app_env = settings.env
app_name = settings.app_name

logger = logging.getLogger(app_name)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def create_file_handler():
    basedir = settings.basedir
    log_dir = os.path.join(basedir, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'pulasan.log')
    file_handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=10, encoding='utf-8')
    return file_handler


# 创建日志队列
log_queue = Queue(-1)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 创建 QueueHandler
queue_handler = QueueHandler(log_queue)
logger.addHandler(queue_handler)

if app_env == 'dev':
    logger.setLevel(logging.DEBUG)
    queue_listener = QueueListener(log_queue, console_handler)
else:
    logger.setLevel(logging.INFO)
    file_handler = create_file_handler()
    file_handler.setFormatter(formatter)
    queue_listener = QueueListener(log_queue, file_handler, console_handler)

# 启动 QueueListener
queue_listener.start()


def stop_logger():
    while not log_queue.empty():
        time.sleep(0.1)
    queue_listener.stop()
