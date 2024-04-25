#!/usr/bin/python3
"""
Defines routes for basic index operations of the API.
This module contains the route definitions for status checks
and other basic API operations.
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API.
    Endpoint: GET /api/v1/status
    Returns:
        JSON response with the status of the API.
    """
    return jsonify({"status": "OK"})
