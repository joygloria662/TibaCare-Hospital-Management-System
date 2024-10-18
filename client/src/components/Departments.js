import React from 'react';
import { Link } from 'react-router-dom';
import { AuthProvider} from './AuthContext'; // Import AuthProvider
import Navbar from './Navbar';

const Departments = () => {
  const departments = [
    { id: 16, name: 'Emergency', imageUrl: '/images/emergency.jpg' },
    { id: 1, name: 'Cardiology', imageUrl: '/images/cardiology.jpg' },
    { id: 2, name: 'Neurology', imageUrl: '/images/neurology.jpg' },
    { id: 7, name: 'Pediatrics', imageUrl: '/images/pediatrics.jpg' },
    { id: 3, name: 'Orthopedics', imageUrl: '/images/orthopedics.jpg' },
    { id: 13, name: 'Gynecology', imageUrl: '/images/gynecology.jpg' },
    { id: 8, name: 'General Surgery', imageUrl: '/images/general_surgery.jpg' },
    { id: 5, name: 'Optometry', imageUrl: '/images/optometry.jpg' },
    { id: 15, name: 'Radiology', imageUrl: '/images/radiology.jpg' },
    { id: 12, name: 'ENT', imageUrl: '/images/ent.jpg' },
    { id: 10, name: 'Oncology', imageUrl: '/images/oncology.jpg' },
    { id: 11, name: 'Urology', imageUrl: '/images/urology.jpg' },
    { id: 4, name: 'Dentistry', imageUrl: '/images/dentistry.jpg' },
    { id: 6, name: 'Dermatology', imageUrl: '/images/dermatology.jpg' },
    { id: 14, name: 'Nephrology', imageUrl: '/images/nephrology.jpg' },
    { id: 9, name: 'Psychiatry', imageUrl: '/images/psychiatry.jpg' }
  ];


  return (
    <div className="departments-page">
      <Navbar/>
      <h2>Hospital Departments</h2>
      <div className="departments-grid">
        {departments.map(department => (
          <div key={department.id} className="department-card">
            <Link to={`/departments/${department.id}`}>
              <img src={department.imageUrl} alt={department.name} />
              <h3>{department.name}</h3>
            </Link>
            {/* Conditional rendering for Emergency Department */}
            {department.name === 'Emergency' ? (
              <p>For urgent cases, visit our Emergency Department immediately.</p>
            ) : (
              // Removed Book Appointment link
              <p>Learn more about {department.name} services.</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};


const WrappedDept = () => (
  <AuthProvider>
      <Departments />
  </AuthProvider>
);

export default WrappedDept;