from flask import Flask, app, request, jsonify, send_from_directory
from flask_cors import CORS
from db import check_password_hash
import hashlib
import os

app = Flask(__name__, static_folder='../frontend')
CORS(app)

@app.route('/')
def home():
    return send_from_directory('../frontend', 'index.html')

@app.route('/frontend/<path:filename>')
def frontend_files(filename):
    return send_from_directory('../frontend', filename)

@app.route('/check', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')

    if not password:
        return jsonify({'error': 'No password provided'}), 400

    hashed = hashlib.sha256(password.encode()).hexdigest()
    result = check_password_hash(hashed)

    if result:
        return jsonify({'leaked': True, 'source': result[0]['source']})
    else:
        return jsonify({'leaked': False})

if __name__ == '__main__':
    app.run(debug=True, port=5000)