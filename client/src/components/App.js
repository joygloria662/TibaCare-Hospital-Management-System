// App.js
import React from 'react';
import { AuthProvider, useAuth } from './AuthContext'; // Import AuthProvider
import Gallery from './Gallery';
import InfoCards from './InfoCards';
import Navbar from './Navbar';
import About from './About'; // Import About component

const images = [
    { url: 'https://img.freepik.com/free-photo/african-american-doctor-patient-doing-consultation_482257-20161.jpg?semt=ais_hybrid', alt: 'xray' },
    { url: 'https://images.pexels.com/photos/263402/pexels-photo-263402.jpeg?auto=compress&cs=tinysrgb&w=400', alt: 'team' },
    { url: 'https://img.freepik.com/free-photo/confident-doctor-hospital-room_9975-22900.jpg?semt=ais_hybrid', alt: 'innovation' }
];

function App() {
    const { user, setUser } = useAuth(); // Use context

    return (
        <>
            <Navbar user={user} setUser={setUser} />
            <div className='App'>
                <Gallery images={images} />
                <InfoCards />
                <About /> {/* Render About component */}
            </div>
        </>
    );
}

const WrappedApp = () => (
    <AuthProvider>
        <App />
    </AuthProvider>
);

export default WrappedApp;

