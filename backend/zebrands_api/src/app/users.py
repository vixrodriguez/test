from .import app


@app.route('/users', methods=['GET'])
def query_user():
    return 'Users'


@app.route('/users', methods=['POST'])
def create_user():
    pass


@app.route('/users', methods=['PUT'])
def update_user():
    pass


@app.route('/users', methods=['DELETE'])
def delete_user():
    pass
