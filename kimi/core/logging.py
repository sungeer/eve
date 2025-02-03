import logging

from kimi.plus.logging import logger


# 将 Loguru 配置为全局的日志处理器
class InterceptHandler(logging.Handler):

    def emit(self, record):
        # 获取对应的 Loguru 日志级别
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 查找在 Loguru 中与记录的日志级别相对应的级别
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


# 替换默认处理器
def register_logging(app):
    # 移除默认处理器
    app.logger.handlers.clear()
    app.logger.setLevel(logging.NOTSET)  # 确保所有日志都会被传递给 Loguru

    # 添加自定义处理器
    app.logger.handlers.append(InterceptHandler())
    logger.info(f'Replaced default logger for app {app.name}')
