# [BuildersRecords API] (http://api.buildersrecords.com)

Business API for BuildersRecords clients.

## To Do List
```
    * Flask-Mail Send Registration Email / Celery
    * Utility UBuildit Upload / Check invalid file
    * Version of API
    * Flask-Admin
    * Flask-Restful
    * Security CORS, routes/endpoints
    * Flask-Migrate / Alembic
    * Sphinx Documentation
    * Setup.py (look at uber's example)
    * Flask-Testing (nose, unittest, doctest, pytests)
```

## Required Software

+ [VirtualBox] (https://www.virtualbox.org/wiki/Downloads)
+ [Vagrant] (https://www.vagrantup.com/downloads.html)

## For Development/Contribution

#### Clone the project
>
```bash
$ git clone git@github.com:maangulo12/buildersrecords-api.git
$ cd buildersrecords-api
```

#### Run vagrant
>
```bash
$ vagrant up    
```

#### SSH into the virtual machine
>
```bash
$ vagrant ssh
```

#### CD into the vagrant folder
>
```bash
$ cd /vagrant/
```

#### Run app
>
```bash
$ python3 manage.py recreate
$ python3 application.py    
```

#### Open [http://localhost:4444] (http://localhost:4444)

## VM

#### PostgreSQL Database Server on the VM
```
Host: localhost
Port: 5432
Database: app_db
Username: postgres
Password: password
```

## Database Migrations

#### Read
+ [Flask-Migrate: Documentation]
    (http://flask-migrate.readthedocs.org/en/latest/)
+ [Flask-Migrate: Miguel Grindberg]
    (http://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask)
+ [Alembic Documentation]
    (http://alembic.readthedocs.org/en/latest/)

#### Commands
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

## Dependencies

#### Python Version
+ Python [3.5.1] (https://www.python.org/downloads/)

#### Extensions
+ [Flask] (https://pypi.python.org/pypi/Flask) : A lightweight Python web framework.
+ [Flask-Bcrypt] (https://pypi.python.org/pypi/Flask-Bcrypt) : A Flask extension that provides bcrypt support for hashing passwords.
+ [Flask-Cors] (https://pypi.python.org/pypi/Flask-Cors) : A Flask extension for handling Cross Origin Resource Sharing.
+ [Flask-Mail] (https://pypi.python.org/pypi/Flask-Mail) : A Flask extension for sending email messages.
+ [Flask-Migrate] (https://pypi.python.org/pypi/Flask-Migrate) : A Flask extension for SQLAlchemy database migrations.
+ [Flask-Restless] (https://pypi.python.org/pypi/Flask-Restless) : A Flask extension for easy RESTful API generation.
+ [Flask-Script] (https://pypi.python.org/pypi/Flask-Script) : A Flask extension that provides support for command-line tasks.
+ [Flask-SQLAlchemy] (https://pypi.python.org/pypi/Flask-SQLAlchemy) : A Flask extension that adds SQLAlchemy support.
+ [gunicorn] (https://pypi.python.org/pypi/gunicorn) : Python WSGI HTTP Server for UNIX.
+ [nose] (https://pypi.python.org/pypi/nose) : Library that extends unittest to make testing easier.
+ [psycopg2] (https://pypi.python.org/pypi/psycopg2) : Python-PostgreSQL Database Adapter.
+ [PyJWT] (https://pypi.python.org/pypi/PyJWT) : Library for implementing JSON Web Tokens for authentication.
+ [simplejson] (https://pypi.python.org/pypi/simplejson) : Library for JSON encoding and decoding.
+ [xlrd] (https://pypi.python.org/pypi/xlrd) : Library for extracting data from Microsoft Excel spreadsheet files.
