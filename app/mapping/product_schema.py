from app.models import Product
from .color_schema import ColorSchema
from marshmallow import validate, Schema, fields, post_load

class ProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=2, max=120))
    description = fields.String(required=True, validate=validate.Length(min=2, max=120))
    price = fields.String(required=True, validate=validate.Length(min=2, max=120))
    colors = fields.Nested(ColorSchema, many=True) 


    @post_load
    def make_producto(self, data, **kwargs):
        return Product(**data)
