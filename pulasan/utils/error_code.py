from enum import Enum


class ErrorCode(Enum):
    # 通用错误 (模块代码 10)
    PARAMETER_MISSING = 10100  # '参数缺失'
    PARAMETER_FORMAT_ERROR = 10101  # '参数格式错误'
    UNAUTHORIZED = 10102  # '未授权'
    FORBIDDEN = 10103  # '禁止访问'
    NOT_FOUND = 10104  # '未找到'
    METHOD_NOT_ALLOWED = 10105  # '方法不允许'
    REQUEST_TIMEOUT = 10106  # '请求超时'
    INVALID_REQUEST = 10107  # '请求无效'

    # 用户相关错误 (模块代码 20)
    USER_NOT_FOUND = 20200  # '用户不存在'
    INCORRECT_PASSWORD = 20201  # '密码错误'
    USER_ALREADY_EXISTS = 20202  # '用户已存在'
    INVALID_USER_STATUS = 20203  # '用户状态无效'

    # 数据库相关错误 (模块代码 30)
    DB_INSERT_FAILED = 30300  # '数据插入失败'
    DB_QUERY_FAILED = 30301  # '数据查询失败'
    DB_UPDATE_FAILED = 30302  # '数据更新失败'
    DB_DELETE_FAILED = 30303  # '数据删除失败'
    DB_CONNECTION_ERROR = 30304  # '数据库连接错误'

    # 外部服务错误 (模块代码 40)
    EXTERNAL_API_CALL_FAILED = 40400  # '第三方API调用失败'
    EXTERNAL_API_TIMEOUT = 40401  # '第三方API超时'
    EXTERNAL_API_MISSING_DATA = 40402  # '第三方API返回缺少data数据'
    EXTERNAL_API_ERROR = 40403  # '第三方API错误'

    # 序列化/反序列化错误 (模块代码 50)
    SERIALIZATION_FAILED = 50500  # '序列化失败'
    DESERIALIZATION_FAILED = 50501  # '反序列化失败'

    # 服务器异常错误 (模块代码 60)
    INTERNAL_SERVER_ERROR = 60600  # '服务器内部错误'
    SERVICE_UNAVAILABLE = 60601  # '服务不可用'
    GATEWAY_TIMEOUT = 60602  # '网关超时'
    INSUFFICIENT_STORAGE = 60603  # '存储空间不足'

    # 网络错误 (模块代码 70)
    NETWORK_ERROR = 70700  # '网络错误'
    DNS_RESOLUTION_FAILED = 70701  # 'DNS解析失败'
    CONNECTION_REFUSED = 70702  # '连接被拒绝'

    # 文件相关错误 (模块代码 80)
    FILE_NOT_FOUND = 80800  # '文件未找到'
    FILE_READ_ERROR = 80801  # '文件读取错误'
    FILE_WRITE_ERROR = 80802  # '文件写入错误'
    FILE_FORMAT_UNSUPPORTED = 80803  # '文件格式不支持'


if __name__ == '__main__':
    error_code = ErrorCode.PARAMETER_MISSING
    print(error_code.value)
