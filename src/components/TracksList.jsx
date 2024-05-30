import React from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import "./playerStyle.css";
// import axios from "axios";
import axiosInstance from './api/axiosInstance';

export default function Tracks() {
    axiosInstance.get("/api/v1/tracks")
        .then((res) => {
            console.log(res);
        })
        .catch((err) => console.log(err));

    return (
        <div className="tracks_container">
            <div className='search_bar'>
                <input className='search_text' type='text' />
                <div>
                    <button><i className="bi bi-search"></i></button>
                </div>
            </div>

            <div className='song_list'>
                <ul>
                    <li id='list_ref'>
                        <div>
                            <p className='song_title'>Song Title</p>
                            <p className='song_artist'>Song Artist</p>
                            <p className='song_duration'>Duration</p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    )
}
