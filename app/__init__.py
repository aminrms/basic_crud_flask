import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_smorest import Api



load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)


    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL" , default="sqlite:///payments.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["API_TITLE"] = "Payment API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)

    from app.routes.payment import blp as PaymentBlueprint
    api = Api(app)
    api.register_blueprint(PaymentBlueprint)

    return app