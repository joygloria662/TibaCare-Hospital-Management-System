// Login.js
import { Link, useNavigate } from "react-router-dom";
import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import * as yup from 'yup';
import Navbar from "./Navbar";
import { useAuth } from './AuthContext'; // Import useAuth

function PatientLogin() {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');
    const navigate = useNavigate();
    const { user, setUser } = useAuth(); // Use context

    const loginSchema = yup.object().shape({
        email: yup.string().email("Invalid email format").required('Email is required'),
        password: yup.string().required('Username is required')
    });

    const { values, errors, touched, isSubmitting, handleChange, handleBlur, handleSubmit } = useFormik({
        initialValues: {
            email: "",
            password: "",
        },
        validationSchema: loginSchema,
        onSubmit: async (values) => {
            setLoading(true);
            try {
                const response = await fetch(`/login`, {
                    method: "POST",
                    credentials: 'include',
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(values)
                });
                
                if (response.ok) {
                    const data = await response.json();
                    setUser(data); // Set user in context
                    setMessage("Login Successful");

                    if (data.data.role === "Doctor") {
                        navigate("/departments");
                    } else if (data.data.role === "Patient") {
                        navigate("/");
                    }
                } else {
                    setMessage("Invalid username or password");
                }
            } catch (error) {
                setMessage("An error occurred during login");
            } finally {
                setLoading(false);
            }
        },
    });

    useEffect(() => {
        if (message) {
            const timer = setTimeout(() => setMessage(''), 5000);
            return () => clearTimeout(timer);
        }
    }, [message]);

    const handleGoBack = () => {
        window.history.back();
    };

    return (
        <>
            <Navbar />
            <div className="login-container">
                <div className="login">
                    <h1>Login as a Patient</h1>
                    <form onSubmit={handleSubmit}>
                        <input
                            type="text"
                            placeholder="Email"
                            name="email"
                            value={values.email}
                            onChange={handleChange}
                            onBlur={handleBlur}
                            className={errors.email && touched.email ? "inputError" : ""}
                        />
                        {errors.email && touched.email && <p className="errors">{errors.email}</p>}

                        <input
                            type="password"
                            placeholder="Password"
                            name="password"
                            value={values.password}
                            onChange={handleChange}
                            onBlur={handleBlur}
                            className={errors.password && touched.password ? "inputError" : ""}
                        />
                        {errors.password && touched.password && <p className="errors">{errors.password}</p>}

                        <button type="submit" disabled={isSubmitting || loading}>
                            {loading ? 'Logging in...' : 'Login'}
                        </button>
                    </form>

                    {message && <p className="responseMessage">{message}</p>}

                    <p>
                        Don't have an account? <Link to="/signup">Sign Up</Link>
                    </p>
                    <button onClick={handleGoBack}>Back</button>
                </div>
            </div>
        </>
    );
}

export default PatientLogin;
