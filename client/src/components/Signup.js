import React, { useState } from "react";
import PatientSignup from "./PatientSignup"; 
import DoctorSignup from "./DoctorSignup"; 
import { Link } from "react-router-dom";

function Signup() {
    const [isPatientSignup, setIsPatientSignup] = useState(true); 

    const handlePatientSignupClick = () => {
        setIsPatientSignup(true); 
    };

    const handleDoctorSignupClick = () => {
        setIsPatientSignup(false);
    };
    

    return (
        <div className="Signup-container">
            <div>
            <div className="tab-buttons">
                <button onClick={handlePatientSignupClick} className={isPatientSignup ? "active" : ""}>
                    Patient Signup
                </button>
                <button onClick={handleDoctorSignupClick} className={!isPatientSignup ? "active" : ""}>
                    Doctor Signup
                </button>
                <Link to='/'>
                <button>
                    Cancel
                </button>
                </Link>
            </div>
            <div className="Signup-form">
                {isPatientSignup ? <PatientSignup /> : <DoctorSignup />}
            </div>
            </div> 
        </div>
    );
}

export default Signup;
