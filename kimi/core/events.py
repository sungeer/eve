from kimi.utils import http_util


def register_events(app):
    @app.before_serving
    async def startup():
        pass

    @app.after_serving
    async def shutdown():
        await http_util.close_httpx()
