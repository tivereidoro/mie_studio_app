import React from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import "./playerStyle.css";
import bgImage from "../assets/earpiece.jpg"
import albumArt from "../assets/album_art.jpg";
// import axios from "axios";
import axiosInstance from './api/axiosInstance';

export default function Tracks() {
    axiosInstance.get("/api/v1/tracks")
        .then((res) => {
            console.log(res);
        })
        .catch((err) => console.log(err));

    return (

        <div className='player_container'>
            <img src={bgImage} alt="bg image" className="bg_img" />

            <div className='player'>
                <div className="list_body">
                    <div className='search_bar'>
                        <input className='search_text' type='search' />
                    </div>

                    <div className='list_item'>
                        <div className='song'>
                            <img src={albumArt} style={{ width: '20px', height: '20px' }} />
                        </div>
                        <p className='song_title'>Song Title</p>
                        <p className='song_artist'>Song Artist</p>
                        <p className='song_duration'>Duration</p>
                    </div>


                    <div className='list_item'>
                        <div className='song'>
                            <img src={albumArt} style={{ width: '20px', height: '20px' }} />
                        </div>
                        <p className='song_title'>Song Title</p>
                        <p className='song_artist'>Song Artist</p>
                        <p className='song_duration'>Duration</p>
                    </div>

                </div>
            </div>

        </div>
    )
}
