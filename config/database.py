import os
from dotenv import load_dotenv
from google.cloud import firestore

load_dotenv()

class Config:
    PROJECT_ID = os.getenv('GCP_PROJECT_ID')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Inisialisasi Firestore
firestore_client = firestore.Client()
