import React from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import "./playerStyle.css";
import bgImage from "../assets/earpiece.jpg"
import albumArt from "../assets/album_art.jpg";
import SongItem from './SongItem';
// import axios from "axios";
import axiosInstance from './api/axiosInstance';

export default function Tracks() {
    axiosInstance.get("/api/v1/tracks")
        .then((res) => {
            console.log(res.data.tracks);
        })
        .catch((err) => console.log(err));

    const tracks = [
        { title: "Hello", artist: "Adele", duration: "3:23" },
        { title: "Roar", artist: "Dusin Oyekan", duration: "3:46" }
    ]

    return (

        <div className='player_container'>
            <img src={bgImage} alt="bg image" className="bg_img" />

            <div className='player'>
                <div className="list_body">
                    <div className='search_bar'>
                        <input className='search_text' type='search' />
                    </div>

                    <div className='list_item'>
                        {tracks.map((track) => {
                            return (<SongItem songTitle={track.title} songDuration={track.duration} songArtist={track.artist} />)
                        })}
                    </div>



                </div>
            </div>

        </div>
    )
}
