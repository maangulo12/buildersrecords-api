# -*- coding: utf-8 -*-
"""
    app
    ~~~~~~

    A Flask application with several extensions.

    Extensions include:
    - Flask-Bcrypt : Used for hashing passwords.
    - Flask-Cors
    - Flask-Mail
    - Flask-Migrate
    - Flask-Restless
    - Flask-Script
    - Flask-SQLAlchemy
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.restless import APIManager
from flask_mail import Mail
from flask.ext.migrate import Migrate
from flask.ext.script import Manager
from flask.ext.cors import CORS


# Initializing Flask app
app = Flask(__name__)

# Configuring Flask app from config module
app.config.from_pyfile('config.py')

# Initializing Flask app extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
restless = APIManager(app, flask_sqlalchemy_db=db)
mail = Mail(app)
migrate = Migrate(app, db)
manager = Manager(app)
cors = CORS(app)

# Importing database models
from app import models

# Importing API endpoints
from app.api import auth
from app.api import utility

# Importing API endpoints (RESTless)
from app.api import models


@app.route('/')
def index():
    """Render the initial view."""
    return render_template('index.html')
