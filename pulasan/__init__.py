from quart import Quart
from werkzeug.exceptions import HTTPException

from pulasan.configs import settings
from pulasan.utils import cors, http_client
from pulasan.utils.db_util import db
from pulasan.utils.tools import abort, jsonify_exc
from pulasan.utils.log_util import logger
from pulasan.utils.errors import ValidationError
from pulasan.views import user_view, chat_view


def create_app():
    app = Quart(__name__)

    register_extensions(app)
    register_events(app)
    register_errors(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    cors.init_app(app)


def register_events(app):
    @app.before_serving
    async def startup():
        await db.connect()

    @app.after_serving
    async def shutdown():
        await db.disconnect()
        await http_client.close_httpx()


def register_errors(app):
    @app.errorhandler(ValidationError)
    async def validation_exception_handler(error):
        logger.opt(exception=True).info(error)
        return jsonify_exc(422)

    @app.errorhandler(HTTPException)
    async def http_exception_handler(error):
        logger.opt(exception=True).info(error)
        return jsonify_exc(error.code)  # jsonify_exc(error.code, error.description)

    @app.errorhandler(Exception)
    async def global_exception_handler(error):
        logger.exception(error)
        return jsonify_exc(500)


def register_blueprints(app):
    app.register_blueprint(chat_view.route)
    app.register_blueprint(user_view.route, url_prefix='/user')


app = create_app()
