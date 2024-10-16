// import React, { Component } from 'react';

// class ErrorBoundary extends Component {
//     constructor(props) {
//         super(props);
//         this.state = { hasError: false };
//     }

//     static getDerivedStateFromError(error) {
//         // Updating state so the next render to show the fallback UI.
//         return { hasError: true };
//     }

//     componentDidCatch(error, errorInfo) {
//         // Logging the error to an error reporting service
//         console.error("ErrorBoundary caught an error", error, errorInfo);
//     }

//     render() {
//         if (this.state.hasError) {
//             // Rendering custom fallback UI
//             return <h1>Something went wrong. Please try again later.</h1>;
//         }

//         return this.props.children; 
//     }
// }

// export default ErrorBoundary;
