from kimi.views import user_view, chat_view


def register_blueprints(app):
    app.register_blueprint(chat_view.route)
    app.register_blueprint(user_view.route, url_prefix='/user')
