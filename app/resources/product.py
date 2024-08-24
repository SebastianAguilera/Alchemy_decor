from flask import Blueprint, request
from app.mapping import ProductSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.product_service import ProductService

product = Blueprint('product', __name__)
product_schema = ProductSchema()
response_schema = ResponseSchema()
product_service = ProductService()

@product.route('/products', methods=['GET'])
def index():
    return {"products": product_schema.dump(product_service.all(), many=True)}, 200

@product.route('/products/<int:id>', methods=['GET'])
def find(id: int):
    response_builder = ResponseBuilder()
    response_builder.add_message("Producto encontrado").add_status_code(100).add_data(product_schema.dump(product_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

@product.route('/products/add', methods=['POST'])
def post_product():
    product = product_schema.load(request.json)
    return {"product": product_schema.dump(product_service.save(product))}, 201

@product.route('/products/<int:id>', methods=['PUT'])
def update_product(id: int):
    product = product_schema.load(request.json)
    response_builder = ResponseBuilder()
    response_builder.add_message("Producto actualizado").add_status_code(100).add_data(product_schema.dump(product_service.update(product, id)))
    return response_schema.dump(response_builder.build()), 200

@product.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id: int):
    product_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Producto borrado").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200
