import {
  createBrowserRouter,
  RouterProvider
} from "react-router-dom";
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import LoginPage from "./components/LoginPage";
// import SignupPage from "./components/SignupPage";
import Player from "./components/Player";
import LoginPage from "./components/LoginPage";
import SignupPage from "./components/SignupPage";
import TracksList from "./components/TracksList";


// Create routers for app navigation
const router = createBrowserRouter([
  {
    path: "/",
    element: <Player />
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
  }
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
