from app.models.product import Product
from marshmallow import fields, Schema, post_load

class ProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True)
    category_id = fields.Integer(required=True)
    category = fields.Nested("CategorySchema", dump_only=True)  
    color_products = fields.List(fields.Nested("ProductColorSchema", dump_only=True))  
    #order_products = fields.List(fields.Nested("OrderProductSchema", dump_only=True)) 

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)