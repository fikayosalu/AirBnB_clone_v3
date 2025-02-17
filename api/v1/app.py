#!/usr/bin/python3
"""Create a JSON 404 error page."""


from flask import Flask, jsonify, make_response


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    """Returns a JSON-formatted 404 status code."""
    return make_response(jsonify({'error': 'Not found'}), 404)
