from quart import Quart

from pulasan.configs import settings


def create_app():
    app = Quart('pulasan')

    register_blueprints(app)
    register_errors(app)
    return app


def register_blueprints(app):
    from pulasan.urls import user_url, chat_url

    app.register_blueprint(chat_url.chat_url)
    app.register_blueprint(user_url.user_url, url_prefix='/user')


def register_errors(app):
    from pulasan.utils.log_util import logger
    from pulasan.utils.tools import abort

    @app.errorhandler(400)
    def bad_request(e):
        return abort(10107, 'Invalid request.')

    @app.errorhandler(403)
    def bad_request(e):
        return abort(10103, 'Access forbidden.')

    @app.errorhandler(404)
    def page_not_found(e):
        return abort(10104, 'The requested URL was not found on the server.')

    @app.errorhandler(405)
    def page_not_found(e):
        return abort(10105, 'The method is not allowed for the requested URL.')

    @app.errorhandler(500)
    def internal_server_error(e):
        return abort(60600, 'An internal server error occurred.')


app = create_app()
