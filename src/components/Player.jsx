import React from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './playerStyle.css'
import bgImage from "../assets/earpiece.jpg"

export default function Player() {
    return (
        <div className='player_container'>
            <img src={bgImage} alt="bg image" className="bg_img" />

            <div className='player'>
                <div><i className="bi-alarm"></i></div>
            </div>
        </div>
    )
}
