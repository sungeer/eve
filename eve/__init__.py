from quart import Quart

from eve.core.settings import CONF
from eve.core.logging import register_logging
from eve.core.extensions import register_extensions
from eve.core.events import register_events
from eve.core.errors import register_errors
from eve.core.blueprints import register_blueprints


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
