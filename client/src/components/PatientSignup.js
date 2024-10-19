import React, { useEffect, useState } from "react";
import { useFormik } from 'formik';
import * as yup from 'yup';
import Navbar from "./Navbar";

function PatientSignup() {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');
    const [messageType, setMessageType] = useState(''); // "success" or "error"

    const passRules = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/;

    // Validation schema
    const basicSchema = yup.object().shape({
        first_name: yup.string().required('First name is required'),
        last_name: yup.string().required('Last name is required'),
        email: yup.string().email('Please enter a valid email').required('Email is required'),
        age: yup.number().integer('Age must be a number').required('Age is required'),
        gender: yup.string().required('Gender is required'),
        phone_number: yup.string()
            .matches(/^\d{10,13}$/, 'Phone number must be between 10 and 13 digits')
            .required('Phone number is required'),
        password: yup.string()
            .min(6, 'Password must be at least 6 characters long')
            .matches(passRules, "Password must contain at least 1 uppercase letter, 1 lowercase letter, and 1 number")
            .required('Password is required'),
        confirmPassword: yup.string()
            .oneOf([yup.ref('password')], "Passwords do not match")
            .required('Confirm password is required'),
    });

    const formik = useFormik({
        initialValues: {
            first_name: '',
            last_name: '',
            email: '',
            age: '',
            gender: '',
            phone_number: '',
            password: '',
            confirmPassword: ''
        },
        validationSchema: basicSchema,
        onSubmit: async (values, actions) => {
            setLoading(true);
            try {
                // Directly use formik `values` as the request body
                const response = await fetch('/patientsignup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json', // Ensure JSON format
                    },
                    body: JSON.stringify(values), // Send formik values directly
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || 'Failed to submit the form');
                }

                // Get the success data (assuming it's in JSON format)
                const data = await response.json();
                setMessage(data.message);
                setMessageType('success');
                actions.resetForm(); // Reset the form after successful submission
            } catch (error) {
                setMessage(error.message);
                setMessageType('error');
            } finally {
                setLoading(false);
            }
        }
    });

    const { values, errors, touched, handleBlur, handleChange, handleSubmit} = formik;

    // Clear message after 5 seconds
    useEffect(() => {
        if (message) {
            const timer = setTimeout(() => {
                setMessage('');
                // setMessageType('');
            }, 5000);
            return () => clearTimeout(timer);
        }
    }, [message]);
    
    return (
        <>
            <Navbar />
            <div className="signup">
                <h1>Patient Signup</h1>
                <form className="signupForm" onSubmit={handleSubmit}>
                    <input
                        type="text"
                        name="first_name"
                        placeholder="First Name"
                        value={values.first_name}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.first_name && touched.first_name ? "inputError" : ""}
                    />
                    {errors.first_name && touched.first_name && <p className="errors">{errors.first_name}</p>}

                    <input
                        type="text"
                        name="last_name"
                        placeholder="Last Name"
                        value={values.last_name}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.last_name && touched.last_name ? "inputError" : ""}
                    />
                    {errors.last_name && touched.last_name && <p className="errors">{errors.last_name}</p>}

                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={values.email}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.email && touched.email ? "inputError" : ""}
                    />
                    {errors.email && touched.email && <p className="errors">{errors.email}</p>}

                    <input
                        type="text"
                        name="age"
                        placeholder="Age"
                        value={values.age}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.age && touched.age ? "inputError" : ""}
                    />
                    {errors.age && touched.age && <p className="errors">{errors.age}</p>}

                    <select
                        name="gender"
                        value={values.gender}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.gender && touched.gender ? "inputError" : ""}
                    >
                        <option value="">Select Gender</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Other">Other</option>
                    </select>
                    {errors.gender && touched.gender && <p className="errors">{errors.gender}</p>}

                    <input
                        type="text"
                        name="phone_number"
                        placeholder="Phone Number"
                        value={values.phone_number}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.phone_number && touched.phone_number ? "inputError" : ""}
                    />
                    {errors.phone_number && touched.phone_number && <p className="errors">{errors.phone_number}</p>}

                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        value={values.password}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.password && touched.password ? "inputError" : ""}
                    />
                    {errors.password && touched.password && <p className="errors">{errors.password}</p>}

                    <input
                        type="password"
                        name="confirmPassword"
                        placeholder="Confirm Password"
                        value={values.confirmPassword}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.confirmPassword && touched.confirmPassword ? "inputError" : ""}
                    />
                    {errors.confirmPassword && touched.confirmPassword && <p className="errors">{errors.confirmPassword}</p>}

                    <div className="signupButtons">
                    <button disabled={loading} type="submit">
                        {loading ? 'Submitting...' : 'SIGNUP'}
                    </button>
                </div>
                </form>
                {message && <p className={`responseMessage ${messageType}`}>{message}</p>}
            </div>
        </>
    );
}

export default PatientSignup;
