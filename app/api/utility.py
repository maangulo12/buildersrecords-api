#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app.api.utility
    ~~~~~~~~~~~~~~~

    This API contains utility endpoints.

    Current endpoints:
        -email    : /api/utility/email    (POST)
        -username : /api/utility/username (POST)
"""

from flask import request, make_response

from app import app
from app.models import User


URL = '/api/utility'


@app.route(URL + '/email', methods=['POST'])
def verify_email():
    """
    Verifies if email address already exists.

    Request Example:
    POST
    {
        email : 'email address'
    }
    """
    data      = request.get_json(force=True)
    email     = data.get('email', None)
    criterion = [email, len(data) == 1]

    if not all(criterion):
        return make_response('Bad Request', 400)

    user = User.query.filter_by(email=email).first()

    if user is None:
        return make_response('Valid email address', 200)
    else:
        return make_response('Email address already exists', 302)


@app.route(URL + '/username', methods=['POST'])
def verify_username():
    """
    Verifies if username already exists.

    Request Example:
    POST
    {
        username : 'username'
    }
    """
    data      = request.get_json(force=True)
    username  = data.get('username', None)
    criterion = [username, len(data) == 1]

    if not all(criterion):
        return make_response('Bad Request', 400)

    user = User.query.filter_by(username=username).first()

    if user is None:
        return make_response('Valid username', 200)
    else:
        return make_response('Username already exists', 302)
