from quart import Quart

from viper.core.settings import CONF
from viper.core.extensions import register_extensions
from viper.core.events import register_events
from viper.core.errors import register_errors
from viper.core.blueprints import register_blueprints


def create_app():
    app = Quart(__name__)  # noqa
    app.config = CONF

    register_extensions(app)
    register_events(app)
    register_errors(app)
    register_blueprints(app)
    return app


app = create_app()
