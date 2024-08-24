from flask import Blueprint, request
from app.mapping import CategorySchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.category_service import CategoryService

category = Blueprint('category', __name__)
category_schema = CategorySchema()
response_schema = ResponseSchema()
category_service = CategoryService()

@category.route('/categories', methods=['GET'])
def index():
    return {"categories": category_schema.dump(category_service.all(), many=True)}, 200

@category.route('/categories/<int:id>', methods=['GET'])
def find(id: int):
    response_builder = ResponseBuilder()
    response_builder.add_message("Categoría encontrada").add_status_code(100).add_data(category_schema.dump(category_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

@category.route('/categories/add', methods=['POST'])
def post_category():
    category = category_schema.load(request.json)
    return {"category": category_schema.dump(category_service.save(category))}, 201

@category.route('/categories/<int:id>', methods=['PUT'])
def update_category(id: int):
    category = category_schema.load(request.json)
    response_builder = ResponseBuilder()
    response_builder.add_message("Categoría actualizada").add_status_code(100).add_data(category_schema.dump(category_service.update(category, id)))
    return response_schema.dump(response_builder.build()), 200

@category.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id: int):
    category_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Categoría borrada").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200
