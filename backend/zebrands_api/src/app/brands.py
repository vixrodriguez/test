from . import app
from .db import Brands


@app.route('/brands', methods=['GET'])
def query_brand():
    return str(Brands.get_all())


@app.route('/brands', methods=['POST'])
def create_brand():
    pass


@app.route('/brands', methods=['PUT'])
def update_brand():
    pass


@app.route('/brands', methods=['DELETE'])
def delete_brand():
    pass
