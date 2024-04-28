#!/usr/bin/python3
"""
Defines routes for basic index operations of the API.
This module contains the route definitions for status checks
and other basic API operations.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API.
    Endpoint: GET /api/v1/status
    Returns:
        JSON response with the status of the API.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieves the number of each object type."""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
