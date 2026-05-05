import os
import hashlib
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from db import check_password_hash

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# ── Serve Frontend ───────────────────────────────────────────────

@app.route('/')
def home():
    return send_from_directory('../frontend', 'index.html')

@app.route('/frontend/<path:filename>')
def frontend_files(filename):
    return send_from_directory('../frontend', filename)

# ── Check Password ───────────────────────────────────────────────

@app.route('/check', methods=['POST'])
def check_password():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'error': 'No data received'
            }), 400

        password = data.get('password', '')

        if not password:
            return jsonify({
                'error': 'No password provided'
            }), 400

        if len(password) > 128:
            return jsonify({
                'error': 'Password too long'
            }), 400

        # Hash the password
        hashed = hashlib.sha256(
            password.encode('utf-8')
        ).hexdigest()

        # Check in database
        result = check_password_hash(hashed)

        if result:
            return jsonify({
                'leaked': True,
                'source': result[0]['source'],
                'message': 'Password found in breach database!'
            })
        else:
            return jsonify({
                'leaked': False,
                'message': 'Password not found in any breach database'
            })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

# ── Health Check ─────────────────────────────────────────────────

@app.route('/health')
def health():
    return jsonify({
        'status': 'online',
        'message': 'SecureCheck API is running'
    })

# ── Run App ──────────────────────────────────────────────────────

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False
    )