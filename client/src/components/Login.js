import { Link, useNavigate} from "react-router-dom";
import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import * as yup from 'yup';



function Login() {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');
    const [users, setUsers] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        fetch(``)
            .then((resp) => resp.json())
            .then((data) => setUsers(data));
    }, []);

    const loginSchema = yup.object().shape({
        username: yup.string().required('Username is required'),
        password: yup.string().required('Username is required')
    });

    const { values, errors, touched, isSubmitting, handleChange, handleBlur, handleSubmit } = useFormik({
        initialValues: {
            username: "",
            password: "",
        },
        validationSchema: loginSchema,
        onSubmit: async (values) => {
            setLoading(true);
            try {
                const authenticated = users.find(
                    (user) =>
                        user.username === values.username &&
                        user.password === values.password
                );

                if (authenticated) {
                    setMessage("Login Successful")

                    if (authenticated.role === 'Doctor'){
                        navigate('/doctordashboard');
                    }else if(authenticated.role === "Patient") {
                        navigate('/patientdashboard');
                    }
                } else {
                    setMessage("Invalid username or password")
                }
            } catch (error) {
                setMessage("An error occurred during logging in")
            } finally {
                setLoading(false)
            }
        }
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
        <div className="login-container">
            <div className="login">
                <h1>Login</h1>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        placeholder="Username"
                        name="username"
                        value={values.username}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        className={errors.username && touched.username ? "inputError" : ""}
                    />
                    {errors.username && touched.username && <p className="errors">{errors.username}</p>}

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
    );
}


export default Login;
