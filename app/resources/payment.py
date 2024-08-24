from flask import Blueprint, request
from app.mapping import PaymentSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.payment_service import PaymentService

payment = Blueprint('payment', __name__)
payment_schema = PaymentSchema()
response_schema = ResponseSchema()
payment_service = PaymentService()

@payment.route('/payments', methods=['GET'])
def index():
    return {"payments": payment_schema.dump(payment_service.all(), many=True)}, 200

@payment.route('/payments/<int:id>', methods=['GET'])
def find(id: int):
    response_builder = ResponseBuilder()
    response_builder.add_message("Pago encontrado").add_status_code(100).add_data(payment_schema.dump(payment_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

@payment.route('/payments/add', methods=['POST'])
def post_payment():
    payment = payment_schema.load(request.json)
    return {"payment": payment_schema.dump(payment_service.save(payment))}, 201

@payment.route('/payments/<int:id>', methods=['PUT'])
def update_payment(id: int):
    payment = payment_schema.load(request.json)
    response_builder = ResponseBuilder()
    response_builder.add_message("Pago actualizado").add_status_code(100).add_data(payment_schema.dump(payment_service.update(payment, id)))
    return response_schema.dump(response_builder.build()), 200

@payment.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id: int):
    payment_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Pago borrado").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200
