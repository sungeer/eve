from pulasan.configs.base_conf import BaseSettings


class ProdSettings(BaseSettings):
    env = 'prod'

    # mysql
    db_name = 'bebinca'
    db_port = 3306
    db_host = '127.0.0.1'
