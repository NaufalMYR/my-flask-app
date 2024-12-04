from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import uuid

auth_bp = Blueprint('auth', __name__)

users = []  # Simulasi penyimpanan data pengguna

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Cari pengguna berdasarkan email dan password
    user = next((user for user in users if user['email'] == email and user['password'] == password), None)
    
    if user:
        user_id = user['user_id']
        name = user['name']
        role = user['role']
        token = create_access_token(identity=str(user_id))  # Gunakan user_id sebagai string
        
        return jsonify(
            error=False,
            message="success",
            loginResult={
                "userId": user_id,
                "name": name,
                "role": role,
                "token": token
            }
        )
    else:
        return jsonify(error=True, message="Invalid email or password"), 401

@auth_bp.route('/register/patient', methods=['POST'])
def register_patient():
    data = request.get_json()
    user_id = str(uuid.uuid4())
    name = data.get('name')
    email = data.get('email')
    whatsapp_number = data.get('whatsapp_number')
    password = data.get('password')
    role = 'Patient'

    user = {
        "user_id": user_id,
        "name": name,
        "email": email,
        "whatsapp_number": whatsapp_number,
        "password": password,
        "role": role
    }
    users.append(user)

    return jsonify(message="Patient registered successfully", name=name, email=email, whatsapp_number=whatsapp_number, role=role)

@auth_bp.route('/register/coass', methods=['POST'])
def register_coass():
    data = request.get_json()
    user_id = str(uuid.uuid4())
    name = data.get('name')
    email = data.get('email')
    whatsapp_number = data.get('whatsapp_number')
    password = data.get('password')
    university = data.get('university')
    semester = data.get('semester')
    student_id_number = data.get('student_id_number')
    hospital = data.get('hospital')
    role = 'Co Ass'

    user = {
        "user_id": user_id,
        "name": name,
        "email": email,
        "whatsapp_number": whatsapp_number,
        "password": password,
        "university": university,
        "semester": semester,
        "student_id_number": student_id_number,
        "hospital": hospital,
        "role": role
    }
    users.append(user)

    return jsonify(message="Co-Ass registered successfully", name=name, email=email, whatsapp_number=whatsapp_number, university=university, semester=semester, student_id_number=student_id_number, hospital=hospital, role=role)
