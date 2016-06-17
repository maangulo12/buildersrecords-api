# -*- coding: utf-8 -*-
"""
    app.admin
    ~~~~~~~~~

    This module implements the Admin interface of this application.
"""

from flask_admin.contrib.sqla import ModelView

from app import ad, db
from app.models import User, Project, Category, Item, Expenditure, Fund, Draw, Subcontractor


# Add views for every model
ad.add_view(ModelView(User, db.session))
ad.add_view(ModelView(Project, db.session))
ad.add_view(ModelView(Category, db.session))
ad.add_view(ModelView(Item, db.session))
ad.add_view(ModelView(Expenditure, db.session))
ad.add_view(ModelView(Fund, db.session))
ad.add_view(ModelView(Draw, db.session))
ad.add_view(ModelView(Subcontractor, db.session))
