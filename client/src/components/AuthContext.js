import React, { createContext, useContext, useState, useEffect } from 'react';

// Create the AuthContext
const AuthContext = createContext();

// Custom hook to use the AuthContext
export const useAuth = () => {
    return useContext(AuthContext);
};

// AuthProvider component
export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [role, setRole] = useState(null);

    useEffect(() => {
        const fetchSession = async () => {
            try {
                const response = await fetch(`/check_session`, {
                    method: 'GET',
                    credentials: 'include',
                });

                if (response.ok) {
                    const { user, role } = await response.json();  // Destructure user and role from response
                    setUser(user); // store user details
                    setRole(role); // store user role (doctor/patient)
                } else {
                    throw new Error('Failed to fetch session');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        };

        fetchSession();
    }, []);

    return (
        <AuthContext.Provider value={{ user, role, setUser, setRole }}>
            {children}
        </AuthContext.Provider>
    );
};
