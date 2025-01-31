from viper.core import cors


def register_extensions(app):
    cors.init_app(app)
