from pydantic.main import BaseModel
from typing import Union


class UserItem(BaseModel):
    # 验证用户注册数据
    username: str
    first_name: str
    last_name: str
