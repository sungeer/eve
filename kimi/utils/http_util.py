from quart import current_app
import httpx

config = current_app.config

limits = httpx.Limits(
    max_keepalive_connections=config.get_int_conf('HTTPX', 'POOL_SIZE_COMMON'),
    max_connections=config.get_int_conf('HTTPX', 'MAX_OVERFLOW_COMMON')
)

timeout = httpx.Timeout(
    connect=2.0,
    read=5.0,
    write=2.0,
    pool=2.0
)

httpx_common = httpx.AsyncClient(limits=limits, timeout=timeout)

# 流式
limits = httpx.Limits(
    max_keepalive_connections=config.get_int_conf('HTTPX', 'POOL_SIZE_STREAM'),
    max_connections=config.get_int_conf('HTTPX', 'MAX_OVERFLOW_STREAM')
)

timeout = httpx.Timeout(
    connect=3.0,  # 连接超时时间
    read=20.0,  # 流式 两个数据块之间的时间间隔
    write=3.0,  # 写入超时时间
    pool=2.0  # 从连接池中获取连接的超时时间
)

httpx_stream = httpx.AsyncClient(limits=limits, timeout=timeout)


async def close_httpx():
    await httpx_common.aclose()
    await httpx_stream.aclose()
