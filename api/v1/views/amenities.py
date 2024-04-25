#!/usr/bin/python3
"""
Amenity API Endpoints
Defines endpoints for managing Amenity objects via RESTful API methods.
"""
from flask import jsonify, abort, request, make_response
from models import storage, Amenity
from api.v1.views import app_views


@app_views.route(
        '/amenities', methods=['GET'], strict_slashes=False)
def get_all_amenities():
    """ Retrieves the list of all Amenity objects """
    all_amenities = [
            amenity.to_dict() for amenity in storage.all(Amenity).values()]
    return jsonify(all_amenities)


@app_views.route(
        '/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """ Retrieves a specific Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route(
        '/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """ Deletes a specific Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route(
        '/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """ Creates an Amenity """
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    new_amenity = Amenity(**request.get_json())
    storage.new(new_amenity)
    storage.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route(
        '/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """ Updates an Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    ignore_keys = ["id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
