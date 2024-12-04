import os
from dotenv import load_dotenv

load_dotenv()  # Memuat variabel lingkungan dari .env

from config import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('HOST', 'localhost'), port=int(os.getenv('PORT', 5000)))
