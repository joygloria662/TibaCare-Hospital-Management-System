import React from 'react';

const DoctorProfile = ({ doctor }) => {
    return (
        <div className="doctor-profile">
            <h2>{doctor.title} {doctor.first_name} {doctor.last_name}</h2>
            <h4>Specialty: {doctor.specialty}</h4>
            <img src={doctor.image} alt={`${doctor.first_name} ${doctor.last_name}`} />
            <p><strong>Years of Experience:</strong> {doctor.years_of_experience}</p>
            <p><strong>Education:</strong> {doctor.education}</p>
            <p><strong>Certifications:</strong> {doctor.certifications}</p>
            <p><strong>Achievements:</strong> {doctor.achievements}</p>
            <p><strong>Status:</strong> {doctor.isAvailable ? 'Available' : 'Unavailable'}</p>
        </div>
    );
};

export default DoctorProfile;
