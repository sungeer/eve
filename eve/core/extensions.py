from eve.plus import cors
from eve.plus.db import Database

db = Database()


def register_extensions(app):
    cors.init_app(app)
    db.init_app(app)
