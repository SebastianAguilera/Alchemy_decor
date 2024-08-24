from app.models.payment import Payment
from marshmallow import fields, Schema, post_load

class PaymentSchema(Schema):
    id = fields.Integer(dump_only=True)
    amount = fields.Float(required=True)
    status = fields.String(required=True)
    payment_method = fields.String(required=True)
    payment_date = fields.String(required=True)
    transaction_id = fields.Integer(required=True)
    #order = fields.Nested("OrderSchema", dump_only=True)

    @post_load
    def make_payment(self, data, **kwargs):
        return Payment(**data)
