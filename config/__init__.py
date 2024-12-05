from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config.database import Config, firestore_client

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    JWTManager(app)

    with app.app_context():
        from routes import register_routes  # Gunakan impor relatif
        register_routes(app)

    return app
