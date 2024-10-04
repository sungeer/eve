import traceback

from pulasan.models.base_model import BaseModel
from pulasan.utils import tools, common
from pulasan.utils.decorators import log4p


class LogModel(BaseModel):

    async def get_logs(self, page, per_page, start_date, end_date, level):
        sql_str = '''
            SELECT 
                ID, Level, Message, CreatedTime
            FROM 
                logs
            WHERE 
                1 = %s 
        '''
        where_values = [1, ]
        if end_date and start_date:
            where_str = ' AND CreatedTime BETWEEN %s AND %s '
            sql_str += where_str
            where_values.extend([start_date, end_date])
        else:
            where_str = ' AND CreatedTime BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 1 DAY) '
            sql_str += where_str
        if level:
            where_str = ' AND Level = %s '
            sql_str += where_str
            where_values.append(level)
        total_str = common.parse_count_str(sql_str, truncate=True)
        await self.conn()
        await self.execute(total_str, where_values)
        total = await self.cursor.fetchone()
        total = total['total']
        offset = (page - 1) * per_page
        limit_str = ' ORDER BY ID DESC LIMIT %s OFFSET %s '
        sql_str += limit_str
        where_values.extend([per_page, offset])
        await self.execute(sql_str, where_values)
        logs = await self.cursor.fetchall()
        await self.close()
        page_info = common.get_page_info(total, page, per_page)
        page_info.update({'data': logs})
        return page_info

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

    @log4p('debug')
    async def debug(self, message):  # 调试
        return await self.add_log('DEBUG', message)

    @log4p('info')
    async def info(self, message):
        return await self.add_log('INFO', message)

    @log4p('warning')
    async def warning(self, message):  # 警告 需要注意
        return await self.add_log('WARNING', message)

    @log4p('error')
    async def error(self, message, exc_info=None):  # 错误 需要立即处理
        if exc_info:
            tb_str = ''.join(traceback.format_exception(None, exc_info, exc_info.__traceback__))
            message = f'{message}\n{tb_str}'
        return await self.add_log('ERROR', message)

    @log4p('critical')
    async def critical(self, message):  # 严重错误 可能导致程序终止
        return await self.add_log('CRITICAL', message)

    @log4p('notset')
    async def notset(self, message):  # 未设置级别 用于初始化日志记录器
        return await self.add_log('NOTSET', message)

    @log4p('exception')
    async def exception(self, error):  # 用于捕获异常并记录堆栈信息
        tb_str = ''.join(traceback.format_exception(None, error, error.__traceback__))
        return await self.add_log('ERROR', tb_str)


if __name__ == '__main__':
    try:
        pass
    except Exception as exc:
        LogModel().error(f'websocket error occurred: {exc}', exc_info=exc)  # exc_info=True
