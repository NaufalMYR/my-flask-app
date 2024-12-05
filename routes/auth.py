from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import uuid

auth_bp = Blueprint('auth', __name__)

users = []  # Simulasi penyimpanan data pengguna

def get_request_data():
    if request.is_json:
        return request.get_json()
    else:
        return request.form

@auth_bp.route('/register', methods=['POST'])
def register():
    data = get_request_data()
    user_id = str(uuid.uuid4())
    role = data.get('role')

    if role not in ['Patient', 'Coass']:
        return jsonify(error=True, message="Invalid role. Must be 'Patient' or 'Coass'"), 400

    name = data.get('name')
    email = data.get('email')
    whatsapp_number = data.get('whatsapp_number')
    password = data.get('password')

    if not all([name, email, whatsapp_number, password]):
        return jsonify(error=True, message="Missing required fields for all roles"), 400

    user = {
        "user_id": user_id,
        "name": name,
        "email": email,
        "whatsapp_number": whatsapp_number,
        "password": password,
        "role": role
    }

    if role == 'Coass':
        university = data.get('university')
        semester = data.get('semester')
        student_id_number = data.get('student_id_number')
        hospital = data.get('hospital')

        if not all([university, semester, student_id_number, hospital]):
            return jsonify(error=True, message="Missing required fields for Coass"), 400

        user.update({
            "university": university,
            "semester": semester,
            "student_id_number": student_id_number,
            "hospital": hospital
        })

    # Simpan user ke dalam list
    users.append(user)

    # Debug: Cetak data pengguna yang baru terdaftar
    print("User registered:", user)

    return jsonify(
        error=False,
        message=f"{role} registered successfully",
        user={
            "user_id": user_id,
            "name": name,
            "email": email,
            "whatsapp_number": whatsapp_number,
            "role": role
        }
    ), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = get_request_data()
        email = data.get('email')
        password = data.get('password')

        # Debug: Cetak data yang diterima
        print("Login request data:", data)

        # Debug: Cetak data pengguna yang terdaftar
        print("Registered users:", users)

        # Cari pengguna berdasarkan email dan password
        user = next((user for user in users if user['email'] == email and user['password'] == password), None)
        
        if user:
            user_id = user['user_id']
            name = user['name']
            role = user['role']
            whatsapp_number = user['whatsapp_number']
            token = create_access_token(identity=str(user_id))  # Gunakan user_id sebagai string

            # Debug: Cetak token yang dibuat
            print("Generated JWT token:", token)
            
            return jsonify(
                error=False,
                message="success",
                loginResult={
                    "userId": user_id,
                    "name": name,
                    "role": role,
                    "whatsapp_number": whatsapp_number,
                    "token": token
                }
            )
        else:
            # Debug: Jika tidak menemukan pengguna
            print("Invalid email or password")
            return jsonify(error=True, message="Invalid email or password"), 401
    except Exception as e:
        print(f"Error during login: {e}")
        return jsonify(error=True, message="Server error"), 500
