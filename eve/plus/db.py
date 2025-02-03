import MySQLdb
from MySQLdb.cursors import DictCursor
from dbutils.pooled_db import PooledDB


class Database:

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.init_pool(app.config)
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['database'] = self

    def init_pool(self, config):
        self.db_pool = PooledDB(  # noqa
            creator=MySQLdb,
            maxcached=5,
            host=config.get_conf('DATABASE', 'HOST'),
            port=config.get_int_conf('DATABASE', 'PORT'),
            db=config.get_conf('DATABASE', 'NAME'),
            user=config.get_conf('DATABASE', 'USER'),
            passwd=config.get_sec_conf('DATABASE', 'PASSWD'),
            charset='utf8mb4',
            cursorclass=DictCursor
        )
