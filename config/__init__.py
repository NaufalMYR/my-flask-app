from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Tambahkan konfigurasi CORS
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    JWTManager(app)

    with app.app_context():
        from routes import register_routes  # Gunakan impor relatif
        register_routes(app)

        db.create_all()

    return app
