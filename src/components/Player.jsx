import React from 'react'
import bgImage from "../assets/music.jpg"

export default function Player() {
    return (
        <div className='player_container'>
            <img src={bgImage} alt='background image' className='bg_image' />

            <div className='player_container'>
                <div></div>
            </div>
        </div>
    )
}
