import React, { useState } from "react";
import PatientLogin from "./PatientLogin"; // Assuming you have a PatientLogin component
import DoctorLogin from "./DoctorLogin"; // Assuming you have a DoctorLogin component

function Login() {
    const [isPatientLogin, setIsPatientLogin] = useState(true); // Default to PatientLogin

    const handlePatientLoginClick = () => {
        setIsPatientLogin(true); // Show PatientLogin
    };

    const handleDoctorLoginClick = () => {
        setIsPatientLogin(false); // Show DoctorLogin
    };

    return (
        <div className="login-container">
            <div className="tab-buttons">
                <button onClick={handlePatientLoginClick} className={isPatientLogin ? "active" : ""}>
                    Patient Login
                </button>
                <button onClick={handleDoctorLoginClick} className={!isPatientLogin ? "active" : ""}>
                    Doctor Login
                </button>
            </div>
            <div className="login-form">
                {isPatientLogin ? <PatientLogin /> : <DoctorLogin />}
            </div>
        </div>
    );
}

export default Login;
