import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import Header from './Header';

const Doctors = () => {
  const { departmentId } = useParams();
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    const doctorsData = {
      // Emergency Department
      16: [
        { id: 45, name: 'Dr. Michael Ndungu', specialty: 'Emergency Physician', imageUrl: '/images/Dr45.jpg', fullyBooked: false },
        { id: 46, name: 'Dr. Sarah Onyango', specialty: 'Trauma Surgeon', imageUrl: '/images/Dr46.jpg', fullyBooked: true },
        { id: 47, name: 'Dr. James Wambui', specialty: 'Emergency Physician', imageUrl: '/images/Dr47.jpg', fullyBooked: false },
        { id: 48, name: 'Dr. Linda Njoroge', specialty: 'Critical Care Specialist', imageUrl: '/images/Dr48.jpg', fullyBooked: false },
        { id: 49, name: 'Dr. Peter Mwangi', specialty: 'Emergency Physician', imageUrl: '/images/Dr49.jpg', fullyBooked: false },
        { id: 50, name: 'Dr. Nancy Omondi', specialty: 'Emergency Physician', imageUrl: '/images/Dr50.jpg', fullyBooked: true },
      ],

      // Cardiology
      1: [
        { id: 1, name: 'Dr. John Kamau', specialty: 'Cardiologist', imageUrl: '/images/Dr1.jpg', fullyBooked: false },
        { id: 2, name: 'Dr. Jane Mwangi', specialty: 'Cardiologist', imageUrl: '/images/Dr2.jpg', fullyBooked: true },
        { id: 3, name: 'Dr. Allan Wekesa', specialty: 'Cardiologist', imageUrl: '/images/Dr3.jpg', fullyBooked: false },
        { id: 4, name: 'Dr. Susan Otieno', specialty: 'Cardiologist', imageUrl: '/images/Dr4.jpg', fullyBooked: false },
      ],

      // Neurology
      2: [
        { id: 5, name: 'Dr. Peter Odhiambo', specialty: 'Neurologist', imageUrl: '/images/Dr5.jpg', fullyBooked: false },
        { id: 6, name: 'Dr. Ann Wanjiru', specialty: 'Neurologist', imageUrl: '/images/Dr6.jpg', fullyBooked: true },
        { id: 7, name: 'Dr. David Maina', specialty: 'Neurologist', imageUrl: '/images/Dr7.jpg', fullyBooked: false },
        { id: 8, name: 'Dr. Angela Mwangi', specialty: 'Neurologist', imageUrl: '/images/Dr8.jpg', fullyBooked: false },
      ],

      // Pediatrics
      7: [
        { id: 21, name: 'Dr. Sarah Njeri', specialty: 'Pediatrician', imageUrl: '/images/Dr21.jpg', fullyBooked: false },
        { id: 22, name: 'Dr. Richard Kamau', specialty: 'Pediatrician', imageUrl: '/images/Dr22.jpg', fullyBooked: true },
        { id: 23, name: 'Dr. Fiona Wambui', specialty: 'Pediatrician', imageUrl: '/images/Dr23.jpg', fullyBooked: false },
        { id: 24, name: 'Dr. Kevin Otieno', specialty: 'Pediatrician', imageUrl: '/images/Dr24.jpg', fullyBooked: false },
      ],

      // Orthopedics
      3: [
        { id: 9, name: 'Dr. Samuel Otieno', specialty: 'Orthopedic Surgeon', imageUrl: '/images/Dr9.jpg', fullyBooked: false },
        { id: 10, name: 'Dr. Lucy Wanjiru', specialty: 'Orthopedic Surgeon', imageUrl: '/images/Dr10.jpg', fullyBooked: true },
        { id: 11, name: 'Dr. Anthony Mburu', specialty: 'Orthopedic Surgeon', imageUrl: '/images/Dr11.jpg', fullyBooked: false },
      ],

      // Gynecology
      13: [
        { id: 38, name: 'Dr. Jack Mwangi', specialty: 'Gynecologist', imageUrl: '/images/Dr38.jpg', fullyBooked: false },
        { id: 39, name: 'Dr. Carol Njeri', specialty: 'Gynecologist', imageUrl: '/images/Dr39.jpg', fullyBooked: true },
      ],

      // General Surgery
      8: [
        { id: 25, name: 'Dr. Michael Wekesa', specialty: 'General Surgeon', imageUrl: '/images/Dr25.jpg', fullyBooked: false },
        { id: 26, name: 'Dr. Evelyn Wanjiru', specialty: 'General Surgeon', imageUrl: '/images/Dr26.jpg', fullyBooked: true },
        { id: 27, name: 'Dr. Charles Mburu', specialty: 'General Surgeon', imageUrl: '/images/Dr27.jpg', fullyBooked: false },
      ],

      // Optometry
      5: [
        { id: 15, name: 'Dr. Grace Otieno', specialty: 'Optometrist', imageUrl: '/images/Dr15.jpg', fullyBooked: false },
        { id: 16, name: 'Dr. Mark Wambui', specialty: 'Ophthalmologist', imageUrl: '/images/Dr16.jpg', fullyBooked: true },
        { id: 17, name: 'Dr. Stephen Muthoni', specialty: 'Optometrist', imageUrl: '/images/Dr17.jpg', fullyBooked: false },
      ],

      // Radiology
      15: [
        { id: 43, name: 'Dr. Esther Mutai', specialty: 'Radiologist', imageUrl: '/images/Dr43.jpg', fullyBooked: false },
        { id: 44, name: 'Dr. Nelson Ndung\'u', specialty: 'Radiologist', imageUrl: '/images/Dr44.jpg', fullyBooked: true },
      ],

      // ENT
      12: [
        { id: 35, name: 'Dr. Janet Wangari', specialty: 'ENT Specialist', imageUrl: '/images/Dr35.jpg', fullyBooked: false },
        { id: 36, name: 'Dr. Robert Odhiambo', specialty: 'ENT Specialist', imageUrl: '/images/Dr36.jpg', fullyBooked: true },
        { id: 37, name: 'Dr. Patricia Njuguna', specialty: 'ENT Specialist', imageUrl: '/images/Dr37.jpg', fullyBooked: false },
      ],

      // Oncology
      10: [
        { id: 30, name: 'Dr. Alice Muriuki', specialty: 'Oncologist', imageUrl: '/images/Dr30.jpg', fullyBooked: false },
        { id: 31, name: 'Dr. Samuel Njeru', specialty: 'Oncologist', imageUrl: '/images/Dr31.jpg', fullyBooked: true },
        { id: 32, name: 'Dr. Linda Mwangi', specialty: 'Oncologist', imageUrl: '/images/Dr32.jpg', fullyBooked: false },
      ],

      // Urology
      11: [
        { id: 33, name: 'Dr. Ibrahim Muthoni', specialty: 'Urologist', imageUrl: '/images/Dr33.jpg', fullyBooked: false },
        { id: 34, name: 'Dr. Sarah Wambui', specialty: 'Urologist', imageUrl: '/images/Dr34.jpg', fullyBooked: true },
      ],

      // Dentistry
      4: [
        { id: 12, name: 'Dr. Paul Muriuki', specialty: 'Dentist', imageUrl: '/images/Dr12.jpg', fullyBooked: false },
        { id: 13, name: 'Dr. Alice Njuguna', specialty: 'Dentist', imageUrl: '/images/Dr13.jpg', fullyBooked: true },
        { id: 14, name: 'Dr. Brian Kamau', specialty: 'Dentist', imageUrl: '/images/Dr14.jpg', fullyBooked: false },
      ],

      // Dermatology
      6: [
        { id: 18, name: 'Dr. Josephine Njeri', specialty: 'Dermatologist', imageUrl: '/images/Dr18.jpg', fullyBooked: false },
        { id: 19, name: 'Dr. Peter Kariuki', specialty: 'Dermatologist', imageUrl: '/images/Dr19.jpg', fullyBooked: true },
        { id: 20, name: 'Dr. Victor Onyango', specialty: 'Dermatologist', imageUrl: '/images/Dr20.jpg', fullyBooked: false },
      ],

      // Nephrology
      14: [
        { id: 40, name: 'Dr. Benjamin Ndung\'u', specialty: 'Nephrologist', imageUrl: '/images/Dr40.jpg', fullyBooked: false },
        { id: 41, name: 'Dr. Mary Akinyi', specialty: 'Nephrologist', imageUrl: '/images/Dr41.jpg', fullyBooked: true },
        { id: 42, name: 'Dr. Laura Otieno', specialty: 'Nephrologist', imageUrl: '/images/Dr42.jpg', fullyBooked: false },
      ],

      // Psychiatry
      9: [
        { id: 28, name: 'Dr. Jacob Wanjiru', specialty: 'Psychiatrist', imageUrl: '/images/Dr28.jpg', fullyBooked: false },
        { id: 29, name: 'Dr. Grace Muthoni', specialty: 'Psychiatrist', imageUrl: '/images/Dr29.jpg', fullyBooked: true },
      ],
    };

    setDoctors(doctorsData[departmentId] || []);
  }, [departmentId]);

  return (
    <div className="doctors-page">
        <Header/>
      <h2>Doctors in Department</h2>
      
      <div className="doctor-cards">
        {doctors.map((doctor) => (
          <div key={doctor.id} className="doctor-card">
            <img src={doctor.imageUrl} alt={doctor.name} />
            <h3>{doctor.name}</h3>
            <p>{doctor.specialty}</p>
            <button>
              <Link to={`/doctors/${doctor.id}/profile`}>Profile</Link>
            </button>

            {/* Conditional rendering for the Book Appointment button */}
            {departmentId === '16' ? null : doctor.fullyBooked ? (
              <button className="not-available" disabled>Not Available</button>
            ) : (
              <button>
                <Link to={`/book-appointment/${doctor.id}`}>Book Appointment</Link>
              </button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Doctors;
