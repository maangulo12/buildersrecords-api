# -*- coding: utf-8 -*-
"""
    app.config
    ~~~~~~~~~~

    This module is used to configure this application.
"""

import os


# Flask
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')
DEBUG      = os.environ.get('DEBUG', True)
TESTING    = os.environ.get('TESTING', True)

# Email
MAIL_SERVER         = os.environ.get('MAIL_SERVER', 'localhost')
MAIL_PORT           = os.environ.get('MAIL_PORT', 25)
MAIL_USE_SSL        = os.environ.get('MAIL_USE_SSL', False)
MAIL_USERNAME       = os.environ.get('MAIL_USERNAME', 'email@address.com')
MAIL_PASSWORD       = os.environ.get('MAIL_PASSWORD' 'password')
MAIL_DEFAULT_SENDER = ('BuildersRecords', MAIL_USERNAME)
MAIL_DEBUG          = False

# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
    'postgresql://postgres:password@localhost:5432/app_db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
