import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext"; // Use the AuthContext for checking login state

// PrivateRoute component
const PrivateRoute = ({ element: Component, ...rest }) => {
    const { user } = useAuth();  // Get the user from context

    if (!user) {
        // If no user is logged in, redirect to the login page
        return <Navigate to="/login" />;
    }

    // If user is logged in, render the component
    return Component;
};

export default PrivateRoute;
