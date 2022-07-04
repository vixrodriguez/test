from . import app
from .db import Products
from .db import Audit
from flask import request


@app.route('/products', methods=['GET'])
def query_product():
    Audit.insert({'action': 'GET',
                  'uri': request.url,
                  'resource_id': 1,
                  'resource_name': 'products',
                  'user_id': 1
                  })
    return str(Products.get_all())


@app.route('/products', methods=['POST'])
def create_product():
    pass


@app.route('/products', methods=['PUT'])
def update_product():
    pass


@app.route('/products', methods=['DELETE'])
def delete_product():
    pass
