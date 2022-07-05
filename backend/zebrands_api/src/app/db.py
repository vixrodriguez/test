import json
from . import db


class BaseJSON:
    def to_json(self):
        result = self.__dict__.copy()
        del result['_sa_instance_state']
        return result


class UserBase:
    def __init__(self, id, username, password):
        self.id = str(id)
        self.username = username
        self.password = password


class Brands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    products = db.relationship("Products")
    active = db.Column(db.Boolean, default=True)

    @staticmethod
    def get_all():
        return db.session.query()

    @staticmethod
    def insert(kwargs):
        if kwargs:
            brand = Brands(**kwargs)
            db.session.add(brand)
            db.session.commit()
            return brand
        else:
            return False


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sku = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    count_query = db.Column(db.Integer, default=0)
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))
    active = db.Column(db.Boolean, default=True)

    @staticmethod
    def get_all():
        return db.session.query(Products).all()


class UsersTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    @staticmethod
    def insert(kwargs):
        if kwargs:
            user_types = UsersTypes(**kwargs)
            db.session.add(user_types)
            db.session.commit()
            return user_types
        else:
            return False


class Users(db.Model, BaseJSON):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey("users_types.id"))
    active = db.Column(db.Boolean, default=True)

    @staticmethod
    def insert(kwargs):
        if kwargs:
            user = Users(**kwargs)
            db.session.add(user)
            db.session.commit()
            return user
        else:
            return False

    @staticmethod
    def get_auth_user(username, password):
        user = Users.query.filter_by(username=username, password=password, active=True).first()
        return user if user else False

    @staticmethod
    def find_by_id(id):
        user = Users.query.filter_by(id=id)
        return user if user else False


class Audit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String, nullable=False)
    uri = db.Column(db.String, nullable=False)
    resource_id = db.Column(db.Integer, nullable=False)
    resource_name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    # def to_json(self):
    #     result = self.__dict__.copy()
    #     del result['_sa_instance_state']
    #     return result

    @staticmethod
    def get_all(raw=False):
        result = db.session.query(Audit).all()
        if not raw:
            return [r.to_json() for r in result]
        else:
            return result

    @staticmethod
    def insert(kwargs):
        if kwargs:
            audit = Audit(**kwargs)
            db.session.add(audit)
            db.session.commit()
            return audit
        else:
            return False

db.create_all()


# User Types

UsersTypes.insert({'name': 'admin'})
UsersTypes.insert({'name': 'anonymous'})

# User
Users.insert({
    'name': 'Admin',
    'username': 'admin',
    'password': '1234',
    'email': 'admin@example.com',
    'user_type_id': 1
})