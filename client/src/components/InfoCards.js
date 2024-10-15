import React from "react";
import { Link } from "react-router-dom";

function InfoCards() {
    return (
        <>
            <div className="infoItems">
            <h1>What can you do with TibaCare?</h1>
            <div className="infoCards">
                <div className="getInfo">
                    <h3>Ask for assistance</h3>
                    <Link to='' >Learn More</Link>
                </div>
                <div className="getInfo">
                    <h3>Ask for assistance</h3>
                    <Link to='' >Learn More</Link>
                </div>
                <div className="getInfo">
                    <h3>Ask for assistance</h3>
                    <Link to='' >Learn More</Link>
                </div>
                <div className="getInfo">
                    <h3>Ask for assistance</h3>
                    <Link to='' >Learn More</Link>
                </div>
                <div className="getInfo">
                    <h3>Ask for assistance</h3>
                    <Link to='' >Learn More</Link>
                </div>
                <div className="getInfo">
                    <h3>Ask for assistance</h3>
                    <Link to='' >Learn More</Link>
                </div>
            </div>
            </div>
            <div className="aboutItems">
                <h1>Why Us?</h1>
                <div className="aboutCards">
                    <div className="getAbout">
                        <h3>Ask for assistance</h3>
                        <Link to='' >Learn More</Link>
                    </div>
                    <div className="getAbout">
                        <h3>Ask for assistance</h3>
                        <Link to='' >Learn More</Link>
                    </div>
                    <div className="getAbout">
                        <h3>Ask for assistance</h3>
                        <Link to='' >Learn More</Link>
                    </div>
                    <div className="getAbout">
                        <h3>Ask for assistance</h3>
                        <Link to='' >Learn More</Link>
                    </div>
                    <div className="getAbout">
                        <h3>Ask for assistance</h3>
                        <Link to='' >Learn More</Link>
                    </div>
                    <div className="getAbout">
                        <h3>Ask for assistance</h3>
                        <Link to='' >Learn More</Link>
                    </div>
                </div>
            </div>
        </>
    )
}

export default InfoCards;