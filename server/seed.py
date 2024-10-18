from datetime import date, time
from config import db, app  # Assuming you have db and app configured in config.py
from models import Patient, Appointment  # Assuming models.py contains your models
from random import randint
from faker import Faker

# Create a Faker instance to generate random data
faker = Faker()


with app.app_context():
    print("Clearing db ...")
    
    User.query.delete
    
    print("Seeding user data")
    
    roles = ["Doctor", "Patient"]
    
    users = []
    
    for _ in range(20):
        user = User(
            first_name = fake.name(),
            last_name = fake.name(),
            email = fake.email(),
            age = random.randint(18, 70),
            role = random.choice(roles),
            password = bcrypt.generate_password_hash(fake.word()).decode('utf-8')
        )
        
        users.append(user)
    db.session.add_all(users)
    db.session.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():  # Ensure app context is active
        seed_database()
