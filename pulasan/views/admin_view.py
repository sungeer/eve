from quart import request

from pulasan.models.log_model import LogModel
from pulasan.utils.tools import jsonify, abort
from pulasan.utils import jwt_util


async def get_logs():
    # /admin/get-logs?level=error&page=1&per_page=200&start_date=2024-09-29&end_date=2024-09-30
    query_params = request.args
    page = int(query_params.get('page', 1))
    per_page = int(query_params.get('per_page', 200))
    start_date = query_params.get('start_date')
    end_date = query_params.get('end_date')
    level = query_params.get('level')
    if end_date and start_date:
        start_date += ' 00:00:00'
        end_date += ' 23:59:59'
    logs = await LogModel().get_logs(page, per_page, start_date, end_date, level)
    return jsonify(logs)
