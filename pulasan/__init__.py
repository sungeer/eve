from quart import Quart
from werkzeug.exceptions import HTTPException

from pulasan.configs import settings


def create_app():
    app = Quart('pulasan')

    register_events(app)
    register_middlewares(app)
    register_errors(app)
    register_blueprints(app)
    return app


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


def register_middlewares(app):
    from pulasan.middlewares import cors_middleware

    cors_middleware.init_app(app)


def register_errors(app):
    from pulasan.models.log_model import LogModel
    from pulasan.utils.tools import abort

    @app.errorhandler(HTTPException)
    async def http_exception_handler(error):
        # error_code = getattr(error, 'code', 500)
        # message = HTTP_STATUS_CODES.get(error_code, str(error))
        # error_code = error.code
        return abort(error.code)

    @app.errorhandler(Exception)
    async def global_exception_handler(error):
        await LogModel().exception(error)
        return abort(500)


def register_blueprints(app):
    from pulasan.urls import user_url, chat_url, admin_url

    app.register_blueprint(chat_url.chat_url)
    app.register_blueprint(user_url.user_url, url_prefix='/user')
    app.register_blueprint(admin_url.admin_url, url_prefix='/admin')


app = create_app()
