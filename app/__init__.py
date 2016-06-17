# -*- coding: utf-8 -*-
"""
    BuildersRecords API
    ~~~~~~~~~~~~~~~~~~~

    A Flask application with several extensions.

    Extensions include:
    - Flask-Admin - Used for creating the admin interface.
    - Flask-Bcrypt - Used for hashing passwords using bcrypt.
    - Flask-Cors - Used for handling Cross Origin Resource Sharing (CORS).
    - Flask-Mail - Used for sending emails.
    - Flask-Migrate - Used for performing SQLAlchemy database migrations.
    - Flask-Restless - Used for RESTful API generation.
    - Flask-Script - Used for running external scripts.
    - Flask-SQLAlchemy - Used for SQLAlchemy support.
"""

from flask import Flask, render_template
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_script import Manager
from flask_cors import CORS


# Initializing Flask app
app = Flask(__name__)

# Configuring Flask app from config module
app.config.from_pyfile('config.py')

# Initializing Flask app extensions
ad = Admin(app, template_mode='bootstrap3')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
restless = APIManager(app, flask_sqlalchemy_db=db)
mail = Mail(app)
migrate = Migrate(app, db)
manager = Manager(app)
cors = CORS(app)

# Importing database models
from app import models

# Importing admin module
from app import admin

# Importing API endpoints
from app.api import auth
from app.api import utility

# Importing API endpoints using RESTless
from app.api import models


# Initial route
@app.route('/')
def index():
    """Render the initial view."""
    return render_template('index.html')
