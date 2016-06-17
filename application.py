#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    wsgi.py
    ~~~~~~~

    Run this module to run the application.

    HOW TO USE:
    - Type the following in the command-line
      python3 wsgi.py
"""

from app import app


if __name__ == '__main__':
    app.run(host=app.config['SERVER_HOST'], port=app.config['SERVER_PORT'])
