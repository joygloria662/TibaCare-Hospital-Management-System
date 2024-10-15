import React from "react";
import { Link } from "react-router-dom";

function InfoCards() {
    return (
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
        </div>

    )
}

export default InfoCards;