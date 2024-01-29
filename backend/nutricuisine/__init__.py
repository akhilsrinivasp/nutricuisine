from flask import Flask
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from nutricuisine.config import LocalDevelopmentConfig
from nutricuisine.database import db, ma

from nutricuisine.api.auth import auth_blueprint
from nutricuisine.api.classifier.predict_api import predict_blueprint
from nutricuisine.api.repices.recommendation_api import recommendation_blueprint
from nutricuisine.api.consume import consume_blueprint
from nutricuisine.api.food import food_blueprint


def create_app(config_class=LocalDevelopmentConfig):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    ma.init_app(app)
    
    CORS(app, resources={r"*": {"origins": "*"}})
    JWTManager(app)
    
    # register blueprints
    
    with app.app_context():
        db.create_all() 
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(predict_blueprint)
        app.register_blueprint(recommendation_blueprint)
        app.register_blueprint(consume_blueprint)
        app.register_blueprint(food_blueprint)
        
    return app
