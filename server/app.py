from flask import Flask, request, session, make_response
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Doctor, Department, Patient, Appointment
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.json.compact = False

migrate = Migrate(app, db)
api = Api(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:4000"}})


db.init_app(app)

class DoctorSignup(Resource):
    def post(self):
        data = request.form
        image = request.files.get('image')

        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
        else:
            image_path = None
            
        new_doctor = Doctor(
            title=data.get('title'),
            doctorId=data.get('doctorId'),
            first_name=data.get('firstName'),
            last_name=data.get('lastName'),
            email=data.get('email'),
            bio=data.get('bio'),
            education=data.get('education'),
            certifications=data.get('certifications'),
            specialty=data.get('specialty'),
            image=image_path,
            department_id = data.get('department'),
            password=bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
        )

        try:
            db.session.add(new_doctor)
            db.session.commit()
            return new_doctor.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

class DoctorLogin(Resource):
    def post(self):
        data = request.get_json() 
        doctor = Doctor.query.filter_by(email=data['email']).first()

        if doctor and bcrypt.check_password_hash(doctor.password, data['password']):
            session['user_id'] = doctor.id
            session['user_role'] = 'doctor'
            return {
                "message": "Login successful",
                "data": doctor.to_dict(),
                "status": 200
            }
        else:
            return {"error": "Invalid credentials"}, 401
        
class PatientSignup(Resource):
    def post(self):
        data = request.form
           
        new_patient = Patient(
            first_name=data.get('firstName'),
            last_name=data.get('lastName'),
            email=data.get('email'),
            age=data.get('age'),
            phone_number=data.get('phoneNumber'),
            gender = data.get('gender'),
            password=bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
        )

        try:
            db.session.add(new_patient)
            db.session.commit()
            return new_patient.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

class PatientLogin(Resource):
    def post(self):
        data = request.get_json() 
        
        patient = Patient.query.filter_by(email=data['email']).first()

        if patient and bcrypt.check_password_hash(patient.password, data['password']):
            session['user_id'] = patient.id
            session['user_role'] = 'patient'
            
            return {
                    "message": "Login successful",
                    "data": patient.to_dict(),
                }, 200
        else:
            return {"error": "Invalid email or password"}, 401



class Logout(Resource):
    def delete(self):
        session.pop('user_id', None)
        return {"message": "Logged out Successfully!"}, 204

# Check Session Resource
class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        user_role = session.get('user_role')

        if user_id and user_role:
            if user_role == 'doctor':
                user = Doctor.query.get(user_id)
            elif user_role == 'patient':
                user = Patient.query.get(user_id)
                user = None  
            if user:
                return {
                    "user": user.to_dict(),
                    "role": user_role 
                }, 200
            else:
                return {"error": "User not found"}, 404
        return {"error": "Unauthorized"}, 401

class DepartmentList(Resource):
    def get(self):
        departments_dict =[department.to_dict() for department in Department.query.all()]
        
        return make_response(departments_dict, 200)
        


api.add_resource(DoctorSignup, '/doctorsignup', endpoint='doctorsignup')
api.add_resource(DoctorLogin, '/doctorlogin', endpoint='doctorlogin')
api.add_resource(Logout, '/logout', endpoint=None)
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(DepartmentList, '/departments', endpoint='departments')
api.add_resource(PatientSignup, '/patientsignup', endpoint='patientsignup')
api.add_resource(PatientLogin, '/patientlogin', endpoint='patientlogin')



if __name__ == "__main__":
    app.run(port=5555)
