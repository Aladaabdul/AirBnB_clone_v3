#!/usr/bin/python3
"""create route that return OK

"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status", methods=['GET'])
def api_status():
    """ return JSON status: "OK"
    
    """
    response = {"status": "OK"}
    return jsonify(response)
