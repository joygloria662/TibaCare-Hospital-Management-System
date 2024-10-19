import React from "react";
import App from "./App";
import Login from "./Login";
import Departments from "./Departments";
import PatientDashboard from './PatientDashboard'
import About from "./About";
import Contact from "./Contact";
import Signup from "./Signup";
import DoctorDashboard from "./DoctorDashboard";

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
        path: '/patientdashboard',
        element: <PatientDashboard />
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
        path: '/doctordashboard',
        element: <DoctorDashboard/>
    }
]


export default routes;