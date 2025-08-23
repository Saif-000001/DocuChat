import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css'; // Import Tailwind CSS and global styles
import App from './App.jsx'; // Import the root App component
/**
 * Create a React root and render the application
 * -----------------------------------------------
 * - StrictMode helps highlight potential problems in development
 * - Renders <App /> into the HTML element with id="root"
 */
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
