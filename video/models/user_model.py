from datetime import datetime
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=32, allow_null=False, allow_blank=False)
    first_name = fields.CharField(max_length=32, allow_null=False, allow_blank=False)
    last_name = fields.CharField(max_length=32, allow_null=False, allow_blank=False)
    last_login = fields.DatetimeField(allow_null=False, default=datetime.now())
    create_time = fields.DatetimeField(allow_null=False, default=datetime.now())
    update_time = fields.DatetimeField(allow_null=False, default=datetime.now())

    def __str__(self):
        return self.username

    class Meta:
        table = 'user'


User_orm = pydantic_model_creator(User, name="User")
User_in_orm = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
