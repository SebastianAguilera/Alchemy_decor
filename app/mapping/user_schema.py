"""
from app.models import User
from marshmallow import validate, Schema, fields, post_load

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(min=2, max=120))
    email = fields.String(required=True, validate=validate.Email())
    password = fields.String(load_only=True)
    userdata = fields.Nested("UserDataSchema", only=("id", "firstname", "lastname", "phone"))

    @post_load
    def make_usuario(self, data, **kwargs):
        return User(**data)
"""
