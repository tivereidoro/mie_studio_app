import {
  BrowserRouter,
} from "react-router-dom";
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import LoginPage from "./components/LoginPage";
import SignupPage from "./components/SignupPage";
import Player from "./components/Player";


// Create routers for app navigation

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Player />
      {/* <LoginPage />
      <SignupPage /> */}
    </BrowserRouter>
  </React.StrictMode>
);
