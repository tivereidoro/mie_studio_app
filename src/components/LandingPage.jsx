import React from 'react';
import "./landing.css"
import { Link } from 'react-router-dom';

export default function LandingPage() {
    return (
        <>
            <div className="container">
                <nav>
                    <div className="logo">
                        <Link to="/"><span>Mie-</span>Studio<span>.</span></Link>
                    </div>
                    <ul>
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/about">About</Link></li>

                    </ul>
                    <div className="buttons">
                        <Link to="/login" className="login_btn">Log in</Link>
                        <Link to="/signup" className="btn">Sign up</Link>
                    </div>
                </nav>


                <div className="content">
                    <h2>Welcome,<br />to a music experience..</h2>
                    <p>Vibe to the rhythm, and flow with the sound</p>
                </div>

                <div className="cta_link">
                    <Link to="/login" className="cta"><i className="bi bi-music-note-list" /> &nbsp;Let's go</Link>
                </div>
            </div>
        </>
    )
}
