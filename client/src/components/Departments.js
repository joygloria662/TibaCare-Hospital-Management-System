import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { AuthProvider } from './AuthContext'; // Import AuthProvider
import Navbar from './Navbar';

const Departments = () => {
  const [departments, setDepartments] = useState([]);
  const [error, setError] = useState(null); // State for error handling

  useEffect(() => {
    fetch('/api/departments')  // Fetching departments from Flask API
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Fetched departments:', data); // Log the fetched data
        setDepartments(data);
      })
      .catch(error => {
        console.error('Error fetching departments:', error);
        setError(error.message); // Set the error message
      });
  }, []);

  return (
    <div className="departments-page">
      <Navbar />
      <h2>Hospital Departments</h2>
      {error && <p className="error">{error}</p>} {/* Display error message if any */}
      <div className="departments-grid">
        {departments.length > 0 ? ( // Check if there are any departments
          departments.map(department => (
            <div key={department.id} className="department-card">
              <Link to={`/departments/${department.id}`}> {/* Link to Doctors page */}
                <img src={department.image} alt={department.name} />
                <h3>{department.name}</h3>
              </Link>
              {department.name === 'Emergency' ? (
                <p>For urgent cases, visit our Emergency Department immediately.</p>
              ) : (
                <p>Learn more about {department.name} services.</p>
              )}
            </div>
          ))
        ) : (
          <p>No departments found.</p> // Message if no departments
        )}
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
