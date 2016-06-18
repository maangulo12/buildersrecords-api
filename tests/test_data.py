# -*- coding: utf-8 -*-
"""
    tests.test_data
    ~~~~~~~~~~~~~~~~~

    This module populates the database with test data.
"""

import random
from flask import json

from app import app
from app.utility import parse_ubuildit_file, parse_invoice_file
from tests.utility import safe_json, get_token


def populate_db():
    """Populates the database with sample data."""
    with app.test_client() as c:
        # Test user login information
        email = 'test@gmail.com'
        username = 'test'
        password = 'test'

        # HTTP header
        headers = { 'Content-Type': 'application/json' }

        # Create test user
        rv = c.post('/api/users',
            data=safe_json(
                email=email,
                username=username,
                password=password
            ),
            headers=headers
        )

        # Authenticate test user
        rv = c.post('/api/auth',
            data=safe_json(
                login=username,
                password=password
            ),
            headers=headers
        )

        # Add token to HTTP header
        token = get_token(rv)
        headers['Authorization'] = 'Bearer {}'.format(token)

        # Create a new project
        rv = c.post('/api/projects',
            data=safe_json(
                name='UBuildIt - Tim & Maritza Messer',
                address='251 Wizard Way',
                city='Spring Branch',
                state='TX',
                zipcode='78070',
                home_sq='2000',
                project_type='ubuildit',
                user_id=1
            ),
            headers=headers
        )

        # The path to the sample data (Excel file)
        path = 'tests/data/spreadsheet.xlsx'

        # Open the file
        f = open(path, 'rb')
        data = f.read()

        # Parse the ubuildit file
        category_list = parse_ubuildit_file(data)

        # Iterate over the list of categories
        for category in category_list:
            # Add category
            rv = c.post('/api/categories',
                data=safe_json(
                    name=category['category_name'],
                    project_id=1
                ),
                headers=headers
            )

            # Iterate over the list of items
            for item in category['item_list']:
                # Add item
                rv = c.post('/api/items',
                    data=safe_json(
                        name=item['cost_category'],
                        description=item['description'],
                        estimated=item['estimated'],
                        actual=item['actual'],
                        category_id=category_list.index(category) + 1,
                        project_id=1
                    ),
                    headers=headers
                )

        # Add funds
        rv = c.post('/api/funds',
            data=json.dumps(dict(
                name='Messer',
                loan=False,
                amount=100000.00,
                project_id=1
            ), use_decimal=True),
            headers=headers
        )
        rv = c.post('/api/funds',
            data=json.dumps(dict(
                name='Blanco Loan',
                loan=True,
                amount=330000.00,
                project_id=1
            ), use_decimal=True),
            headers=headers
        )

        # Add draws
        rv = c.post('/api/draws',
            data=json.dumps(dict(
                date='09/24/2015',
                amount=25000.00,
                fund_id=2
            ), use_decimal=True),
            headers=headers
        )
        rv = c.post('/api/draws',
            data=json.dumps(dict(
                date='10/01/2015',
                amount=5000.00,
                fund_id=2
            ), use_decimal=True),
            headers=headers
        )
        rv = c.post('/api/draws',
            data=json.dumps(dict(
                date='10/03/2015',
                amount=7500.00,
                fund_id=2
            ), use_decimal=True),
            headers=headers
        )

        # Parse invoice file
        expenditure_list = parse_invoice_file(path)

        # Iterate over the list of expenditures
        for expenditure in expenditure_list:
            fund_id = 1
            if expenditure['notes'] == 'Blanco':
                fund_id = 2

            # Add expenditure
            rv = c.post('/api/expenditures',
                data=json.dumps(dict(
                    date=expenditure['date'],
                    company=expenditure['company'],
                    cost=expenditure['cost'],
                    category_id=random.randint(1, 8),
                    item_id=random.randint(1, 110),
                    fund_id=fund_id,
                    project_id=1
                ), use_decimal=True),
                headers=headers
            )

        # Add subcontractors
        rv = c.post('/api/subcontractors',
            data=safe_json(
                company='84 Lumber',
                person='John Smith',
                number='210-543-4534',
                project_id=1
            ),
            headers=headers
        )
        rv = c.post('/api/subcontractors',
            data=safe_json(
                company='Ez Company',
                person='Shawn Tarver',
                number='512-586-6516',
                project_id=1
            ),
            headers=headers
        )
        rv = c.post('/api/subcontractors',
            data=safe_json(
                company='Coca Cola',
                person='Mike Jones',
                number='210-253-5861',
                project_id=1
            ),
            headers=headers
        )
