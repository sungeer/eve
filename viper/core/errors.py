from werkzeug.exceptions import HTTPException

from viper.utils.resp_util import jsonify_exc
from viper.utils.log_util import logger
from viper.utils.errors import ValidationError


def register_errors(app):
    @app.errorhandler(ValidationError)
    async def validation_exception_handler(error):
        logger.opt(exception=True).warning(error)
        return jsonify_exc(422)

    @app.errorhandler(HTTPException)
    async def http_exception_handler(error):
        logger.opt(exception=True).warning(error)
        return jsonify_exc(error.code)  # jsonify_exc(error.code, error.description)

    @app.errorhandler(Exception)
    async def global_exception_handler(error):
        logger.exception(error)
        return jsonify_exc(500)
