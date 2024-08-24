from app.models.product_color import ProductColor
from marshmallow import fields, Schema, post_load

class ProductColorSchema(Schema):
    product_id = fields.Integer(required=True)
    color_id = fields.Integer(required=True)
    stock = fields.Integer(required=True)
    product = fields.Nested("ProductSchema", dump_only=True)
    #color = fields.Nested("ColorSchema", dump_only=True)

    @post_load
    def make_product_color(self, data, **kwargs):
        return ProductColor(**data)
