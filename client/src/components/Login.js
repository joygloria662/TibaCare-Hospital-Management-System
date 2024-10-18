import React, { useState } from "react";
import PatientLogin from "./PatientLogin"; 
import DoctorLogin from "./DoctorLogin"; 

function Login() {
    const [isPatientLogin, setIsPatientLogin] = useState(true); 

    const handlePatientLoginClick = () => {
        setIsPatientLogin(true); 
    };

    const handleDoctorLoginClick = () => {
        setIsPatientLogin(false); 
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
