#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app.api.stripe
    ~~~~~~~~~~~~~~

    This API is used for connecting with Stripe.
"""

import stripe
from flask import request, make_response, jsonify
from flask_mail import Message

from app import app, db, mail
from app.models import User


URL = '/api/stripe'


@app.route(URL, methods=['POST'])
def create():
    """
    Creates a Stripe subscription.

    Request Example:
    POST
    {
        email    : 'email address'
        username : 'username'
        password : 'password'
        plan     : 'subscription plan'
        token_id : 'stripe card token id'
    }
    """
    data      = request.get_json(force=True)
    email     = data.get('email', None)
    username  = data.get('username', None)
    password  = data.get('password', None)
    plan      = data.get('plan', None)
    token_id  = data.get('token_id', None)
    criterion = [email, username, password, plan, token_id, len(data) == 5]

    if not all(criterion):
        return make_response('Bad request', 400)

    try:
        customer = stripe.Customer.create(
            email=email,
            plan=plan,
            source=token_id
        )
        user = User(
            email=email,
            username=username,
            password=password,
            stripe_id=customer['id']
        )
        db.session.add(user)
        db.session.commit()
        # msg = Message('Thank you from BuildersRecords', recipients=[email])
        # msg.html = render_template('mail/registration.html')
        # mail.send(msg)
        return make_response(jsonify(customer), 201)

    except stripe.error.CardError:
        return make_response('Card declined', 400)

    except stripe.error.RateLimitError:
        return make_response('Too many requests made to Stripe', 400)

    except stripe.error.InvalidRequestError:
        return make_response('Invalid parameters were supplied to Stripe', 400)

    except stripe.error.AuthenticationError:
        return make_response('Authentication with Stripe failed', 400)

    except stripe.error.APIConnectionError:
        return make_response('Network communication with Stripe failed', 400)

    except stripe.error.StripeError:
        return make_response('Stripe Error', 400)

    except Exception:
        return make_response('Error', 400)


# Needs route security
@app.route(URL + '/<stripe_id>', methods=['GET'])
def retrieve(stripe_id):
    """
    Gets a Stripe subscription.
    """
    customer = stripe.Customer.retrieve(stripe_id)

    if customer is None:
        return make_response('Could not retrieve customer', 400)

    return make_response(jsonify(customer), 200)


# Needs route security
@app.route(URL + '/<stripe_id>', methods=['PUT'])
def update(stripe_id):
    """
    Updates a Stripe subscription.

    Request Example:
    PUT
    {
        stripe_id : 'stripe customer id'
        token_id  : 'stripe card token id'
    }
    """
    data      = request.get_json(force=True)
    stripe_id = data.get('stripe_id', None)
    token_id  = data.get('token_id', None)
    criterion = [stripe_id, token_id, len(data) == 2]

    if not all(criterion):
        return make_response('Bad request', 400)

    try:
        customer = stripe.Customer.retrieve(stripe_id)

        if customer is None:
            return make_response('Could not retrieve customer', 400)

        customer.source = token_id
        customer.save()
        return make_response(jsonify(customer), 200)

    except stripe.error.CardError:
        return make_response('Card declined', 400)

    except stripe.error.RateLimitError:
        return make_response('Too many requests made to Stripe', 400)

    except stripe.error.InvalidRequestError:
        return make_response('Invalid parameters were supplied to Stripe', 400)

    except stripe.error.AuthenticationError:
        return make_response('Authentication with Stripe failed', 400)

    except stripe.error.APIConnectionError:
        return make_response('Network communication with Stripe failed', 400)

    except stripe.error.StripeError:
        return make_response('Stripe Error', 400)

    except Exception:
        return make_response('Error', 400)
