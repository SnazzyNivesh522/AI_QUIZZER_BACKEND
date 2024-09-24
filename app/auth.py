from flask import request, jsonify
from flask_jwt_extended import create_access_token, JWTManager
from config import app

jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username and password:
        token = create_access_token(identity=username,expires_delta=app.config['JWT_ACCESS_TOKEN_EXPIRES'])
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid username or password'}), 401
