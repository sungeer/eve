from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import default_exceptions

from kimi.utils.json_util import JsonExtendResponse


class BaseResponse:

    def __init__(self):
        self.status = True
        self.error_code = None
        self.message = None
        self.data = None

    def to_dict(self):
        resp_dict = {
            'status': self.status,
            'error_code': self.error_code,
            'message': self.message,
            'data': self.data
        }
        return resp_dict


def jsonify(*args, **kwargs):
    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:
        content = args[0]
    else:
        content = args or kwargs
    response = BaseResponse()
    response.data = content
    response = response.to_dict()
    return JsonExtendResponse(response)


def jsonify_exc(error_code, message=None):
    if not message:
        message = HTTP_STATUS_CODES.get(error_code)
    response = BaseResponse()
    response.status = False
    response.error_code = error_code
    response.message = message
    response = response.to_dict()
    return JsonExtendResponse(response)


def abort(error_code, message=None):
    exception_type = default_exceptions.get(error_code)  # NotFound
    raise exception_type(description=message)
