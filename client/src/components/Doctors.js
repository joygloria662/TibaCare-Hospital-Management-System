import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Navbar from './Navbar';
import DoctorCard from './DoctorCard'; // Import the DoctorCard component

const Doctors = () => {
  const { departmentId } = useParams();
  const [doctors, setDoctors] = useState([]);
console.log(doctors)
  useEffect(() => {
    // Fetching doctors by department from the Flask API
    fetch(`/api/departments/${departmentId}/doctors`)
      .then(response => response.json())
      .then(data => setDoctors(data))
      .catch(error => console.error('Error fetching doctors:', error));
  }, [departmentId]);

  return (
    <div>
      <Navbar />
      <h2>Doctors in Department {departmentId}</h2>
      <div className="doctors-grid">
        {doctors.map(doctor => (
          // Pass doctor data to DoctorCard component
          <DoctorCard key={doctor.id} doctor={doctor} />
        ))}
      </div>
    </div>
  );
};

export default Doctors;
