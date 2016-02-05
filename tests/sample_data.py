#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    sample_data
    ~~~~~~~~~~~

    This module is used for populating the database with sample data.
"""

import random
import stripe
from flask import json

from app import app
from app.utility import parse_ubuildit_file, parse_invoice_file


FILE_PATH = 'tests/data/spreadsheet.xlsx'


def populate_db():
    client = app.test_client()

    # stripe.Plan.create(
    #     amount=0,
    #     interval='monthly',
    #     name='Free Plan',
    #     currency='usd',
    #     id='free'
    # )
    # stripe.Plan.create(
    #     amount=2500,
    #     interval='month',
    #     name='Monthly Plan',
    #     currency='usd',
    #     id='monthly'
    # )
    # stripe.Plan.create(
    #     amount=26700,
    #     interval='year',
    #     name='Yearly Plan',
    #     currency='usd',
    #     id='yearly'
    # )

    token = stripe.Token.create(
        card=dict(
            number=4242424242424242,
            exp_month=1,
            exp_year=2025,
            cvc=333,
            name='TEST NAME'
        )
    )

    headers = { 'content-type': 'application/json' }

    response = client.post(
        '/api/stripe',
        data=json.dumps(dict(
            email='test@gmail.com',
            username='test',
            password='test',
            plan='free',
            token_id=token['id']
        )),
        headers=headers
    )

    response = client.post(
        '/api/auth',
        data=json.dumps(dict(
            login='test',
            password='test'
        ))
    )

    data = json.loads(response.data)
    headers['authorization'] = 'Bearer ' + data['token']

    client.post(
        '/api/projects',
        data=json.dumps(dict(
            name='UBuildIt - Tim & Maritza Messer',
            address='251 Wizard Way',
            city='Spring Branch',
            state='TX',
            zipcode='78070',
            home_sq='2000',
            project_type='ubuildit',
            user_id=1
        )),
        headers=headers
    )

    file_obj = open(FILE_PATH, 'rb')
    file_contents = file_obj.read()
    category_list = parse_ubuildit_file(file_contents)

    for category in category_list:
        client.post(
            '/api/categories',
            data=json.dumps(dict(
                name=category['category_name'],
                project_id=1
            )),
            headers=headers
        )

        for item in category['item_list']:
            client.post(
                '/api/items',
                data=json.dumps(dict(
                    name=item['cost_category'],
                    description=item['description'],
                    estimated=item['estimated'],
                    actual=item['actual'],
                    category_id=category_list.index(category) + 1,
                    project_id=1
                )),
                headers=headers
            )


    client.post(
        '/api/funds',
        data=json.dumps(dict(
            name='Messer',
            loan=False,
            amount=100000.00,
            project_id=1
        ), use_decimal=True),
        headers=headers
    )
    client.post(
        '/api/funds',
        data=json.dumps(dict(
            name='Blanco Loan',
            loan=True,
            amount=330000.00,
            project_id=1
        ), use_decimal=True),
        headers=headers
    )

    client.post(
        '/api/draws',
        data=json.dumps(dict(
            date='09/24/2015',
            amount=25000.00,
            fund_id=2
        ), use_decimal=True),
        headers=headers
    )
    client.post(
        '/api/draws',
        data=json.dumps(dict(
            date='10/01/2015',
            amount=5000.00,
            fund_id=2
        ), use_decimal=True),
        headers=headers
    )
    client.post(
        '/api/draws',
        data=json.dumps(dict(
            date='10/03/2015',
            amount=7500.00,
            fund_id=2
        ), use_decimal=True),
        headers=headers
    )

    expenditure_list = parse_invoice_file(FILE_PATH)

    for expenditure in expenditure_list:
        fund_id = 1
        if expenditure['notes'] == 'Blanco':
            fund_id = 2

        client.post(
            '/api/expenditures',
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

    client.post(
        '/api/subcontractors',
        data=json.dumps(dict(
            company='84 Lumber',
            person='John Smith',
            number='210-543-4534',
            project_id=1
        )),
        headers=headers
    )
    client.post(
        '/api/subcontractors',
        data=json.dumps(dict(
            company='Ez Company',
            person='Shawn Tarver',
            number='512-586-6516',
            project_id=1
        )),
        headers=headers
    )
    client.post(
        '/api/subcontractors',
        data=json.dumps(dict(
            company='Coca Cola',
            person='Mike Jones',
            number='210-253-5861',
            project_id=1
        )),
        headers=headers
    )
