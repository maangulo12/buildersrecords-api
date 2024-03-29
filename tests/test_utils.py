# -*- coding: utf-8 -*-
"""
    tests.test_utils
    ~~~~~~~~~~~~~~~~

    This module contains the utility functions for testing.
"""

from flask import json


def safe_json(**kwargs):
    """Creates a safe JSON object"""
    return json.dumps(dict(kwargs))


def get_token(rv):
    """Returns a token from the authentication response"""
    d = json.loads(rv.data)
    return d['token']
