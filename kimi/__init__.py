from quart import Quart

from kimi.core.settings import CONF
from kimi.core.logging import register_logging
from kimi.core.extensions import register_extensions
from kimi.core.events import register_events
from kimi.core.errors import register_errors
from kimi.core.blueprints import register_blueprints


def create_app():
    app = Quart(__name__)  # noqa
    app.config = CONF

    register_logging(app)
    register_extensions(app)
    register_events(app)
    register_errors(app)
    register_blueprints(app)
    return app


app = create_app()
