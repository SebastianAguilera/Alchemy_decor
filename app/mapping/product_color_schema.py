"""
from app.models import ProductColor
from marshmallow import Schema, fields, post_load

class ProductColorSchema(Schema):
    product_id = fields.Integer(dump_only=True)
    color_id = fields.Integer(dump_only=True)

    @post_load
    def make_product_color(self, data, **kwargs):
        return ProductColor(**data)

"""