#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    manage.py
    ~~~~~~~~~

    This module is used for doing quick commands in this application.

    Commands:
    - create   : Creates all of the tables in the database.
    - drop     : Drops all of the tables from the database.
    - populate : Populates the database with sample data.
    - recreate : Drops, recreates, and populates the tables in the database.
    - runapp   : Runs the application.
    - runtests : Runs tests using nose.
    - db       : Performs database migrations.
    - shell    : Runs a Python shell using IPython.

    HOW TO USE:
    - Type the following in the command-line
      python3 manage.py (insert command here)
"""

import os
from flask_migrate import MigrateCommand

from app import app, db, manager
from tests.sample_data import populate_db


# COMMAND: create
@manager.command
def create():
    """Creates all of the tables in the database."""
    db.create_all()
    print('Created all of the tables in the database.')


# COMMAND: drop
@manager.command
def drop():
    """Drops all of the tables from the database."""
    db.drop_all()
    print('Dropped all of the tables from the database.')


# COMMAND: populate
@manager.command
def populate():
    """Populates the database with sample data."""
    populate_db()
    print('Populated the database with sample data.')


# COMMAND: recreate
@manager.command
def recreate():
    """Drops, recreates, and populates the tables in the database."""
    drop()
    create()
    populate()


# COMMAND: runapp
@manager.command
def runapp():
    """Runs the application."""
    app.run(host=app.config['SERVER_HOST'], port=app.config['SERVER_PORT'])


# COMMAND: runtests
@manager.command
def runtests():
    """Runs tests to this application using nose."""
    os.system('nosetests tests/tests.py')
    print('Finished running all tests.')


# COMMAND: db
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
