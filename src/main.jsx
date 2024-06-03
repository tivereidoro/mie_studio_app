import {
  createBrowserRouter,
  RouterProvider
} from "react-router-dom";
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import LoginPage from "./components/LoginPage";
import LandingPage from "./components/LandingPage";
import Player from "./components/Player";
import LoginPage from "./components/LoginPage";
import SignupPage from "./components/SignupPage";
import TracksList from "./components/TracksList";


// Create routers for app navigation
const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />
  },
  {
    path: "login",
    element: <LoginPage />
  },
  {
    path: "signup",
    element: <SignupPage />
  },
  {
    path: "tracks",
    element: <TracksList />
  },
  {
    path: 'player',
    element: <Player />
  },
]);

// Render the app
ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
