#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    BuildersRecords API
    ~~~~~~~~~~~~~~~~~~~~
    :copyright: (c) 2016

    This module runs the application.

    HOW TO USE:
    - Type the following in the command-line
      python3 application.py
"""

from app import app


if __name__ == '__main__':
    app.run(host=app.config['SERVER_HOST'], port=app.config['SERVER_PORT'])
