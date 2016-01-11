# [BuildersRecords API] (http://api.buildersrecords.com)

Backend API for BuildersRecords apps.

## Required Software

+ [VirtualBox] (https://www.virtualbox.org/wiki/Downloads)
+ [Vagrant] (https://www.vagrantup.com/downloads.html)

## For Development

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

#### SSH into the virtual machine (VM)
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

#### Read:
+ [Flask-Migrate: Documentation]
    (http://flask-migrate.readthedocs.org/en/latest/)
+ [Flask-Migrate: Miguel Grindberg]
    (http://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask)
+ [Alembic Documentation]
    (http://alembic.readthedocs.org/en/latest/)

#### Commands:
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
