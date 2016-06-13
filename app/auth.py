# -*- coding: utf-8 -*-
"""
    app.auth
    ~~~~~~~~

    JSON Web Token (JWT) authentication for this Flask application.

    Using external modules such as:
    - PyJWT - https://github.com/jpadilla/pyjwt
"""

import jwt
from flask import request, current_app
from flask.ext.restless import ProcessingException

from app.models import User


def verify_jwt(*args, **kwargs):
    """
    Verifies JSON web token.
    """
    auth = request.headers.get('Authorization', None)

    if auth is None:
        raise ProcessingException('Authorization header was missing', 401)

    parts = auth.split()

    if parts[0].lower() != 'Bearer'.lower():
        raise ProcessingException('Unsupported authorization type', 400)
    elif len(parts) == 1:
        raise ProcessingException('Token missing', 400)
    elif len(parts) > 2:
        raise ProcessingException('Token contains spaces', 400)

    try:
        payload = jwt.decode(
            parts[1],
            current_app.config['SECRET_KEY'],
            options=dict(verify_exp=False)
        )
        user = User.query.filter_by(id=payload['user_id']).first()

        if user is None:
            raise ProcessingException('User does not exist', 401)

    except jwt.InvalidTokenError:
        raise ProcessingException('Token is invalid', 400)
