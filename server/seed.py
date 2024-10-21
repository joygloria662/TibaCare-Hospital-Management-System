from models import Patient, Appointment, Doctor, Department, db
from datetime import datetime
from app import app, bcrypt
from faker import Faker
import random

faker = Faker()


# Sample detailed doctor profiles
doctors_profiles = [
    {
        "title": "Dr.",
        "doctorId": "DOC001",
        "first_name": "Regina",
        "last_name": "Hicks",
        "email": "regina.hicks@example.com",
        "bio": "Experienced cardiologist with a passion for heart health.",
        "education": "MD, Johns Hopkins University, Class of 2018",
        "certifications": "Board Certified in Internal Medicine and Cardiology",
        "specialty": "Cardiologist",
        "image": "images/Dr4.jpg",
        "department_id": 2,
        "years_of_experience": 5,
        "achievements": "Involved in groundbreaking research on heart disease prevention."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC002",
        "first_name": "Michael",
        "last_name": "Ndungu",
        "email": "michael.ndungu@example.com",
        "bio": "Emergency physician with extensive experience in trauma care.",
        "education": "MD, University of Nairobi, Class of 2011",
        "certifications": "Board Certified in Emergency Medicine",
        "specialty": "Emergency Physician",
        "image": "images/Dr45.jpg",
        "department_id": 1,
        "years_of_experience": 12,
        "achievements": "Led multiple emergency response initiatives, published 5 peer-reviewed articles."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC003",
        "first_name": "Sarah",
        "last_name": "Onyango",
        "email": "sarah.onyango@example.com",
        "bio": "Expert trauma surgeon dedicated to improving patient outcomes.",
        "education": "MD, Kenyatta University, Class of 2015",
        "certifications": "Fellowship in Trauma Surgery",
        "specialty": "Trauma Surgeon",
        "image": "images/Dr46.jpg",
        "department_id": 1,
        "years_of_experience": 8,
        "achievements": "Developed a surgical technique now adopted nationally, recipient of the Best Surgical Resident Award."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC004",
        "first_name": "James",
        "last_name": "Wambui",
        "email": "james.wambui@example.com",
        "bio": "Skilled emergency physician with a focus on patient care.",
        "education": "MD, Moi University, Class of 2018",
        "certifications": "Advanced Trauma Life Support Certification",
        "specialty": "Emergency Physician",
        "image": "images/Dr47.jpg",
        "department_id": 1,
        "years_of_experience": 5,
        "achievements": "Implemented a new triage protocol that improved patient intake times."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC005",
        "first_name": "Linda",
        "last_name": "Njoroge",
        "email": "linda.njoroge@example.com",
        "bio": "Critical care specialist with a commitment to excellence in patient care.",
        "education": "MD, University of Medicine, Class of 2013",
        "certifications": "Certified in Critical Care Medicine",
        "specialty": "Critical Care Specialist",
        "image": "images/Dr48.jpg",
        "department_id": 1,
        "years_of_experience": 10,
        "achievements": "Pioneered a community health program for critical care, recognized for excellence in patient care."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC006",
        "first_name": "Peter",
        "last_name": "Mwangi",
        "email": "peter.mwangi@example.com",
        "bio": "Dedicated emergency physician with training in lifesaving techniques.",
        "education": "MD, University of Nairobi, Class of 2017",
        "certifications": "Basic Life Support Certification",
        "specialty": "Emergency Physician",
        "image": "images/Dr49.jpg",
        "department_id": 1,
        "years_of_experience": 6,
        "achievements": "Developed training modules for emergency response teams."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC007",
        "first_name": "Nancy",
        "last_name": "Omondi",
        "email": "nancy.omondi@example.com",
        "bio": "Emergency physician passionate about community health education.",
        "education": "MD, Jomo Kenyatta University, Class of 2019",
        "certifications": "Emergency Medical Technician Certification",
        "specialty": "Emergency Physician",
        "image": "images/Dr50.jpg",
        "department_id": 1,
        "years_of_experience": 4,
        "achievements": "Actively involved in outreach programs for emergency preparedness."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC008",
        "first_name": "John",
        "last_name": "Kamau",
        "email": "john.kamau@example.com",
        "bio": "Experienced cardiologist with a focus on patient-centered care.",
        "education": "MD, Harvard Medical School, Class of 2008",
        "certifications": "Fellow of the American College of Cardiology",
        "specialty": "Cardiologist",
        "image": "images/Dr1.jpg",
        "department_id": 2,
        "years_of_experience": 15,
        "achievements": "Published multiple articles on cardiac health, recognized for innovative research."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC009",
        "first_name": "Jane",
        "last_name": "Mwangi",
        "email": "jane.mwangi@example.com",
        "bio": "Cardiologist known for introducing groundbreaking cardiac programs.",
        "education": "MD, Stanford University, Class of 2014",
        "certifications": "Board Certified in Cardiology",
        "specialty": "Cardiologist",
        "image": "images/Dr2.jpg",
        "department_id": 2,
        "years_of_experience": 9,
        "achievements": "Introduced a cardiac rehabilitation program that improved patient outcomes."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC010",
        "first_name": "Allan",
        "last_name": "Wekesa",
        "email": "allan.wekesa@example.com",
        "bio": "Cardiologist committed to community service and health education.",
        "education": "MD, University of California, Class of 2016",
        "certifications": "Advanced Cardiac Life Support Certification",
        "specialty": "Cardiologist",
        "image": "images/Dr3.jpg",
        "department_id": 2,
        "years_of_experience": 7,
        "achievements": "Conducted seminars on heart health awareness, recognized for community service."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC011",
        "first_name": "Susan",
        "last_name": "Otieno",
        "email": "susan.otieno@example.com",
        "bio": "Innovative cardiologist with a passion for preventative care.",
        "education": "MD, Johns Hopkins University, Class of 2018",
        "certifications": "Board Certified in Internal Medicine and Cardiology",
        "specialty": "Cardiologist",
        "image": "images/Dr4.jpg",
        "department_id": 2,
        "years_of_experience": 5,
        "achievements": "Involved in groundbreaking research on heart disease prevention."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC012",
        "first_name": "David",
        "last_name": "Karanja",
        "email": "david.karanja@example.com",
        "bio": "Pediatrician focused on child development and wellness.",
        "education": "MD, University of Nairobi, Class of 2012",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr5.jpg",
        "department_id": 4,
        "years_of_experience": 11,
        "achievements": "Established a child wellness program that has served over 1000 families."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC013",
        "first_name": "Joyce",
        "last_name": "Adhiambo",
        "email": "joyce.adhiambo@example.com",
        "bio": "Pediatrician with a special interest in childhood obesity.",
        "education": "MD, Kenyatta University, Class of 2014",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr6.jpg",
        "department_id": 4,
        "years_of_experience": 9,
        "achievements": "Published research on childhood obesity, recognized for community initiatives."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC014",
        "first_name": "Samuel",
        "last_name": "Otieno",
        "email": "samuel.otieno@example.com",
        "bio": "Orthopedic surgeon with extensive experience in sports injuries.",
        "education": "MD, University of Cape Town, Class of 2010",
        "certifications": "Fellowship in Orthopedic Surgery",
        "specialty": "Orthopedic Surgeon",
        "image": "images/Dr7.jpg",
        "department_id": 5,
        "years_of_experience": 13,
        "achievements": "Led research on sports injuries, authored multiple publications."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC015",
        "first_name": "Grace",
        "last_name": "Njeri",
        "email": "grace.njeri@example.com",
        "bio": "Orthopedic surgeon with a focus on trauma care.",
        "education": "MD, University of Illinois, Class of 2013",
        "certifications": "Board Certified in Orthopedic Surgery",
        "specialty": "Orthopedic Surgeon",
        "image": "images/Dr8.jpg",
        "department_id": 5,
        "years_of_experience": 8,
        "achievements": "Developed protocols for post-surgery rehabilitation."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC016",
        "first_name": "Alex",
        "last_name": "Wangari",
        "email": "alex.wangari@example.com",
        "bio": "Experienced neurologist specializing in epilepsy and seizures.",
        "education": "MD, University of Chicago, Class of 2009",
        "certifications": "Board Certified in Neurology",
        "specialty": "Neurologist",
        "image": "images/Dr9.jpg",
        "department_id": 3,
        "years_of_experience": 14,
        "achievements": "Published multiple articles on epilepsy treatment."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC017",
        "first_name": "Pamela",
        "last_name": "Juma",
        "email": "pamela.juma@example.com",
        "bio": "Neurologist with a focus on stroke recovery.",
        "education": "MD, University of California, Class of 2016",
        "certifications": "Fellowship in Neurology",
        "specialty": "Neurologist",
        "image": "images/Dr10.jpg",
        "department_id": 3,
        "years_of_experience": 7,
        "achievements": "Involved in stroke recovery programs, recognized for patient advocacy."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC018",
        "first_name": "Felix",
        "last_name": "Muriuki",
        "email": "felix.muriuki@example.com",
        "bio": "General surgeon with experience in minimally invasive techniques.",
        "education": "MD, University of Washington, Class of 2012",
        "certifications": "Board Certified in General Surgery",
        "specialty": "General Surgeon",
        "image": "images/Dr11.jpg",
        "department_id": 6,
        "years_of_experience": 11,
        "achievements": "Pioneered new techniques in laparoscopic surgery."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC019",
        "first_name": "Caroline",
        "last_name": "Oganda",
        "email": "caroline.oganda@example.com",
        "bio": "General surgeon with a passion for surgical education.",
        "education": "MD, University of Toronto, Class of 2014",
        "certifications": "Board Certified in General Surgery",
        "specialty": "General Surgeon",
        "image": "images/Dr12.jpg",
        "department_id": 6,
        "years_of_experience": 9,
        "achievements": "Conducted surgical workshops for residents."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC020",
        "first_name": "Evelyn",
        "last_name": "Achieng",
        "email": "evelyn.achieng@example.com",
        "bio": "Gynecologist specializing in women's health and wellness.",
        "education": "MD, University of Nairobi, Class of 2013",
        "certifications": "Board Certified in Obstetrics and Gynecology",
        "specialty": "Gynecologist",
        "image": "images/Dr13.jpg",
        "department_id": 6,
        "years_of_experience": 8,
        "achievements": "Active in community health initiatives focusing on women's issues."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC021",
        "first_name": "Victor",
        "last_name": "Okello",
        "email": "victor.okello@example.com",
        "bio": "Pediatrician with expertise in childhood diseases.",
        "education": "MD, University of Manchester, Class of 2015",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr14.jpg",
        "department_id": 4,
        "years_of_experience": 9,
        "achievements": "Published research on childhood diabetes."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC022",
        "first_name": "Lillian",
        "last_name": "Wambui",
        "email": "lillian.wambui@example.com",
        "bio": "Cardiologist focused on preventive heart care.",
        "education": "MD, Yale University, Class of 2011",
        "certifications": "Board Certified in Cardiology",
        "specialty": "Cardiologist",
        "image": "images/Dr15.jpg",
        "department_id": 2,
        "years_of_experience": 12,
        "achievements": "Developed community awareness programs on heart health."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC023",
        "first_name": "Robert",
        "last_name": "Kirubi",
        "email": "robert.kirubi@example.com",
        "bio": "Expert in critical care medicine with years of experience.",
        "education": "MD, University of Edinburgh, Class of 2009",
        "certifications": "Certified in Critical Care Medicine",
        "specialty": "Critical Care Specialist",
        "image": "images/Dr16.jpg",
        "department_id": 1,
        "years_of_experience": 15,
        "achievements": "Received accolades for excellence in patient care."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC024",
        "first_name": "Pamela",
        "last_name": "Karanja",
        "email": "pamela.karanja@example.com",
        "bio": "Dedicated orthopedic surgeon specializing in sports injuries.",
        "education": "MD, University of California, Class of 2014",
        "certifications": "Fellowship in Orthopedic Surgery",
        "specialty": "Orthopedic Surgeon",
        "image": "images/Dr17.jpg",
        "department_id": 5,
        "years_of_experience": 8,
        "achievements": "Involved in community sports health education."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC025",
        "first_name": "Benard",
        "last_name": "Atuma",
        "email": "benard.atuma@example.com",
        "bio": "Neurosurgeon with a focus on brain tumors.",
        "education": "MD, Johns Hopkins University, Class of 2012",
        "certifications": "Board Certified in Neurology",
        "specialty": "Neurosurgeon",
        "image": "images/Dr18.jpg",
        "department_id": 3,
        "years_of_experience": 10,
        "achievements": "Developed innovative surgical techniques for brain tumors."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC026",
        "first_name": "Aisha",
        "last_name": "Omondi",
        "email": "aisha.omondi@example.com",
        "bio": "General surgeon with a focus on women's health.",
        "education": "MD, University of Cape Town, Class of 2016",
        "certifications": "Board Certified in General Surgery",
        "specialty": "General Surgeon",
        "image": "images/Dr19.jpg",
        "department_id": 6,
        "years_of_experience": 7,
        "achievements": "Established women's health programs in the community."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC027",
        "first_name": "Njeri",
        "last_name": "Muthoni",
        "email": "njeri.muthoni@example.com",
        "bio": "Pediatric cardiologist passionate about children's heart health.",
        "education": "MD, Harvard Medical School, Class of 2018",
        "certifications": "Board Certified in Pediatric Cardiology",
        "specialty": "Pediatric Cardiologist",
        "image": "images/Dr20.jpg",
        "department_id": 4,
        "years_of_experience": 5,
        "achievements": "Advocated for children's access to cardiac care."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC028",
        "first_name": "Isaac",
        "last_name": "Kimani",
        "email": "isaac.kimani@example.com",
        "bio": "Emergency physician with a background in trauma care.",
        "education": "MD, University of Nairobi, Class of 2015",
        "certifications": "Fellowship in Emergency Medicine",
        "specialty": "Emergency Physician",
        "image": "images/Dr21.jpg",
        "department_id": 1,
        "years_of_experience": 9,
        "achievements": "Implemented new emergency response protocols."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC029",
        "first_name": "Carla",
        "last_name": "Akinyi",
        "email": "carla.akinyi@example.com",
        "bio": "Neurosurgeon specializing in complex brain surgery.",
        "education": "MD, University of Toronto, Class of 2012",
        "certifications": "Board Certified in Neurosurgery",
        "specialty": "Neurosurgeon",
        "image": "images/Dr22.jpg",
        "department_id": 3,
        "years_of_experience": 8,
        "achievements": "Awarded for innovative approaches in brain surgery."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC030",
        "first_name": "Diana",
        "last_name": "Jebet",
        "email": "diana.jebet@example.com",
        "bio": "Gynecologist with a focus on high-risk pregnancies.",
        "education": "MD, University of London, Class of 2014",
        "certifications": "Board Certified in Obstetrics and Gynecology",
        "specialty": "Gynecologist",
        "image": "images/Dr23.jpg",
        "department_id": 6,
        "years_of_experience": 6,
        "achievements": "Recognized for contributions to maternal health."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC031",
        "first_name": "Lydia",
        "last_name": "Ochieng",
        "email": "lydia.ochieng@example.com",
        "bio": "Experienced pediatrician focusing on childhood obesity.",
        "education": "MD, University of Nairobi, Class of 2017",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr24.jpg",
        "department_id": 4,
        "years_of_experience": 7,
        "achievements": "Led community programs addressing childhood obesity."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC032",
        "first_name": "Moses",
        "last_name": "Chege",
        "email": "moses.chege@example.com",
        "bio": "General surgeon specializing in laparoscopic procedures.",
        "education": "MD, University of Texas, Class of 2010",
        "certifications": "Board Certified in General Surgery",
        "specialty": "General Surgeon",
        "image": "images/Dr25.jpg",
        "department_id": 6,
        "years_of_experience": 10,
        "achievements": "Conducted workshops on minimally invasive surgery."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC033",
        "first_name": "Kevin",
        "last_name": "Gitau",
        "email": "kevin.gitau@example.com",
        "bio": "Orthopedic surgeon specializing in joint replacements.",
        "education": "MD, University of Illinois, Class of 2011",
        "certifications": "Fellowship in Orthopedic Surgery",
        "specialty": "Orthopedic Surgeon",
        "image": "images/Dr26.jpg",
        "department_id": 5,
        "years_of_experience": 9,
        "achievements": "Recognized for excellence in joint replacement surgery."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC034",
        "first_name": "Amani",
        "last_name": "Muturi",
        "email": "amani.muturi@example.com",
        "bio": "Pediatrician with a focus on child mental health.",
        "education": "MD, University of Melbourne, Class of 2016",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr27.jpg",
        "department_id": 4,
        "years_of_experience": 8,
        "achievements": "Involved in research on childhood mental health."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC035",
        "first_name": "Sharon",
        "last_name": "Wawira",
        "email": "sharon.wawira@example.com",
        "bio": "Neurologist specializing in dementia care.",
        "education": "MD, University of Alberta, Class of 2015",
        "certifications": "Fellowship in Neurology",
        "specialty": "Neurologist",
        "image": "images/Dr28.jpg",
        "department_id": 3,
        "years_of_experience": 6,
        "achievements": "Published research on dementia treatment."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC036",
        "first_name": "Julius",
        "last_name": "Chebet",
        "email": "julius.chebet@example.com",
        "bio": "General surgeon with experience in trauma surgery.",
        "education": "MD, University of Ghana, Class of 2014",
        "certifications": "Board Certified in General Surgery",
        "specialty": "General Surgeon",
        "image": "images/Dr29.jpg",
        "department_id": 6,
        "years_of_experience": 7,
        "achievements": "Recognized for excellence in trauma surgery."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC037",
        "first_name": "Kevin",
        "last_name": "Mugisha",
        "email": "kevin.mugisha@example.com",
        "bio": "Expert in pediatric infectious diseases.",
        "education": "MD, University of Minnesota, Class of 2012",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatric Infectious Disease Specialist",
        "image": "images/Dr30.jpg",
        "department_id": 4,
        "years_of_experience": 9,
        "achievements": "Conducted research on childhood infectious diseases."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC038",
        "first_name": "Maria",
        "last_name": "Nabwire",
        "email": "maria.nabwire@example.com",
        "bio": "Orthopedic surgeon specializing in pediatric orthopedic surgery.",
        "education": "MD, University of Cape Town, Class of 2018",
        "certifications": "Fellowship in Pediatric Orthopedic Surgery",
        "specialty": "Pediatric Orthopedic Surgeon",
        "image": "images/Dr31.jpg",
        "department_id": 5,
        "years_of_experience": 5,
        "achievements": "Advocated for pediatric orthopedic care."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC039",
        "first_name": "Peter",
        "last_name": "Muthomi",
        "email": "peter.muthomi@example.com",
        "bio": "Expert in critical care and trauma surgery.",
        "education": "MD, Stanford University, Class of 2013",
        "certifications": "Board Certified in Critical Care Medicine",
        "specialty": "Critical Care Specialist",
        "image": "images/Dr32.jpg",
        "department_id": 1,
        "years_of_experience": 9,
        "achievements": "Involved in trauma surgery education."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC040",
        "first_name": "Joyce",
        "last_name": "Wanjiru",
        "email": "joyce.wanjiru@example.com",
        "bio": "Gynecologist specializing in reproductive health.",
        "education": "MD, University of Nairobi, Class of 2016",
        "certifications": "Board Certified in Obstetrics and Gynecology",
        "specialty": "Gynecologist",
        "image": "images/Dr33.jpg",
        "department_id": 6,
        "years_of_experience": 8,
        "achievements": "Advocate for women's reproductive health."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC041",
        "first_name": "Daniel",
        "last_name": "Ngoya",
        "email": "daniel.ngoya@example.com",
        "bio": "Pediatrician with experience in adolescent health.",
        "education": "MD, University of Michigan, Class of 2014",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr34.jpg",
        "department_id": 4,
        "years_of_experience": 9,
        "achievements": "Involved in programs addressing adolescent health issues."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC042",
        "first_name": "Gladys",
        "last_name": "Omutere",
        "email": "gladys.omutere@example.com",
        "bio": "Orthopedic surgeon specializing in joint disorders.",
        "education": "MD, University of Bristol, Class of 2012",
        "certifications": "Fellowship in Orthopedic Surgery",
        "specialty": "Orthopedic Surgeon",
        "image": "images/Dr35.jpg",
        "department_id": 5,
        "years_of_experience": 10,
        "achievements": "Conducted workshops on orthopedic care."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC043",
        "first_name": "Samuel",
        "last_name": "Mwenda",
        "email": "samuel.mwenda@example.com",
        "bio": "Expert in pediatric neurology.",
        "education": "MD, University of London, Class of 2015",
        "certifications": "Board Certified in Pediatric Neurology",
        "specialty": "Pediatric Neurologist",
        "image": "images/Dr36.jpg",
        "department_id": 4,
        "years_of_experience": 8,
        "achievements": "Involved in research on pediatric neurological disorders."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC044",
        "first_name": "Philip",
        "last_name": "Murimi",
        "email": "philip.murimi@example.com",
        "bio": "Critical care physician with extensive trauma experience.",
        "education": "MD, University of Cape Town, Class of 2010",
        "certifications": "Board Certified in Critical Care Medicine",
        "specialty": "Critical Care Specialist",
        "image": "images/Dr37.jpg",
        "department_id": 1,
        "years_of_experience": 12,
        "achievements": "Recognized for contributions to critical care."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC045",
        "first_name": "Rebecca",
        "last_name": "Njuguna",
        "email": "rebecca.njuguna@example.com",
        "bio": "Experienced gynecologist focusing on reproductive endocrinology.",
        "education": "MD, University of California, Class of 2013",
        "certifications": "Board Certified in Obstetrics and Gynecology",
        "specialty": "Gynecologist",
        "image": "images/Dr38.jpg",
        "department_id": 6,
        "years_of_experience": 11,
        "achievements": "Developed reproductive health education programs."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC046",
        "first_name": "Henry",
        "last_name": "Karanja",
        "email": "henry.karanja@example.com",
        "bio": "Pediatrician specializing in childhood nutrition.",
        "education": "MD, University of Massachusetts, Class of 2015",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr39.jpg",
        "department_id": 4,
        "years_of_experience": 9,
        "achievements": "Involved in community nutrition programs."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC047",
        "first_name": "Jacqueline",
        "last_name": "Muli",
        "email": "jacqueline.muli@example.com",
        "bio": "Expert in adolescent medicine.",
        "education": "MD, University of North Carolina, Class of 2014",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr40.jpg",
        "department_id": 4,
        "years_of_experience": 9,
        "achievements": "Advocated for adolescent health issues."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC048",
        "first_name": "Grace",
        "last_name": "Atuma",
        "email": "grace.atuma@example.com",
        "bio": "Orthopedic surgeon specializing in spinal surgery.",
        "education": "MD, University of Virginia, Class of 2013",
        "certifications": "Fellowship in Orthopedic Surgery",
        "specialty": "Orthopedic Surgeon",
        "image": "images/Dr41.jpg",
        "department_id": 5,
        "years_of_experience": 10,
        "achievements": "Involved in spinal health education."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC049",
        "first_name": "John",
        "last_name": "Muriuki",
        "email": "john.muriuki@example.com",
        "bio": "Experienced gynecologist focusing on maternal-fetal medicine.",
        "education": "MD, University of Florida, Class of 2012",
        "certifications": "Board Certified in Obstetrics and Gynecology",
        "specialty": "Gynecologist",
        "image": "images/Dr42.jpg",
        "department_id": 6,
        "years_of_experience": 11,
        "achievements": "Advocate for maternal health education."
    },
    {
        "title": "Dr.",
        "doctorId": "DOC050",
        "first_name": "Alice",
        "last_name": "Akinyi",
        "email": "alice.akinyi@example.com",
        "bio": "Pediatrician specializing in developmental disorders.",
        "education": "MD, University of Pennsylvania, Class of 2016",
        "certifications": "Board Certified in Pediatrics",
        "specialty": "Pediatrician",
        "image": "images/Dr43.jpg",
        "department_id": 4,
        "years_of_experience": 7,
        "achievements": "Conducted research on developmental disorders."
    }
]
with app.app_context():
    print("Clearing db ...")
    db.drop_all()  # Optional: Clear all tables (ensure you want to do this)
    db.create_all()  # Recreate tables after dropping them
    Doctor.query.delete()
    Patient.query.delete()
    Department.query.delete()
    Appointment.query.delete()

    print("Seeding Department data...")

    departments_data = [
        { 'name': 'Emergency', 'image': 'images/emergency.jpg' },
        { 'name': 'Cardiology', 'image': 'images/cardiology.jpg' },
        { 'name': 'Neurology', 'image': 'images/neurology.jpg' },
        { 'name': 'Pediatrics', 'image': 'images/pediatrics.jpg' },
        { 'name': 'Orthopedics', 'image': 'images/orthopedics.jpg' },
        { 'name': 'Gynecology', 'image': 'images/gynecology.jpg' },
        { 'name': 'General Surgery', 'image': 'images/general_surgery.jpg' },
    ]

    # Seed department data into the database
    for department_data in departments_data:
        department = Department(
            name=department_data['name'],
            description=faker.text(),
            image=department_data['image']
        )
        db.session.add(department)

    db.session.commit()

    print("Seeding Doctor data...")

    # Seed doctor data into the database
    for doctor_data in doctors_profiles:
        doctor = Doctor(
            title="Dr.",
            doctorId=faker.unique.random_number(digits=7, fix_len=True),
            first_name=doctor_data['name'].split()[1],
            last_name=doctor_data['name'].split()[2],
            email=faker.unique.email(),
            bio=faker.paragraph(nb_sentences=3),
            education=doctor_data['education'],
            certifications=doctor_data['certifications'],
            achievements=doctor_data['achievements'],
            image=doctor_data['image'],
            specialty=doctor_data['specialty'],
            department_id=doctor_data['department_id'],
            years_of_experience=doctor_data['years_of_experience'],
            phone_number=faker.phone_number(),
            password=bcrypt.generate_password_hash('1234Abcd').decode('utf-8')
        )
        db.session.add(doctor)

    db.session.commit()

    print("Seeding Patient data...")
    
    patients = []
    genders = ['Male', 'Female', 'Other']
    for _ in range(100):
        patient = Patient(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            age=faker.random_int(18, 99),
            gender=random.choice(genders),
            email=faker.unique.email(),
            phone_number=faker.phone_number(),
            password=bcrypt.generate_password_hash('1234Abcd').decode('utf-8')
        )
        patients.append(patient)
    db.session.add_all(patients)
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
            patient_id=random.randint(1, 100),  # Ensure patient ID is valid
            doctor_id=random.randint(1, 50)     # Ensure doctor ID is valid
        )
        appointments.append(appointment)

    db.session.add_all(appointments)
    db.session.commit()

    print("Database seeded successfully!")
