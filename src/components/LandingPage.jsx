import React from 'react';
import "./landing.css"
import { Link } from 'react-router-dom';

export default function LandingPage() {
    return (
        <>
            <div className='wrapper'>
                <div className='header'>
                    <h4>MieStudio</h4>

                    <div className='content'>
                        <h2>Escape into sound.<br></br> Feel the rhythm of NOW!</h2>
                        <div className="buttons">
                            <Link className="button" to="/login"><i class="bi bi-music-note-list" /> &nbsp;Welcome</Link>
                        </div>
                    </div>

                    <img className="curve" src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/626071/bottom-curve_copy.svg" />
                    <img className="waves" src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/626071/waves_copy.svg" />
                </div>
            </div>

            {/* <div className="background"></div> */}
        </>
    )
}
