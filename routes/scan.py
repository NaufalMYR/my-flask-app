from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import os

scan_bp = Blueprint('scan', __name__)

@scan_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_image():
    if 'image' not in request.files:
        return jsonify(message="No image uploaded"), 400
    image = request.files['image']
    filename = os.path.join('uploads', image.filename)

    # Buat direktori 'uploads' jika belum ada
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    image.save(filename)

    results = "AI analysis results for " + image.filename

    return jsonify(message="Image uploaded successfully", results=results)

@scan_bp.route('/news', methods=['GET'])
@jwt_required()
def get_news():
    # Placeholder for fetching news articles
    news = [
        {"id": 1, "title": "Dental Health News 1"},
        {"id": 2, "title": "Dental Health News 2"}
    ]
    return jsonify(news=news)

@scan_bp.route('/news/<int:id>', methods=['GET'])
@jwt_required()
def get_news_detail(id):
    # Placeholder for fetching detailed news
    news = {"title": f"Dental Health News {id}", "content": f"Details about news {id}"}
    return jsonify(news=news)
