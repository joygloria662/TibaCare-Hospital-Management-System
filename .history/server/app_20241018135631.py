from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api,Resource

from models import db, Patient
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
api = Api(app)
bcrypt = Bcrypt(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:4000"}})

db.init_app(app)



class Signup(Resource):
    def post(self):
        new_user = User(
            first_name = request.json['firstname'],
            last_name = request.json['lastname'],
            email = request.json['email'],
            age = request.json['age'],
            role = request.json['role'],           
        )
        new_user.password_hash = request.json['password']
        
        db.session.add(new_user)
        db.session.commit()
        
        return new_user.to_dict(), 201
        
    
class Login(Resource):
    def post(self):
        
        email = request.json['email']
        password = request.json['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.authenticate(password):
            session['user_id'] = user.id      
            return user.to_dict(), 200
        return {
            'error': 'Invalid email or password'
        }, 401
        
api.add_resource(Login, '/login')
api.add_resource(Signup, '/signup')



if __name__ == "__main__":
    app.run(port=5555, debug=True)
