import os


class BaseSettings:
    app_name = 'pulasan'

    # os.path.abspath 将相对路径转换为绝对路径
    # os.path.dirname 当前脚本所在目录
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

    jwt_algorithm = 'HS256'  # 加密算法
    access_token_expire_minutes = 1440  # token 有效期 1440 即 24h

    ai_url = 'https://ai-api.betteryeah.com'
