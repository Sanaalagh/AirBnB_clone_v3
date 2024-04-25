#!/usr/bin/python3
"""
Flask application setup for API version 1
This module initializes the Flask application,
registers API endpoints, and defines the main entry point.
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """Custom 404 Not found error handler."""
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
