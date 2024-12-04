from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import os

scan_bp = Blueprint('scan', __name__)

news_data = [
    {"id": 1, "title": "Dental Health News 1", "content": "Details about news 1"},
    {"id": 2, "title": "Dental Health News 2", "content": "Details about news 2"}
]

@scan_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_image():
    current_user = get_jwt_identity()  # Memastikan identitas JWT dapat diambil
    if 'image' not in request.files:
        return jsonify(message="No image uploaded"), 400
    image = request.files['image']
    filename = os.path.join('uploads', image.filename)

    # Buat direktori 'uploads' jika belum ada
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    image.save(filename)

    results = "AI analysis results for " + image.filename

    return jsonify(message="Image uploaded successfully", results=results, user=current_user)  # Tambahkan user untuk verifikasi

@scan_bp.route('/news', methods=['GET'])
@jwt_required()
def get_news():
    current_user = get_jwt_identity()  # Memastikan identitas JWT dapat diambil
    return jsonify(news=news_data, user=current_user)  # Tambahkan user untuk verifikasi

@scan_bp.route('/news/<int:id>', methods=['GET'])
@jwt_required()
def get_news_detail(id):
    current_user = get_jwt_identity()  # Memastikan identitas JWT dapat diambil
    news_item = next((item for item in news_data if item["id"] == id), None)
    if news_item is None:
        return jsonify(message="News not found"), 404
    return jsonify(news=news_item, user=current_user)  # Tambahkan user untuk verifikasi
