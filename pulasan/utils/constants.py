from pulasan.utils.error_enum import ErrorEnum

http_map = {
    400: 'Invalid request.',
    403: 'Access forbidden.',
    404: 'The requested URL was not found on the server.',
    405: 'The method is not allowed for the requested URL.'
}

error_map = {
    400: ErrorEnum.INVALID_REQUEST.value,
    403: ErrorEnum.FORBIDDEN.value,
    404: ErrorEnum.NOT_FOUND.value,
    405: ErrorEnum.METHOD_NOT_ALLOWED.value
}
