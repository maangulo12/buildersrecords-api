# -*- coding: utf-8 -*-
"""
    app.config
    ~~~~~~~~~~

    Flask application configuration module.

    Flask documentation on configuration handling.
    http://flask.pocoo.org/docs/0.11/config/
"""

import os


# Flask
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')
DEBUG      = os.environ.get('DEBUG', True)
TESTING    = os.environ.get('TESTING', True)

# Server
SERVER_HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
SERVER_PORT = os.environ.get('SERVER_PORT', 4444)

# Email
MAIL_SERVER         = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT           = os.environ.get('MAIL_PORT', 465)
MAIL_USE_SSL        = os.environ.get('MAIL_USE_SSL', True)
MAIL_DEBUG          = os.environ.get('MAIL_DEBUG', False)
MAIL_USERNAME       = os.environ.get('MAIL_USERNAME', 'buildersrecords.app@gmail.com')
MAIL_PASSWORD       = os.environ.get('MAIL_PASSWORD' 'buildersrecords123')
MAIL_DEFAULT_SENDER = ('BuildersRecords', MAIL_USERNAME)

# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
    'postgresql://postgres:password@localhost:5432/app_db')
