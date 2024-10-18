from models import Patient, Appointment, Doctor, Department, db
from datetime import datetime
from app import app, bcrypt
from faker import Faker
import random

faker = Faker()


with app.app_context():
    print("Clearing db ...")
    Doctor.query.delete()
    Patient.query.delete()
    Department.query.delete()
    Appointment.query.delete()
    
    print("Seeding Doctor data...")

    doctors_data = [
        # Emergency Department (Department 1)
        { 'name': 'Dr. Michael Ndungu', 'specialty': 'Emergency Physician', 'image': 'images/Dr45.jpg', 'department_id': 1 },
        { 'name': 'Dr. Sarah Onyango', 'specialty': 'Trauma Surgeon', 'image': 'images/Dr46.jpg', 'department_id': 1 },
        { 'name': 'Dr. James Wambui', 'specialty': 'Emergency Physician', 'image': 'images/Dr47.jpg', 'department_id': 1 },
        { 'name': 'Dr. Linda Njoroge', 'specialty': 'Critical Care Specialist', 'image': 'images/Dr48.jpg', 'department_id': 1 },
        { 'name': 'Dr. Peter Mwangi', 'specialty': 'Emergency Physician', 'image': 'images/Dr49.jpg', 'department_id': 1 },
        { 'name': 'Dr. Nancy Omondi', 'specialty': 'Emergency Physician', 'image': 'images/Dr50.jpg', 'department_id': 1 },
        
        # Cardiology (Department 2)
        { 'name': 'Dr. John Kamau', 'specialty': 'Cardiologist', 'image': 'images/Dr1.jpg','department_id': 2 },
        { 'name': 'Dr. Jane Mwangi', 'specialty': 'Cardiologist', 'image': 'images/Dr2.jpg', 'department_id': 2 },
        { 'name': 'Dr. Allan Wekesa', 'specialty': 'Cardiologist', 'image': 'images/Dr3.jpg','department_id': 2 },
        { 'name': 'Dr. Susan Otieno', 'specialty': 'Cardiologist', 'image': 'images/Dr4.jpg','department_id': 2 },

        # Neurology (Department 3)
        { 'name': 'Dr. Peter Odhiambo', 'specialty': 'Neurologist', 'image': 'images/Dr5.jpg','department_id': 3 },
        { 'name': 'Dr. Ann Wanjiru', 'specialty': 'Neurologist', 'image': 'images/Dr6.jpg', 'department_id': 3 },
        { 'name': 'Dr. David Maina', 'specialty': 'Neurologist', 'image': 'images/Dr7.jpg','department_id': 3 },
        { 'name': 'Dr. Angela Mwangi', 'specialty': 'Neurologist', 'image': 'images/Dr8.jpg','department_id': 3 },

        # Pediatrics (Department 4)
        { 'name': 'Dr. Sarah Njeri', 'specialty': 'Pediatrician', 'image': 'images/Dr21.jpg','department_id': 4 },
        { 'name': 'Dr. Richard Kamau', 'specialty': 'Pediatrician', 'image': 'images/Dr22.jpg', 'department_id': 4 },
        { 'name': 'Dr. Fiona Wambui', 'specialty': 'Pediatrician', 'image': 'images/Dr23.jpg','department_id': 4 },
        { 'name': 'Dr. Kevin Otieno', 'specialty': 'Pediatrician', 'image': 'images/Dr24.jpg','department_id': 4 },

        # Orthopedics (Department 5)
        { 'name': 'Dr. Samuel Otieno', 'specialty': 'Orthopedic Surgeon', 'image': 'images/Dr9.jpg','department_id': 5 },
        { 'name': 'Dr. Lucy Wanjiru', 'specialty': 'Orthopedic Surgeon', 'image': 'images/Dr10.jpg', 'department_id': 5 },
        { 'name': 'Dr. Anthony Mburu', 'specialty': 'Orthopedic Surgeon', 'image': 'images/Dr11.jpg','department_id': 5 },

        # Gynecology (Department 6)
        { 'name': 'Dr. Jack Mwangi', 'specialty': 'Gynecologist', 'image': 'images/Dr38.jpg','department_id': 6 },
        { 'name': 'Dr. Carol Njeri', 'specialty': 'Gynecologist', 'image': 'images/Dr39.jpg', 'department_id': 6 },

        # General Surgery (Department 7)
        { 'name': 'Dr. Michael Wekesa', 'specialty': 'General Surgeon', 'image': 'images/Dr25.jpg','department_id': 7 },
        { 'name': 'Dr. Evelyn Wanjiru', 'specialty': 'General Surgeon', 'image': 'images/Dr26.jpg', 'department_id': 7 },
        { 'name': 'Dr. Charles Mburu', 'specialty': 'General Surgeon', 'image': 'images/Dr27.jpg','department_id': 7 },

    ]

    # Seed data into the database
    for doctor_data in doctors_data:
        doctor = Doctor(
            title="Dr.",
            doctorId=faker.random_number(digits=7, fix_len=True),
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            bio=faker.text(),
            education=faker.text(),
            certifications=faker.text(),
            image=doctor_data['image'],
            specialty=doctor_data['specialty'],
            department_id=doctor_data['department_id'],
            password=bcrypt.generate_password_hash('1234Abcd').decode('utf-8')
        )
        db.session.add(doctor)

    db.session.commit()

    print("Seeding Patient data...")
    
    patients = []
    genders = ['Male', 'Female', 'Other']
    used_emails = set() 
    for _ in range(100):
        email = faker.email()
        while email in used_emails: 
            email = faker.email()
        used_emails.add(email)

        patient = Patient(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            age=faker.random_int(18, 99),
            gender=random.choice(genders),
            email=email,
            phone_number=faker.phone_number(),
            password=bcrypt.generate_password_hash('1234Abcd').decode('utf-8')
        )
        patients.append(patient)
    db.session.add_all(patients)
    db.session.commit()
    
    print("Seeding Department data...")

    departments_data = [
        { 'name': 'Emergency', 'image': 'images/emergency.jpg' },
        { 'name': 'Cardiology', 'image': 'images/cardiology.jpg' },
        { 'name': 'Neurology', 'image': 'images/neurology.jpg' },
        { 'name': 'Pediatrics', 'image': 'images/pediatrics.jpg' },
        { 'name': 'Orthopedics', 'image': 'images/orthopedics.jpg' },
        { 'name': 'Gynecology', 'image': 'images/gynecology.jpg' },
        { 'name': 'General Surgery', 'image': 'images/general_surgery.jpg' },
        { 'name': 'Optometry', 'image': 'images/optometry.jpg' },
        { 'name': 'Radiology', 'image': 'images/radiology.jpg' },
        { 'name': 'ENT', 'image': 'images/ent.jpg' },
        { 'name': 'Oncology', 'image': 'images/oncology.jpg' },
        { 'name': 'Urology', 'image': 'images/urology.jpg' },
        { 'name': 'Dentistry', 'image': 'images/dentistry.jpg' },
        { 'name': 'Dermatology', 'image': 'images/dermatology.jpg' },
        { 'name': 'Nephrology', 'image': 'images/nephrology.jpg' },
        { 'name': 'Psychiatry', 'image': 'images/psychiatry.jpg' },
    ]

    # Seed data into the database
    for department_data in departments_data:
            department = Department(
                name=department_data['name'],
                description=faker.text(),
                image=department_data['image']
            )
            db.session.add(department)

    db.session.commit()

    print("Seeding Appointment data...")
    appointments = []
    for _ in range(100):
        
        time_str = faker.time()  
        time_obj = datetime.strptime(time_str, '%H:%M:%S').time()

        appointment = Appointment(
            date=faker.date_this_year(),
            time=time_obj,  
            medical_records=faker.text(),
            patient_id=random.randint(1, 100),
            doctor_id=random.randint(1, 50)
        )
        appointments.append(appointment)  

    
    db.session.add_all(appointments)
    db.session.commit()
    
    print("Database seeded successfully!")
    
