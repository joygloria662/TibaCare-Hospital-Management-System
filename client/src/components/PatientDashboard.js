import React from 'react';
import PatientDetails from './PatientDetails';
import Departments from './Departments';


const PatientDashboard = () => {

    return (
        <div className="dashboard">
            <h2 className="dashboard-title">Patient Dashboard</h2>
            <nav className="dashboard-nav">
                <PatientDetails />
            </nav>
            <Departments />
        </div>
    );
}




export default PatientDashboard;