import React from 'react'
import { NavLink } from "react-router-dom";

export default function Navbar() {
    return (
        <div id='navbar' className='navbar'>
            <div className='navbar-icon'></div>

            <div className='navbar-links'>
                <ul>
                    <li><NavLink to="/">Home</NavLink></li>
                    <li><NavLink to="/about">About</NavLink></li>
                    <li><NavLink to="/loginPage">Log In</NavLink></li>
                </ul>
            </div>
        </div>
    )
}
