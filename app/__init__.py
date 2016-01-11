#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app package
    ~~~~~~~~~~~
    :copyright: (c) 2016

    This is the core package of this application.

    Flask and extensions:
        -Flask            : http://flask.pocoo.org/
        -Flask-SQLAlchemy : http://flask-sqlalchemy.pocoo.org/2.1/
        -Flask-Bcrypt     : http://flask-bcrypt.readthedocs.org/en/latest/
        -Flask-Restful    : http://flask-restful.readthedocs.org/en/0.3.5/
        -Flask-Restless   : http://flask-restless.readthedocs.org/en/latest/
        -Flask-Mail       : http://pythonhosted.org/Flask-Mail/
        -Flask-Migrate    : http://flask-migrate.readthedocs.org/en/latest/
        -Flask-Script     : http://flask-script.readthedocs.org/en/latest/
        -Stripe           : https://stripe.com/docs/api/python
"""

import stripe
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask_restful import Api
from flask.ext.restless import APIManager
from flask_mail import Mail
from flask.ext.migrate import Migrate
from flask.ext.script import Manager


# Create Flask application
app = Flask(__name__)

# Configurations
app.config.from_pyfile('settings.py')

# Stripe
stripe.api_key = app.config['STRIPE_API_KEY']

# Extensions
db       = SQLAlchemy(app)
bcrypt   = Bcrypt(app)
api      = Api(app)
restless = APIManager(app, flask_sqlalchemy_db=db)
mail     = Mail(app)
migrate  = Migrate(app, db)
manager  = Manager(app)

# Models
from app import models

# RESTful API
from app.api import auth
from app.api import mail
from app.api import subscriptions
from app.api import uploads

# RESTless API
from app.api import models

# Views
@app.route('/')
def index():
    return render_template('index.html')
