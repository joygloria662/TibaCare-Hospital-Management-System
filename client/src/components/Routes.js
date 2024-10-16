import React from "react";
import App from "./App";
import Signup from "./Signup";
import Login from "./Login";
import Departments from "./Departments";
import Doctors from "./Doctors";
import DoctorProfile from "./DoctorProfile";

const routes = [
    {
        path: '/',
        element: <App />
    },
    {
        path: '/signup',
        element: <Signup />
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
        path: "/departments/:departmentId", 
        element: <Doctors />
    },
    {
        path: "/doctors/:doctorId/profile",
        element: <DoctorProfile />
    }

]


export default routes;