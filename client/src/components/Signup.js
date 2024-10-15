import React, { useEffect, useState } from "react";
import { useFormik } from 'formik';
import * as yup from 'yup';
import { Link } from "react-router-dom";

function Signup() {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');

    const passRules = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/;

    const basicSchema = yup.object().shape({
        email: yup.string().email('Please enter a valid email').required('Cannot be blank'),
        age: yup
            .number()
            .positive()
            .integer()
            .required('Cannot be blank')
            .typeError("Please enter a number"),
        password: yup
            .string()
            .min(6)
            .matches(passRules, { message: "Your Password must have at least 6 characters: at least 1 uppercase, 1 lowercase, and 1 number" })
            .required('Cannot be blank'),
        confirmPassword: yup
            .string()
            .oneOf([yup.ref('password')], "Passwords do not match")
            .required('Cannot be blank'),
    });

    const { values, errors, touched, isSubmitting, handleBlur, handleChange, handleSubmit } = useFormik({
        initialValues: {
            firstName: '',
            lastName: '',
            email: '',
            age: '',
            role: 'Doctor',
            password: '',
            confirmPassword: ''
        },
        validationSchema: basicSchema,

        onSubmit: async (values, actions) => {
            setLoading(true)
            try {
                const response = await fetch('http://localhost:5000/signup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(values)
                });

                if (!response.ok) {
                    throw new Error('Failed to submit the form')
                }

                const data = await response.json();
                setMessage(data.message)
                actions.resetForm()
            } catch (error) {
                setMessage(error.message);
            } finally {
                setLoading(false)
            }
        },
    });

    useEffect(() => {
        if (message) {
            const timer = setTimeout(() => setMessage(''), 5000);
            return () => clearTimeout(timer)
        }
    }, [message])

    return (
        <div>
        <div className="signup">
            <h1>Signup</h1>
            <form className="signupForm" onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="firstName"
                    placeholder="First Name"
                    value={values.firstName}
                    onChange={handleChange}
                    onBlur={handleBlur}
                />
                <input
                    type="text"
                    name="lastName"
                    placeholder="Last Name"
                    value={values.lastName}
                    onChange={handleChange}
                    onBlur={handleBlur}
                />
                <input
                    type="text"
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
                    name="role"
                    value={values.role}
                    onChange={handleChange}
                >
                    <option>Doctor</option>
                    <option>Patient</option>
                </select>
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
                    <button disabled={isSubmitting || loading} type="submit">
                    {loading ? 'Submitting...' : 'SIGNUP'}
                    </button>
                    <Link to="/login" className="hero-link">
                        <button type="button" className="cancelbtn">CANCEL</button>
                    </Link>
                </div>
            </form>
            {message && <p className="responseMessage">{message}</p>}
        </div>
        </div>
    );
}

export default Signup;
