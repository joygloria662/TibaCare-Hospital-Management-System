from flask_sqlalchemy import SQLAlchemy
from config import bcrypt, db
from sqlalchemy_serializer import SerializerMixin as sm


class User(db.Model, sm):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email= db.Column(db.String)
    age= db.Column(db.String)
    role= db.Column(db.String)
    _password_hash= db.Column(db.String)
    
    @property
    def password_hash(self):
        raise Exception('Password hashes must not be viewed.')
    
    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)
    
    
    def __repr__(self):
        return f'<User {self.first_name}, {self.last_name}, {self.email}, {self.age}, {self.role}>'
    
