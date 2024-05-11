"""
from app.models import UserData
from marshmallow import validate, Schema, fields, post_load

class UserDataSchema(Schema):
    id = fields.Integer(dump_only=True)
    firstname = fields.String(required=True, validate=validate.Length(min=2, max=120))
    lastname = fields.String(required=True, validate=validate.Length(min=2, max=120))
    phone = fields.String(required=True, validate=validate.Length(min=7, max=15))



    @post_load
    def make_usuario(self, data, **kwargs):
        return UserData(**data)
"""