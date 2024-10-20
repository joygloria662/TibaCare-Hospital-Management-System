import React from "react";
import App from "./App";
import Login from "./Login";
import Departments from "./Departments";
import PatientDashboard from './PatientDashboard'
import About from "./About";
import Contact from "./Contact";
import Signup from "./Signup";
import DoctorDashboard from "./DoctorDashboard";
import PrivateRoute from "./PrivateRoute";


const routes = [
    {
        path: '/',
        element: <App />
    },
    {
        path: 'about',
        element: <About />
    },
    {
        path: 'contact',
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
    }
]


export default routes;