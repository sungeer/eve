from quart import request

from pulasan.utils.tools import jsonify


class CorsMiddleware:
    """
    使用 allow_credentials 可以控制是否允许跨域请求发送凭证
    在开启凭证支持时，确保 Access-Control-Allow-Origin 明确指定允许的来源，不能使用通配符 *
    即 ['https://example.com', 'https://anotherdomain.com']
    """

    def __init__(self, allow_origins=None, allow_methods=None, allow_headers=None, allow_credentials=False):
        self.app = None
        self.allow_origins = allow_origins or ['*']
        self.allow_methods = allow_methods or ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
        self.allow_headers = allow_headers or ['Content-Type', 'Authorization']
        self.allow_credentials = allow_credentials

    def init_app(self, app):
        self.app = app
        self.register_handlers()
        return self

    def _set_cors_headers(self, response):
        origin = request.headers.get('Origin')
        if origin in self.allow_origins or '*' in self.allow_origins:
            response.headers['Access-Control-Allow-Origin'] = origin if '*' not in self.allow_origins else '*'
            response.headers['Access-Control-Allow-Methods'] = ', '.join(self.allow_methods)
            response.headers['Access-Control-Allow-Headers'] = ', '.join(self.allow_headers)
            if self.allow_credentials:
                response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    async def _before_request(self):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'CORS preflight'})
            response.status_code = 204
            return self._set_cors_headers(response)
        return None

    async def _after_request(self, response):
        return self._set_cors_headers(response)

    def register_handlers(self):
        self.app.before_request(self._before_request)
        self.app.after_request(self._after_request)
