from quart import Quart
from werkzeug.exceptions import HTTPException

from pulasan.configs import settings


def create_app():
    app = Quart(__name__)

    register_extensions(app)
    register_events(app)
    register_errors(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    from pulasan.utils import cors

    cors.init_app(app)


def register_events(app):
    from pulasan.utils.db_util import db

    @app.before_serving
    async def startup():
        await db.connect()

    @app.after_serving
    async def shutdown():
        await db.disconnect()

        from pulasan.utils import http_client
        await http_client.close_httpx()


def register_errors(app):
    from pulasan.utils.log_util import logger
    from pulasan.utils.tools import abort

    @app.errorhandler(HTTPException)
    async def http_exception_handler(error):
        logger.opt(exception=True).warning(error)
        return abort(error.code)

    @app.errorhandler(Exception)
    async def global_exception_handler(error):
        logger.exception(error)
        return abort(500)


def register_blueprints(app):
    from pulasan.urls import user_url, chat_url

    app.register_blueprint(chat_url.chat_url)
    app.register_blueprint(user_url.user_url, url_prefix='/user')


app = create_app()
