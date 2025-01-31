import logging
from logging import getLogger

from quart.logging import default_handler

from viper.utils.log_util import logger


# 拦截标准库的 logging 记录器
class InterceptHandler(logging.Handler):

    def emit(self, record):
        # 获取对应的日志级别
        level = logger.level(record.levelname).name
        # 格式化日志内容
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        # 记录日志
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def register_logging(app):
    # 移除默认的 handler
    getLogger(app.name).removeHandler(default_handler)
    # 拦截 Quart 的日志记录器
    logging.getLogger(app.name).handlers = [InterceptHandler()]
