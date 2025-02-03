import json
from datetime import datetime, date
from decimal import Decimal

from quart import Response


def dict_to_json(data):
    return json.dumps(data, cls=JsonExtendEncoder, ensure_ascii=False)


def dict_to_json_stream(data):
    return json.dumps(data, cls=JsonExtendEncoder, ensure_ascii=False).encode('utf-8')


class JsonExtendEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (tuple, list, datetime)):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, bytes):
            return obj.decode('utf-8')
        return super().default(obj)


class JsonExtendResponse(Response):

    def __init__(self, response, **kwargs):
        json_response = dict_to_json_stream(response)
        super().__init__(json_response, mimetype='application/json', **kwargs)
