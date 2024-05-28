import React from 'react'
import './playerStyle.css'
import bgImage from "../assets/music.jpg"

export default function Player() {
    return (
        <div className='player_container'>
            <img src={bgImage} alt='background image' className='bg_image' />

            <div className='player_ui'>
                <div>Hello</div>
            </div>

            <div className='control_panel'>
                <div>Back Forward</div>
            </div>
        </div>
    )
}
