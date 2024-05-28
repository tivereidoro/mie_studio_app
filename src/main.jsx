import {
  BrowserRouter,
} from "react-router-dom";

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './components/App';
import ErrorPage from './components/ErrorPage';
import './index.css';
import LandingPage from './components/homepage/LandingPage';
import LoginPage from "./components/LoginPage";
import SignupPage from "./components/SignupPage";


// Create routers for app navigation

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      {/* <LoginPage /> */}
      <SignupPage />

      {/* <Routes>
        <Route path="/" element={<LoginPage />} />
      </Routes> */}
    </BrowserRouter>
  </React.StrictMode>
);
