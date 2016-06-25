# [BuildersRecords API] (http://api.buildersrecords.com)

REST API for BuildersRecords clients.

## To Do List
```
    * Sphinx Documentation / Swagger
    * Flask-Admin
    * Flask-Security
    * Heroku SSL/Dynos/Database
    * Travis CI
    * Flask-CORS, routes/endpoints protection
    * Flask-Mail Send Registration Email / Celery / Testing Emails
    * Flask-SQLAlchemy
    * Flask-Migrate / Alembic
    * Flask-Restless
    * JWT authentication
    * Write more tests.py
    * Utility UBuildit Upload / Check invalid file
    * Version of API
    * Flask-Restful
    * Setup.py (look at uber's example)
    * Flask-Testing (nose, unittest, doctest, pytests)
```

## To Contribute

#### Step 1: Download the required software

+ [VirtualBox] (https://www.virtualbox.org/wiki/Downloads)
+ [Vagrant] (https://www.vagrantup.com/downloads.html)

#### Step 2: Clone the project
>
```bash
$ git clone git@github.com:maangulo12/buildersrecords-api.git
```

#### Step 3: Change directory into the cloned project
>
```bash
$ cd buildersrecords-api
```

#### Step 4: Run vagrant
>
```bash
$ vagrant up    
```

#### Step 5: SSH into the virtual machine
>
```bash
$ vagrant ssh
```

#### Step 6: CD into the vagrant folder
>
```bash
$ cd /vagrant/
```

#### Step 7: Setup the database
>
```bash
$ python3 manage.py recreate
```

#### Step 8: Run the application
>
```bash
$ python3 manage.py runapp    
```

#### Step 9: Open [http://localhost:4444] (http://localhost:4444)

## PostgreSQL Database

#### Login Credentials
```
Host: localhost
Port: 5432
Database: app_db
Username: postgres
Password: password
```

#### Database Migrations
+ [Flask-Migrate: Documentation]
    (http://flask-migrate.readthedocs.org/en/latest/)
+ [Flask-Migrate: Miguel Grindberg]
    (http://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask)
+ [Alembic Documentation]
    (http://alembic.readthedocs.org/en/latest/)

#### Commands for Database Migrations
>
```bash
# Create migrations folder
$ python3 manage.py db init
>
# Perform migration
$ python3 manage.py db migrate
>
# Upgrade database
$ python3 manage.py db upgrade
```

## Project Dependencies

#### Python Version
+ Python [3.5.1] (https://www.python.org/downloads/)

#### Libraries / Extensions
+ [Flask] (https://pypi.python.org/pypi/Flask): A lightweight Python web framework.
+ [Flask-Admin] (https://pypi.python.org/pypi/Flask-Admin): A Flask extension for creating the admin interface.
+ [Flask-Bcrypt] (https://pypi.python.org/pypi/Flask-Bcrypt): A Flask extension for hashing passwords using bcrypt.
+ [Flask-Cors] (https://pypi.python.org/pypi/Flask-Cors): A Flask extension for handling Cross Origin Resource Sharing.
+ [Flask-Mail] (https://pypi.python.org/pypi/Flask-Mail): A Flask extension for sending email messages.
+ [Flask-Migrate] (https://pypi.python.org/pypi/Flask-Migrate): A Flask extension for SQLAlchemy database migrations.
+ [Flask-Restless] (https://pypi.python.org/pypi/Flask-Restless): A Flask extension for easy RESTful API generation.
+ [Flask-Script] (https://pypi.python.org/pypi/Flask-Script): A Flask extension that provides support for command-line tasks.
+ [Flask-SQLAlchemy] (https://pypi.python.org/pypi/Flask-SQLAlchemy): A Flask extension that adds SQLAlchemy support.
+ [gunicorn] (https://pypi.python.org/pypi/gunicorn): Python WSGI HTTP Server for UNIX.
+ [nose] (https://pypi.python.org/pypi/nose): Library that extends unittest to make testing easier.
+ [psycopg2] (https://pypi.python.org/pypi/psycopg2): Python-PostgreSQL Database Adapter.
+ [PyJWT] (https://pypi.python.org/pypi/PyJWT): Library for implementing JSON Web Tokens for authentication.
+ [simplejson] (https://pypi.python.org/pypi/simplejson): Library for JSON encoding/decoding support.
+ [xlrd] (https://pypi.python.org/pypi/xlrd): Library for extracting data from Microsoft Excel spreadsheets.
