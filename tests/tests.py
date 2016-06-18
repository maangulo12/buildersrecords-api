# -*- coding: utf-8 -*-
"""
    tests.tests
    ~~~~~~~~~~~

    Unittest module for testing this application.

    TO RUN THE TESTS:
    - Type the following in the command-line
      python3 manage.py runtests
"""

import unittest
from flask import current_app, json

from app import app, db
from tests.test_utils import safe_json, get_token


class AppTestCase(unittest.TestCase):
    """
    This class contains the functions for testing this application. There is
    a function that runs at the start of every test and another at the end of
    every test.
    """
    def setUp(self):
        """
        This function sets up the tests. It runs at the start of every test.
        It sets up the test client and clears the database at the start of
        every test.
        """
        print('Setting up...')
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """
        This function runs at the end of every test. It clears the database at
        the end of every test.
        """
        print('Tearing down...')
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        """
        This function checks if the application is running.
        """
        print('TEST: test_app_exists')
        print(current_app)
        self.assertFalse(current_app is None)

    def test_home_page(self):
        """
        This function checks if the home page exists.
        """
        print('TEST: test_home_page')
        rv = self.client.get('/')
        print(rv.status_code)
        self.assertTrue(rv.status_code == 200)

    # This test is skipped
    @unittest.skip("Skipping test")
    def test_admin_page(self):
        """
        This function checks if the admin page exists.
        """
        print('TEST: test_admin_page')
        rv = self.client.get('/admin')
        print(rv.status_code)
        self.assertTrue(rv.status_code == 200)

    def test_api(self):
        """
        This function tests the API (endpoints) of this application.
        """
        # Start of the test
        print('TEST: test_api')
        headers = { 'Content-Type': 'application/json' }

        # Check if email exists
        print('POST /api/utility/email')
        rv = self.client.post('/api/utility/email',
            data=safe_json(email='runtests@gmail.com'),
            headers=headers
        )
        print(rv.status_code)
        self.assertTrue(rv.status_code == 200)

        # Check if username exists
        print('POST /api/utility/username')
        rv = self.client.post('/api/utility/username',
            data=safe_json(username='runtests'),
            headers=headers
        )
        print(rv.status_code)
        self.assertTrue(rv.status_code == 200)

        # Create a new user
        print('POST /api/users')
        rv = self.client.post('/api/users',
            data=safe_json(
                email='runtests@gmail.com',
                username='runtests',
                password='runtests'
            ),
            headers=headers
        )
        print(rv.status_code)
        self.assertTrue(rv.status_code == 201)

        # Check if email exists
        print('POST /api/utility/email (test 2)')
        rv = self.client.post('/api/utility/email',
            data=safe_json(email='runtests@gmail.com'),
            headers=headers
        )
        print(rv.status_code)
        self.assertTrue(rv.status_code == 302)

        # Check if username exists
        print('POST /api/utility/username (test 2)')
        rv = self.client.post('/api/utility/username',
            data=safe_json(username='runtests'),
            headers=headers
        )
        print(rv.status_code)
        self.assertTrue(rv.status_code == 302)

        # Authenticate user
        print('POST /api/auth (authentication)')
        rv = self.client.post('/api/auth',
            data=safe_json(
                login='runtests',
                password='runtests'
            ),
            headers=headers
        )
        print(rv.status_code)
        self.assertTrue(rv.status_code == 200)

        # Add token to HTTP header
        print('STORE JSON Web Token')
        token = get_token(rv)
        headers['Authorization'] = 'Bearer {}'.format(token)

        # Check if the user exists.
        print('GET /api/users/1')
        rv = self.client.get('/api/users/1',
            headers=headers
        )
        print(rv.status_code)
        self.assertTrue(rv.status_code == 200)


if __name__ == '__main__':
    unittest.main()
