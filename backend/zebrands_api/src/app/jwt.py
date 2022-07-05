from .db import Users, UserBase

# JWT


def autenticate(username, password):
    user = Users.get_auth_user(username, password)
    if user:
        user_base = UserBase(user.id, user.username, user.password)
        return user_base


def identity(payload):
    user_id = payload['identity']
    user = Users.find_by_id(id=user_id).first()
    return user if user else False
