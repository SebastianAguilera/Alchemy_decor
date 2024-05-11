"""
from app.models import Color
from marshmallow import validate, Schema, fields, post_load

class ColorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=2, max=120))
    description = fields.String(required=True, validate=validate.Length(min=2, max=120))

    @post_load
    def make_color(self, data, **kwargs):
        return Color(**data)
"""



