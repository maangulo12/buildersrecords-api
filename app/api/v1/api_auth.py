# -*- coding: utf-8 -*-
"""
    app.api.api_auth
    ~~~~~~~~~~~~~~~~

    This module contains the API v1 endpoints for authentication.

    Endpoints:
        - Auth : /api/auth (POST)
"""

import jwt
from flask import request, jsonify, make_response

from app import app
from app.models import User


URL = '/api/auth'


@app.route(URL, methods=['POST'])
def authentication():
    """
    Authenticates a user and sends a JWT.

    Request Example:
    POST
    {
        login    : 'username' or 'email address'
        password : 'password'
    }
    """
    data      = request.get_json(force=True)
    login     = data.get('login', None)
    password  = data.get('password', None)
    criterion = [login, password, len(data) == 2]

    if not all(criterion):
        return make_response('Bad Request', 400)

    user = User.query.filter_by(username=login).first()

    if user is None:
        user = User.query.filter_by(email=login).first()

    if user and user.check_password(password):
        token = jwt.encode(dict(user_id=user.id), app.config['SECRET_KEY'])
        return make_response(jsonify(token=token), 200)
    else:
        return make_response('Unauthenticated', 401)
