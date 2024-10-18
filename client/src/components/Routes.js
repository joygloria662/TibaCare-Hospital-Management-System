import React from "react";
import App from "./App";
// import Signup from "./PatientSignup";
import Login from "./Login";
import Departments from "./Departments";
import Doctors from "./Doctors";
import DoctorProfile from "./DoctorProfile";
import PatientDashboard from './PatientDashboard'
import PatientDetails from "./PatientDetails";
import BookAppointment from "./BookAppointment";
import DoctorSignup from "./DoctorSignup";
import DoctorLogin from "./DoctorLogin";

const routes = [
    {
        path: '/',
        element: <App />
    },
    {
        path: '/drsignup',
        element: <DoctorSignup />
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
        path: '/login',
        element: <Login />
    },
    {
        path: "/departments/:departmentId", 
        element: <Doctors />
    },
    {
        path: "/doctors/:doctorId/profile",
        element: <DoctorProfile />
    },
    {
        path : '/patient-details',
        element : <PatientDetails/>
    },
    {
        path: "/book-appointment/:id",
        element: <BookAppointment />,
      },
]


export default routes;