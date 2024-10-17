from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin as sm

db = SQLAlchemy()

class Doctor(db.Model, sm):
    __tablename__ = "doctors"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    doctorId = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email= db.Column(db.String)
    bio = db.Column(db.String)
    education = db.Column(db.String)
    certifications = db.Column(db.String)
    achievements = db.Column(db.String)
    image = db.Column(db.String)
    password = db.Column(db.String)
    
    
    def __repr__(self):
        return f'<User {self.first_name}, {self.last_name}, {self.email}, >'
 
