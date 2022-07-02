from typing import Union

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from video.routers import user_router
from video.models.user_model import User
from config import settings

app = FastAPI(**settings.FastAPI_SETTINGS)

# 设置跨域传参
app.add_middleware(
    CORSMiddleware,
    **settings.CORS
)

# 加载路由
app.include_router(user_router.router)


@app.on_event("startup")
async def startup_event():
    # 在程序启动的时候，连接数据库
    register_tortoise(
        app,
        db_url=settings.db_url,
        modules={"models": ["video.models.user_model"]}
    )
    print('数据库连接成功')


@app.get('/')
async def index():
    users = await User.all()
    print(users)
    return {'message': 'Hello World'}


if __name__ == '__main__':
    # 直接启动
    uvicorn.run('video.main:app', host='127.0.0.1', port=8000, log_level='info')
