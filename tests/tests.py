#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~~~~~

    This module is used for testing the backend of this application.

    -How to use it (type the following in the command-line):
        python3 manage.py runtests
"""

import unittest
from flask import current_app, json

from app import app, db


class AppTestCase(unittest.TestCase):

    def setUp(self):
        print('Setting up...')
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        print('Tearing down...')
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        print('TEST: test_app_exists')
        print(current_app)
        self.assertFalse(current_app is None)

    # def test_home_page(self):
    #     print('TEST: test_home_page')
    #     response = self.client.get('/')
    #     print(response.status_code)
    #     self.assertTrue(response.status_code == 200)

    def test_api(self):
        print('TEST: test_api')

        headers = { 'content-type': 'application/json' }

        print('POST /api/utility/email')
        response = self.client.post(
            '/api/utility/email',
            data=json.dumps(dict(email='runtests@gmail.com')),
            headers=headers
        )
        print(response.status_code)
        self.assertTrue(response.status_code == 200)

        print('POST /api/utility/username')
        response = self.client.post(
            '/api/utility/username',
            data=json.dumps(dict(username='runtests')),
            headers=headers
        )
        print(response.status_code)
        self.assertTrue(response.status_code == 200)

        print('POST /api/users')
        response = self.client.post(
            '/api/users',
            data=json.dumps(dict(
                email='runtests@gmail.com',
                username='runtests',
                password='runtests'
            )),
            headers=headers
        )
        print(response.status_code)
        self.assertTrue(response.status_code == 201)

        print('POST /api/utility/email (test 2)')
        response = self.client.post(
            '/api/utility/email',
            data=json.dumps(dict(email='runtests@gmail.com')),
            headers=headers
        )
        print(response.status_code)
        self.assertTrue(response.status_code == 302)

        print('POST /api/utility/username (test 2)')
        response = self.client.post(
            '/api/utility/username',
            data=json.dumps(dict(username='runtests')),
            headers=headers
        )
        print(response.status_code)
        self.assertTrue(response.status_code == 302)

        print('POST /api/auth (authentication)')
        response = self.client.post(
            '/api/auth',
            data=json.dumps(dict(
                login='runtests',
                password='runtests'
            )),
            headers=headers
        )
        print(response.status_code)
        self.assertTrue(response.status_code == 200)

        print('STORE JSON Web Token')
        data = json.loads(response.data.decode('utf-8'))
        headers['authorization'] = 'Bearer ' + data['token']

        print('GET /api/users/1')
        response = self.client.get(
            '/api/users/1',
            headers=headers
        )
        print(response.status_code)
        self.assertTrue(response.status_code == 200)


if __name__ == '__main__':
    unittest.main()
