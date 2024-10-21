import React from "react";
import App from "./App";
import Login from "./Login";
import Departments from "./Departments";
import Doctors from "./Doctors"; // Import the Doctors component
import PatientDashboard from './PatientDashboard';
import About from "./About";
import Contact from "./Contact";
import Signup from "./Signup";
import DoctorDashboard from "./DoctorDashboard";
import DoctorProfileContainer from "./DoctorProfileContainer"; // Import DoctorProfileContainer
import PrivateRoute from "./PrivateRoute";

const routes = [
    {
        path: '/',
        element: <App />
    },
    {
        path: '/about',
        element: <About />
    },
    {
        path: '/contact',
        element: <Contact />
    },
    {
        path: '/login',
        element: <Login />
    },
    {
        path: "/departments",
        element: <Departments />
    },
    {
        path: "/departments/:departmentId", // Route for doctors in a specific department
        element: <Doctors /> // Use Doctors component here
    },
    {
        path: '/signup',
        element: <Signup />
    },
    {
        path: '/patientdashboard',
        element: <PrivateRoute element={<PatientDashboard />} />  // Protect patient dashboard
    },
    {
        path: '/doctordashboard',
        element: <PrivateRoute element={<DoctorDashboard />} />  // Protect doctor dashboard
    },
    {
        path: '/doctors/:doctorId/profile', // Route for doctor profile
        element: <DoctorProfileContainer /> // Render DoctorProfileContainer component
    }
];

export default routes;
