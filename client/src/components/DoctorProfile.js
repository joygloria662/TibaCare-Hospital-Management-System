import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Navbar from './Navbar';

const DoctorProfile = () => {
  const { doctorId } = useParams(); // Get doctor ID from the URL
  const [doctor, setDoctor] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false); // Track modal state

  useEffect(() => {
    const doctorsData = [
      { 
        id: 1, 
        name: 'Dr. John Kamau', 
        specialty: 'Cardiologist', 
        bio: 'Dr. Kamau has over 10 years of experience in cardiology and specializes in treating heart conditions. He has worked with several renowned hospitals and is a certified heart transplant specialist.', 
        experience: '10 years',
        education: 'MBChB (UoN), MMed (Cardiology) - University of Nairobi', 
        certifications: 'Certified Heart Transplant Specialist', 
        achievements: 'Lead surgeon in 15 successful heart transplants.', 
        imageUrl: '/images/Dr1.jpg' 
      },
      // Add other doctors here...
    ];

    const selectedDoctor = doctorsData.find((doc) => doc.id === parseInt(doctorId));
    setDoctor(selectedDoctor);
  }, [doctorId]);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  if (!doctor) {
    return <p>Loading doctor information...</p>;
  }

  return (
    <div className="doctor-profile-page">
        <Navbar/>
      <div className="profile-card">
        <img src={doctor.imageUrl} alt={doctor.name} className="profile-img" />
        <h2>{doctor.name}</h2>
        <h4>Specialty: {doctor.specialty}</h4>
        <button className="profile-button" onClick={openModal}>
          View Profile
        </button>
      </div>

      {isModalOpen && (
        <div className="modal-overlay">
          <div className="modal-content">
            <span className="close-modal" onClick={closeModal}>&times;</span>
            <img src={doctor.imageUrl} alt={doctor.name} className="profile-img" />
            <h2>{doctor.name}</h2>
            <h4>Specialty: {doctor.specialty}</h4>
            <p>{doctor.bio}</p>
            <p><strong>Years of Experience:</strong> {doctor.experience}</p>
            <p><strong>Education:</strong> {doctor.education}</p>
            <p><strong>Certifications:</strong> {doctor.certifications}</p>
            <p><strong>Achievements:</strong> {doctor.achievements}</p>
            <button className="book-appointment-btn">
              <a href={`/book-appointment/${doctor.id}`}>Book Appointment</a>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default DoctorProfile;
