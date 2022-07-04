from . import app
from .db import Audit
from flask import jsonify
from flask import request


@app.route('/logs', methods=['GET'])
def query_audit():
    logs = Audit.get_all()
    return jsonify(results=logs)
