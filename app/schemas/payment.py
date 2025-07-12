from app import ma
from marshmallow import fields
from app.models.payment import PaymentModel



class PaymentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PaymentModel
        load_instance  = True

        
    id = ma.auto_field(dump_only=True)
    amount = ma.auto_field(required=True)
    currency = ma.auto_field()
    status = ma.auto_field(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    
payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)