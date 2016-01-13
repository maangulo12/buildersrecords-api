#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app.api.utility
    ~~~~~~~~~~~~~~~

    This API contains utility endpoints.

    Current endpoints:
        -email          : /api/utility/email    (POST)
        -username       : /api/utility/username (POST)
        -ubuildit/file  : /api/utility/ubuildit (POST)
"""

from flask import request, make_response

from app import app, db
from app.models import User, Project, Category, Item
from app.utility import parse_ubuildit_file


URL = '/api/utility'


@app.route(URL + '/email', methods=['POST'])
def verify_email():
    """
    Verifies if email address already exists.

    Request Example:
    POST
    {
        email : 'email address'
    }
    """
    data      = request.get_json(force=True)
    email     = data.get('email', None)
    criterion = [email, len(data) == 1]

    if not all(criterion):
        return make_response('Bad Request', 400)

    user = User.query.filter_by(email=email).first()

    if user is None:
        return make_response('Valid email address', 200)
    else:
        return make_response('Email address already exists', 302)


@app.route(URL + '/username', methods=['POST'])
def verify_username():
    """
    Verifies if username already exists.

    Request Example:
    POST
    {
        username : 'username'
    }
    """
    data      = request.get_json(force=True)
    username  = data.get('username', None)
    criterion = [username, len(data) == 1]

    if not all(criterion):
        return make_response('Bad Request', 400)

    user = User.query.filter_by(username=username).first()

    if user is None:
        return make_response('Valid username', 200)
    else:
        return make_response('Username already exists', 302)


# Need route protection
@app.route(URL + '/ubuildit', methods=['POST'])
def parse_ubuildit_file():
    """
    Parses a UBuildIt Cost Review excel file.

    Request Example:
    POST
    {
        file         : 'file' (FileStorage object)
        name         : 'name'
        address      : 'address'
        city         : 'city'
        state        : 'state'
        zipcode      : 'zipcode'
        home_sq      : 'home_sq'
        project_type : 'project_type'
        user_id      : 'user_id'
    }
    """
    # get length of request
    file_obj     = request.files['file']
    name         = request.form['name']
    address      = request.form['address']
    city         = request.form['city']
    state        = request.form['state']
    zipcode      = request.form['zipcode']
    home_sq      = request.form['home_sq']
    project_type = request.form['project_type']
    user_id      = request.form['user_id']

    criterion    = [file_obj, name, address, city, state, zipcode, home_sq,
                    project_type, user_id]

    print(name)
    print(user_id)

    if not all(criterion):
        return make_response('Bad request', 400)

    try:
        # Check for invalid file
        file_contents = file_obj.read()
        category_list = parse_ubuildit_file(file_contents)

        project = Project(
            name=name,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            home_sq=home_sq,
            project_type=project_type,
            user_id=user_id
        )
        db.session.add(project)
        db.session.commit()

        for cat in category_list:
            category = Category(
                name=cat['category_name'],
                project_id=project['id']
            )
            db.session.add(category)
            db.session.commit()

            for cat_item in cat['item_list']:
                item = Item(
                    name=cat_item['cost_category'],
                    description=cat_item['description'],
                    estimated=cat_item['estimated'],
                    actual=cat_item['actual'],
                    category_id=category['id'],
                    project_id=project['id']
                )
                db.session.add(item)
                db.session.commit()

        return make_response('The file was successfully parsed', 201)

    except:
        return make_response('The file could not be parsed', 400)
