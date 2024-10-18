import React, { useState, useEffect } from 'react';
import './PatientDetails.css';


const PatientDetails = ({ patientId }) => {
  const [patient, setPatient] = useState(null);
  const [error, setError] = useState(null);


  useEffect(() => {
    fetch(`http://localhost:3000/patients/${patientId}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => setPatient(data))
      .catch((error) => {
        console.error('Fetch error:', error);
        setError(error.message);
      });
  }, [patientId]);


  return (
    <div className="patient-details">
      <h2>Patient Details</h2>
      {error ? (
        <p>Error fetching patient details: {error}</p>
      ) : patient ? (
        <div>
          <p><strong>Name:</strong> {patient.name}</p>
          <p><strong>Age:</strong> {patient.age}</p>
          <p><strong>Medical History:</strong></p>
          {patient.medicalHistory && patient.medicalHistory.length > 0 ? (
            <ul>
              {patient.medicalHistory.map((entry, index) => (
                <li key={index}>
                  <p><strong>Date:</strong> {entry.date}</p>
                  <p><strong>Diagnosis:</strong> {entry.diagnosis}</p>
                  <p><strong>Treatment:</strong> {entry.treatment}</p>
                </li>
              ))}
            </ul>
          ) : (
            <p>No medical history available.</p>
          )}
        </div>
      ) : (
        <p>Loading patient details...</p>
      )}
    </div>
  );
};


export default PatientDetails;