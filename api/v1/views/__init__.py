#!/usr/bin/python3
"""
Initialize the views package for API version 1.
This package contains modules for defining
the API endpoints and their routes.
"""
from flask import Blueprint

# Create a Blueprint named 'app_views'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all view modules here to register their routes
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.places import *
from api.v1.views.users import *
from api.v1.views.places_reviews import *
