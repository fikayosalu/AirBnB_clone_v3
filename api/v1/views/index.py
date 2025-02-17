#!/usr/bin/python3
""" Set up response for status code """
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def response_status():
    """ Return status of the API """
    return jsonify({"status": "OK"})
