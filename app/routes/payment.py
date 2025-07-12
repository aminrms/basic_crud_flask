from flask_smorest import Blueprint,abort
from flask.views import MethodView
from app.models.payment import PaymentModel
from app.schemas.payment import PaymentSchema
from sqlalchemy.exc import SQLAlchemyError
from app import db


blp = Blueprint("Payment" ,"payments",url_prefix="/api/payments")


@blp.route("/")
class PaymentRecource(MethodView):
    @blp.response(200, PaymentSchema(many=True))
    def get(self):
        return PaymentModel.query.order_by(PaymentModel.created_at.desc()).all()

    @blp.arguments(PaymentSchema)
    @blp.response(201, PaymentSchema)
    def post(self, new_data:PaymentModel):
        try:
            db.session.add(new_data)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the item: {e}")

        return new_data

@blp.route("/<int:pk>")
class PaymentDetailsRecource(MethodView):

    @blp.response(200,PaymentSchema)
    def  get(self,id):
        return PaymentModel.query.get_or_404(id)
    
    @blp.arguments(PaymentSchema(partial=("status",)))
    @blp.response(200, PaymentSchema)
    def put(self, update_data, id):
        payment = PaymentModel.query.get_or_404(id)
        if "status" in update_data:
            payment.status = update_data["status"]
        db.session.commit()
        return payment