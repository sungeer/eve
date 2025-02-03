from kimi.plus import cors
from kimi.plus.db import Database

db = Database()


def register_extensions(app):
    cors.init_app(app)
    db.init_app(app)
