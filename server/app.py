from flask import Flask, request, session, jsonify, current_app, url_for
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask import Flask, request, session, jsonify, current_app, url_for
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Doctor
from werkzeug.utils import secure_filename
import os

# Flask app setup
app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.json.compact = False

# Initialize extensions
migrate = Migrate(app, db)
api = Api(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:4000"}})

# Initialize database
db.init_app(app)

# Doctor Signup Resource
class DoctorSignup(Resource):
    def post(self):
        data = request.form  # Get form data

        # Get the uploaded image
        image = request.files.get('image')

        # Ensure an image was uploaded
        if image:
            # Secure the filename and save the image in the static folder
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
        else:
            image_path = None

        # Create a new doctor instance
        new_doctor = Doctor(
            title=data.get('title'),
            doctorId=data.get('doctorId'),  # Generate a unique doctor ID for each new doctor
            first_name=data.get('firstName'),
            last_name=data.get('lastName'),
            email=data.get('email'),
            bio=data.get('bio'),
            education=data.get('education'),
            certifications=data.get('certifications'),
            achievements=data.get('achievements'),
            image=image_path,  # Store the image path
            password=bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
        )

        try:
            # Add the doctor to the database and commit
            db.session.add(new_doctor)
            db.session.commit()
            return new_doctor.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

# Doctor Login Resource
class DoctorLogin(Resource):
        data = request.form  # Get form data

        # Get the uploaded image
        image = request.files.get('image')

        # Ensure an image was uploaded
        if image:
            # Secure the filename and save the image in the static folder
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
        else:
            image_path = None

        # Create a new doctor instance
        new_doctor = Doctor(
            title=data.get('title'),
            doctorId=data.get('doctorId'),  # Generate a unique doctor ID for each new doctor
            first_name=data.get('firstName'),
            last_name=data.get('lastName'),
            email=data.get('email'),
            bio=data.get('bio'),
            education=data.get('education'),
            certifications=data.get('certifications'),
            achievements=data.get('achievements'),
            image=image_path,  # Store the image path
            password=bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
        )

        try:
            # Add the doctor to the database and commit
            db.session.add(new_doctor)
            db.session.commit()
            return new_doctor.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

# Doctor Login Resource
class DoctorLogin(Resource):
    def post(self):
        data = request.get_json()  # Get JSON data
        doctor = Doctor.query.filter_by(email=data['email']).first()

        # Verify password
        if doctor and bcrypt.check_password_hash(doctor.password, data['password']):
            session['user_id'] = doctor.id
            return {
                "message": "Login successful",
                "data": doctor.to_dict(only=('id', 'title', 'first_name', 'last_name', 'email', 'bio', 'education', 'certifications', 'achievements', 'image')),
                "status": 200
            }, 200
        else:
            return {"error": "Invalid credentials"}, 401

# Logout Resource
class Logout(Resource):
    def delete(self):
        session.pop('user_id', None)
        return {"message": "Logged out Successfully!"}, 204

# Check Session Resource
class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')

        if user_id:
            doctor = Doctor.query.get(user_id)
            if doctor:
                return doctor.to_dict(), 200
            else:
                return {"error": "User not found"}, 404
        return {"error": "Unauthorized"}, 401

# API Resource Routing
api.add_resource(DoctorSignup, '/doctorsignup', endpoint='doctorsignup')
api.add_resource(DoctorLogin, '/doctorlogin', endpoint='doctorlogin')
api.add_resource(Logout, '/logout', endpoint=None)
api.add_resource(CheckSession, '/check_session', endpoint='check_session')

# Run the application
# Run the application
if __name__ == "__main__":
    app.run(port=5555, debug=True)