import os
import asyncio

DATABASE = 'video'
USER = 'root'
PASSWORD = '1277431229'
PORT = 3306
HOST = '127.0.0.1'
MYSQL_URL = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4'


class Settings:
    FastAPI_SETTINGS = dict(
        title="测试",
        description="描述",  # 描述
        version="0.0.1",  # 版本号
    )
    sem = asyncio.Semaphore(30)  # 控制项目中 异步请求其他网址时的并发量
    retry = 30  # 网络访重试次数
    # 数据库 配置
    DB = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": 'root',
        "password": '1277431229',
        "database": 'video',
        "charset": "utf8mb4"
    }
    db_url: str = "mysql://{user}:{password}@{host}:{port}/{database}?charset={charset}".format(**DB)
    CORS = dict(
        allow_origins=['*'],  # 设置允许的origins来源
        allow_credentials=True,
        allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
        allow_headers=["*"])  # 允许跨域的headers，可以用来鉴别来源等作用。

    # 程序配置
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(BASE_DIR, 'logs')
    if not os.path.exists(log_path):
        os.makedirs(log_path)


settings = Settings()
