from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import uuid

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Validasi email dan password (placeholder)
    if email == 'test@example.com' and password == 'password':
        user_id = str(uuid.uuid4())  # Menghasilkan user ID acak untuk contoh
        name = 'Test User'
        identity = str(user_id)  # Pastikan userId adalah string
        token = create_access_token(identity=identity)  # Menggunakan userId sebagai subjek
        
        return jsonify(
            error=False,
            message="success",
            loginResult={
                "userId": user_id,
                "name": name,
                "token": token
            }
        )
    else:
        return jsonify(error=True, message="Invalid email or password"), 401

@auth_bp.route('/register/patient', methods=['POST'])
def register_patient():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    whatsapp_number = data.get('whatsapp_number')
    password = data.get('password')
    role = 'Patient'
    # Lakukan proses penyimpanan data (placeholder)
    return jsonify(message="Patient registered successfully", name=name, email=email, whatsapp_number=whatsapp_number, role=role)

@auth_bp.route('/register/coass', methods=['POST'])
def register_coass():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    whatsapp_number = data.get('whatsapp_number')
    password = data.get('password')
    university = data.get('university')
    semester = data.get('semester')
    student_id_number = data.get('student_id_number')
    hospital = data.get('hospital')
    role = 'Co Ass'
    # Lakukan proses penyimpanan data (placeholder)
    return jsonify(message="Co-Ass registered successfully", name=name, email=email, whatsapp_number=whatsapp_number, university=university, semester=semester, student_id_number=student_id_number, hospital=hospital, role=role)
