#!/usr/bin/python3
"""
Index module for the API.
"""

import models
from models import storage
from models.base_model import BaseModel
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
     """
    Get the status of the API.
    """
    return jsonify({"status": "OK"})
