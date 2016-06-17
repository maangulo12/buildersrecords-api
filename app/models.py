# -*- coding: utf-8 -*-
"""
    app.models
    ~~~~~~~~~~

    This module implements the database models of this application.

        Models          Table Name
        - User          : users
        - Project       : projects
        - Category      : categories
        - Item          : items
        - Expenditure   : expenditure
        - Fund          : funds
        - Draw          : draws
        - Subcontractor : subcontractors

    Documentation:
        - Flask-SQLAlchemy - http://flask-sqlalchemy.pocoo.org/2.1/api/
        - SQLAlchemy       - http://docs.sqlalchemy.org/en/latest/
"""

from datetime import datetime

from app import db, bcrypt


# MODEL: User
class User(db.Model):
    """A model of a user."""
    __tablename__ = 'users'

    # Fields
    id           = db.Column(db.Integer, primary_key=True)
    email        = db.Column(db.String(50), nullable=False, unique=True)
    username     = db.Column(db.String(30), nullable=False, unique=True)
    password     = db.Column(db.String, nullable=False)
    date_created = db.Column(db.TIMESTAMP, nullable=False)

    # One-to-Many relationship (One user -> Many projects)
    projects = db.relationship('Project', backref='users')

    def __init__(self, email, username, password):
        """This function initializes a user."""
        self.email        = email
        self.username     = username
        # Protecting password using a one-way hash function
        self.password     = bcrypt.generate_password_hash(password)
        self.date_created = datetime.now()

    def check_password(self, password):
        """This function checks if passwords match."""
        return bcrypt.check_password_hash(self.password, password)


# MODEL: Project
class Project(db.Model):
    """A model of a project."""
    __tablename__ = 'projects'

    # Fields
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(50), nullable=False)
    address      = db.Column(db.String(80), nullable=False)
    city         = db.Column(db.String(30), nullable=False)
    state        = db.Column(db.String(2), nullable=False)
    zipcode      = db.Column(db.String(10), nullable=False)
    home_sq      = db.Column(db.Integer, nullable=False)
    project_type = db.Column(db.String(15), nullable=False)
    user_id      = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # One-to-Many relationships
    items          = db.relationship('Item', backref='projects')
    categories     = db.relationship('Category', backref='projects')
    funds          = db.relationship('Fund', backref='projects')
    expenditures   = db.relationship('Expenditure', backref='projects')
    subcontractors = db.relationship('Subcontractor', backref='projects')


# MODEL: Category
class Category(db.Model):
    """A model of a category."""
    __tablename__ = 'categories'

    # Fields
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(50), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    # One-to-Many relationships
    items        = db.relationship('Item', backref='categories')
    expenditures = db.relationship('Expenditure', backref='categories')


# MODEL: Item
class Item(db.Model):
    """A model of an item."""
    __tablename__ = 'items'

    # Fields
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(80))
    estimated   = db.Column(db.Numeric(12,2))
    actual      = db.Column(db.Numeric(12,2))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    project_id  = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    # One-to-Many relationship
    expenditures = db.relationship('Expenditure', backref='items')


# MODEL: Fund
class Fund(db.Model):
    """A model of a fund."""
    __tablename__ = 'funds'

    # Fields
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(50), nullable=False)
    loan       = db.Column(db.Boolean, nullable=False)
    amount     = db.Column(db.Numeric(12,2), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    # One-to-Many relationships
    expenditures = db.relationship('Expenditure', backref='funds')
    draws        = db.relationship('Draw', backref='funds')


# MODEL: Draw
class Draw(db.Model):
    """A model of a draw."""
    __tablename__ = 'draws'

    # Fields
    id      = db.Column(db.Integer, primary_key=True)
    date    = db.Column(db.Date, nullable=False)
    amount  = db.Column(db.Numeric(12,2), nullable=False)
    fund_id = db.Column(db.Integer, db.ForeignKey('funds.id'), nullable=False)


# MODEL: Expenditure
class Expenditure(db.Model):
    """A model of an expenditure."""
    __tablename__ = 'expenditures'

    # Fields
    id          = db.Column(db.Integer, primary_key=True)
    date        = db.Column(db.Date, nullable=False)
    company     = db.Column(db.String(50), nullable=False)
    cost        = db.Column(db.Numeric(12,2), nullable=False)
    fund_id     = db.Column(db.Integer, db.ForeignKey('funds.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    item_id     = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    project_id  = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)


# MODEL: Subcontractor
class Subcontractor(db.Model):
    """A model of a subcontractor."""
    __tablename__ = 'subcontractors'

    # Fields
    id         = db.Column(db.Integer, primary_key=True)
    company    = db.Column(db.String(50), nullable=False)
    person     = db.Column(db.String(50))
    number     = db.Column(db.String(15))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
