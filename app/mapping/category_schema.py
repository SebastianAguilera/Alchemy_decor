from app.models.category import Category
from marshmallow import fields, Schema, post_load

class CategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    products = fields.List(fields.Nested("ProductSchema", dump_only=True))  # Relación con Product

    @post_load
    def make_category(self, data, **kwargs):
        return Category(**data)
