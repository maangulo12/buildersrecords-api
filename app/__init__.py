#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app package
    ~~~~~~~~~~~
    :copyright: (c) 2016

    This is the core package of this application.
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask_restful import Api
from flask.ext.restless import APIManager
from flask_mail import Mail
from flask.ext.migrate import Migrate
from flask.ext.script import Manager
from flask.ext.cors import CORS


# Create Flask application
app = Flask(__name__)

# Configurations
app.config.from_pyfile('settings.py')

# Extensions
db       = SQLAlchemy(app)
bcrypt   = Bcrypt(app)
api      = Api(app)
restless = APIManager(app, flask_sqlalchemy_db=db)
mail     = Mail(app)
migrate  = Migrate(app, db)
manager  = Manager(app)
cors     = CORS(app)

# Models
from app import models

# RESTful API
from app.api import auth
from app.api import stripe
from app.api import utility

# RESTless API
from app.api import models

# Views
@app.route('/')
def index():
    return render_template('index.html')
