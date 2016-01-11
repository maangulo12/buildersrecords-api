#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app.settings
    ~~~~~~~~~~~~

    This module contains the config variables of this application.
"""

import os


# Flask app secret key
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')

# WSGI server
SERVER_HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
SERVER_PORT = os.environ.get('SERVER_PORT', 4444)
DEBUG       = os.environ.get('DEBUG', True)
TESTING     = os.environ.get('TESTING', False) # Change this for mail testing

# Stripe
STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY',
    'sk_test_N625XoY2OXkrQzpDiRg7tt1g')

# Auth
AUTH_SECRET = os.environ.get('AUTH_SECRET', 'secret')

# Email
MAIL_SERVER         = 'smtp.gmail.com'
MAIL_PORT           = 465
MAIL_USE_SSL        = True
MAIL_USERNAME       = os.environ.get('MAIL_USERNAME', 'buildersrecords.app@gmail.com') # change this for mail testing
MAIL_PASSWORD       = os.environ.get('MAIL_PASSWORD' 'buildersrecords123') # change this for mail testing
MAIL_DEFAULT_SENDER = ('BuildersRecords', MAIL_USERNAME)

# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
    'postgresql://postgres:password@localhost:5432/app_db')