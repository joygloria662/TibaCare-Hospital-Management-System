
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin as sm
import datetime 
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

class Patient(db.Model, sm):
    __tablename__ = 'patients'

    serialize_rules = ("-appointments.patient",)

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    appointments = db.relationship("Appointment", back_populates="patient")
    doctors = association_proxy("appointments", "doctor", creator=lambda doctor_obj: Appointment(doctor=doctor_obj))

    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name} {self.email}>"

class Appointment(db.Model, sm):
    __tablename__ = 'appointments'

    serialize_rules = ("-patient.appointments", "-doctor.appointments",)

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    medical_records = db.Column(db.String, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"))
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"))

    patient = db.relationship("Patient", back_populates="appointments")
    doctor = db.relationship("Doctor", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment {self.patient_id} {self.doctor_id}>"

class Department(db.Model, sm):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    doctors = db.relationship("Doctor", back_populates="department")

    def __repr__(self):
        return f"<Department {self.name}>"

class Doctor(db.Model, sm):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    specialization = db.Column(db.String, nullable=False)

    appointments = db.relationship("Appointment", back_populates="doctor")
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    department = db.relationship("Department", back_populates="doctors")
    patients = association_proxy("appointments", "patient", creator=lambda patient_obj: Appointment(patient=patient_obj))

    def __repr__(self):
        return f"<Doctor {self.first_name} {self.last_name}>"

