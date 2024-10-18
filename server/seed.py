from config import app, bcrypt, db
from models import User
import random
from faker import Faker

fake = Faker()


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
    
    print("Seeding Complete!")
    