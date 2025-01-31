from viper.utils import http_util
from viper.utils.db_util import db


def register_events(app):
    @app.before_serving
    async def startup():
        await db.connect()

    @app.after_serving
    async def shutdown():
        await db.disconnect()
        await http_util.close_httpx()
