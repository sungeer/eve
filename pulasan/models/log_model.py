import traceback

from pulasan.models.base_model import BaseModel
from pulasan.utils import tools


class LogModel(BaseModel):

    async def add_log(self, level, message):
        sql_str = '''
            INSERT INTO 
                logs 
                (Level, Message, CreatedTime) 
            VALUES 
                (%s, %s, %s)
        '''
        created_at = tools.current_time()
        await self.conn()
        await self.execute(sql_str, (level, message, created_at))
        await self.commit()
        lastrowid = self.cursor.lastrowid
        await self.close()
        return lastrowid

    async def debug(self, message):  # 调试
        return await self.add_log('DEBUG', message)

    async def info(self, message):
        return await self.add_log('INFO', message)

    async def warning(self, message):  # 警告 需要注意
        return await self.add_log('WARNING', message)

    async def error(self, message, exc_info=None):  # 错误 需要立即处理
        if exc_info:
            tb_str = ''.join(traceback.format_exception(None, exc_info, exc_info.__traceback__))
            message = f'{message}\n{tb_str}'
        return await self.add_log('ERROR', message)

    async def critical(self, message):  # 严重错误 可能导致程序终止
        return await self.add_log('CRITICAL', message)

    async def notset(self, message):  # 未设置级别 用于初始化日志记录器
        return await self.add_log('NOTSET', message)

    async def exception(self, error):  # 用于捕获异常并记录堆栈信息
        tb_str = ''.join(traceback.format_exception(None, error, error.__traceback__))
        return await self.add_log('ERROR', tb_str)


logger = LogModel()
