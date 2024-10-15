import React from 'react';

/*remember to import login and logout*/
function About(){
    return(
        <section className="about-section">
            <div className="about-container">
                {/*Mission Statement*/}
                <h2> className="about-heading"</h2>
                <p className="about-text">
                Providing compassionate care, groundbreaking treatments, and a healing touch — because your health is our mission.
                 </p>
                {/*Team Mantra*/}
                <h2 className="about-heading">Team Mantra</h2>
                <p className="about-text">
                Together, we’re the heartbeat of healthcare, every patient, every day.
                 </p>

                 {/*Vision statement*/}
                 <h2 className="about-heading">Our Vision</h2>
                 <p className= "about-text">
                 To lead the future of healthcare with cutting-edge innovation, a healthier community, and a patient-centered approach that redefines medical excellence.
                  </p>


            </div>
        </section>
    );
}
export default About;