import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './components/App';
import ErrorPage from './components/ErrorPage';
import './index.css';
import LandingPage from './components/homepage/LandingPage';


// Create routers for app navigation
const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: "home/",
    element: <App />,
    errorElement: <ErrorPage />,
  },
  {
    path: "about/",
    element: <AboutPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: "login/",
    element: <LoginPage />,
    errorElement: <ErrorPage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
