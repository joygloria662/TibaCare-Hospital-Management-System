import React from "react";
import App from "./App";
import Login from "./Login";
import Departments from "./Departments";
import PatientDashboard from './PatientDashboard'
import About from "./About";
import Contact from "./Contact";
import DoctorSignup from "./DoctorSignup";

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
        path: '/Patient-dashboard',
        element: <PatientDashboard />
    },
    {
        path: "/departments",
        element: <Departments />
    },
    {
        path: '/drsignup',
        element: <DoctorSignup />
    }
]


export default routes;