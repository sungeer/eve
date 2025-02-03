from quart_cors import cors


def init_app(app):
    cors(
        app,
        allow_origin='*',
        allow_methods='*',
        allow_headers='*',
        expose_headers='*',
        max_age=3600
    )
