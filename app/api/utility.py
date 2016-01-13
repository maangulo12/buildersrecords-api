#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app.api.utility
    ~~~~~~~~~~~~~~~

    This API contains utility endpoints.

    Current endpoints:
        -email          : /api/utility/email          (POST)
        -username       : /api/utility/username       (POST)
        -ubuildit/file  : /api/utility/ubuildit/parse (POST)
        -ubuildit/parse : /api/utility/ubuildit/save  (POST)
"""

from flask import request, make_response, g

from app import app, db
from app.models import User, Category, Item
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


# Needs route protection
@app.route(URL + '/ubuildit/parse', methods=['POST'])
def parse_ubuildit_file():
    """
    Parses a UBuildIt Cost Review excel file.

    Request Example:
    POST
    {
        file : 'file' (FileStorage object)
    }
    """
    # get request size
    file_obj  = request.files['file']
    criterion = [file_obj]

    if not all(criterion):
        return make_response('Bad request', 400)

    try:
        file_contents = file_obj.read()
        g.data = parse_ubuildit_file(file_contents)
        return make_response('The file is OK', 200)

    except:
        return make_response('Incorrect file', 400)


# Needs route protection
@app.route(URL + '/ubuildit/save', methods=['POST'])
def save_contents():
    """
    Save the contents of a UBuildIt Cost Review excel file.

    Request Example:
    POST
    {
        project_id : 'project id'
    }
    """
    data       = request.get_json(force=True)
    project_id = data.get('project_id', None)
    criterion  = [project_id, len(data) == 1]

    if not all(criterion):
        return make_response('Bad request', 400)

    try:
        category_list = getattr(g, 'data', None)

        for cat in category_list:
            category = Category(
                name=cat['category_name'],
                project_id=project_id
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
                    project_id=project_id
                )
                db.session.add(item)
                db.session.commit()

        return make_response('The contents of the file were saved', 200)

    except:
        return make_response('Could not save the contents of the file', 400)
