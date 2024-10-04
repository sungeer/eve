from quart import request

from pulasan.utils.tools import jsonify


class CorsMiddleware:
    def __init__(self, allow_origins=None, allow_methods=None, allow_headers=None, allow_credentials=False):
        self.app = None
        self.allow_origins = allow_origins or ['*']
        self.allow_methods = allow_methods or ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
        self.allow_headers = allow_headers or ['Content-Type', 'Authorization']
        self.allow_credentials = allow_credentials

    def init_app(self, app, _is_handlers_aout=True):
        self.app = app
        if _is_handlers_aout:
            self.register_handlers()
        return self

    async def _after_request(self, response):
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
            response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
            response.headers['Access-Control-Allow-Methods'] = ', '.join(self.allow_methods)
            response.headers['Access-Control-Allow-Headers'] = ', '.join(self.allow_headers)
            if self.allow_credentials:
                response.headers['Access-Control-Allow-Credentials'] = 'true'
            return response

    def register_handlers(self):
        self.app.after_request(self._after_request)
        self.app.before_request(self._before_request)
