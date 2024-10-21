import React, { useState } from 'react';
import DoctorProfile from './DoctorProfile'; // Import DoctorProfile to show in modal

const DoctorCard = ({ doctor }) => {
  const [isModalOpen, setIsModalOpen] = useState(false); // Modal state

  const openModal = () => setIsModalOpen(true);
  const closeModal = () => setIsModalOpen(false);

  // Determine availability based on doctor status
  const isAvailable = !doctor.fullyBooked;

  return (
    <div className="doctor-card">
      <img src={`/${doctor.image}`} alt={doctor.name} className="doctor-card-img" />
      <h3>{doctor.name}</h3>
      <p>Specialty: {doctor.specialty}</p>
      <p>{isAvailable ? "Available" : "Fully Booked"}</p>

      {/* Button to open modal and view profile */}
      <button onClick={openModal}>View Profile</button>

      {/* Display Unavailable button if doctor is not available */}
      {isAvailable ? (
        <button className="book-appointment-btn">
          <a href={`/book-appointment/${doctor.id}`}>Book Appointment</a>
        </button>
      ) : (
        <button className="unavailable-button" disabled style={{ backgroundColor: '#d3d3d3', cursor: 'not-allowed' }}>
          Unavailable
        </button>
      )}

      {/* Modal with DoctorProfile */}
      {isModalOpen && (
        <div className="modal-overlay">
          <div className="modal-content">
            <span className="close-modal" onClick={closeModal}>&times;</span>
            {/* Passing the doctor data to DoctorProfile */}
            <DoctorProfile doctor={doctor} />
          </div>
        </div>
      )}
    </div>
  );
};

export default DoctorCard;
