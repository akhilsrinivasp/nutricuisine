from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from flask import request
from flask import Blueprint, request, jsonify

import os
import secrets  
from hashlib import sha256
from flask import request
from flask_restful import Resource
from nutricuisine.models import User, users_schema, user_schema
from nutricuisine import db

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    # no image
    if not request.form:
        return {'message': 'No data found'}, 404
    data = request.form
    name = data['name']
    username = data['username']
    password = data['password']
    email = data['email']
    
    user = User.query.filter_by(username=username).first()
    
    if user:
        return {'message': 'User {} already exists'.format(username)}, 409
    
    new_user = User(
        name=name,
        username=username,
        password=generate_password_hash(password),
        email=email
    )
    
    db.session.add(new_user)
    db.session.commit()
     
    return {'message': 'User {} was created'.format(username)}, 201
    
    
@auth_blueprint.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        # if not user:
        #     return {'message': 'User {} doesn\'t exist'.format(username)}, 404
        
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return {
                'message': 'Logged in as {}'.format(user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        else:
            return {'message': 'Wrong credentials'}, 401
    else:
        return {'error': 'Invalid request method'}
    
@auth_blueprint.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    if request.method == 'POST':
        username = get_jwt_identity()
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        
        return {
            'message': 'Access token refreshed for {}'.format(username),
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200
    else:
        return {'error': 'Invalid request method'}

@auth_blueprint.route('/reset_password', methods=['PUT'])
@jwt_required()
def reset_password():
    if request.method == 'PUT':
        username = get_jwt_identity()
        old_password = request.form.get('old_password')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(username)}, 404
        
        if not check_password_hash(user.password, old_password):
            return {'message': 'Wrong credentials'}, 401
        
        user.password = generate_password_hash(password)
        db.session.commit()
        return {'message': 'Password updated'}, 200
    else:
        return {'error': 'Invalid request method'}
    
@auth_blueprint.route('/get_user', methods=['GET'])
@jwt_required()
def get_user():
    if request.method == 'GET':
        username = get_jwt_identity()
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(username)}, 404
        
        return user_schema.dump(user), 200
    else:
        return {'error': 'Invalid request method'}
    
@auth_blueprint.route('/get_all_users', methods=['GET'])
def dummy():
    if request.method == 'GET':
        users = User.query.all()
        return users_schema.dump(users), 200
    else:
        return {'error': 'Invalid request method'}
