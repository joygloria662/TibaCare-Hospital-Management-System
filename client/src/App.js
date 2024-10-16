import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';  
import Departments from './components/Departments';  
import Doctors from './components/Doctors';  
import Gallery from './components/Gallery';  
import InfoCards from './components/InfoCards';  
import Signup from './components/Signup'; 
import ErrorBoundary from './components/ErrorBoundary'; 

const images = [
  { url: 'https://img.freepik.com/free-photo/african-american-doctor-patient-doing-consultation_482257-20161.jpg?semt=ais_hybrid', alt: 'xray' },
  { url: 'https://images.pexels.com/photos/263402/pexels-photo-263402.jpeg?auto=compress&cs=tinysrgb&w=400', alt: 'team' },
  { url: 'https://img.freepik.com/free-photo/confident-doctor-hospital-room_9975-22900.jpg?semt=ais_hybrid', alt: 'innovation' },
];

const App = () => {
  return (
    <Router>
      <Header />
      <ErrorBoundary>
        <Routes>
          <Route
            path="/"
            element={
              <div className="App">
                <Gallery images={images} />
                <InfoCards />
              </div>
            }
          />
          <Route path="/departments" element={<Departments />} />
          <Route path="/departments/:departmentId" element={<Doctors />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="*" element={<h1>404 Not Found</h1>} /> {/* Catch-all for undefined routes */}
        </Routes>
      </ErrorBoundary>
    </Router>
  );
};

export default App;
