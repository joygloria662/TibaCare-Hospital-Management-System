import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="header">
      <div className="logo">
        <img src="/images/logo1.png" alt="TibaCare Logo" />
        <span className="logo-text">TibaCare Hospital Management System</span> {/* Added text */}
      </div>
      <nav className="navbar">
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About Us</Link></li>
          <li><Link to="/departments">Departments</Link></li>
          <li><Link to="/contact">Contact Us</Link></li>
        </ul>
      </nav>
      <div className="auth-actions">
        <button><Link to="/login">Login</Link></button>
        <button><Link to="/logout">Logout</Link></button>
        <button><Link to="/book-appointment">Book Appointment</Link></button>
      </div>
    </header>
  );
};

export default Header;
