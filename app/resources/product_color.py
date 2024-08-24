from flask import Blueprint, request
from app.mapping import ProductColorSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.product_color_service import ProductColorService

product_color = Blueprint('product_color', __name__)
product_color_schema = ProductColorSchema()
response_schema = ResponseSchema()
product_color_service = ProductColorService()

@product_color.route('/product_colors', methods=['GET'])
def index():
    return {"product_colors": product_color_schema.dump(product_color_service.all(), many=True)}, 200

@product_color.route('/product_colors/<int:product_id>/<int:color_id>', methods=['GET'])
def find(product_id: int, color_id: int):
    response_builder = ResponseBuilder()
    response_builder.add_message("Color del producto encontrado").add_status_code(100).add_data(product_color_schema.dump(product_color_service.find(product_id, color_id)))
    return response_schema.dump(response_builder.build()), 200

@product_color.route('/product_colors/add', methods=['POST'])
def post_product_color():
    product_color = product_color_schema.load(request.json)
    return {"product_color": product_color_schema.dump(product_color_service.save(product_color))}, 201

@product_color.route('/product_colors/<int:product_id>/<int:color_id>', methods=['PUT'])
def update_product_color(product_id: int, color_id: int):
    product_color = product_color_schema.load(request.json)
    response_builder = ResponseBuilder()
    response_builder.add_message("Color del producto actualizado").add_status_code(100).add_data(product_color_schema.dump(product_color_service.update(product_color, product_id, color_id)))
    return response_schema.dump(response_builder.build()), 200

@product_color.route('/product_colors/<int:product_id>/<int:color_id>', methods=['DELETE'])
def delete_product_color(product_id: int, color_id: int):
    product_color_service.delete(product_id, color_id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Color del producto borrado").add_status_code(100).add_data({'product_id': product_id, 'color_id': color_id})
    return response_schema.dump(response_builder.build()), 200
