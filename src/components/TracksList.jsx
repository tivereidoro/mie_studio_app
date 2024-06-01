import React from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import "./playerStyle.css";
import bgImage from "../assets/earpiece.jpg"
import albumArt from "../assets/album_art.jpg";
import SongItem from './SongItem';
// import axios from "axios";
import axiosInstance from './api/axiosInstance';

export default function Tracks() {
    function populateTracks(tracks) {

        const items = []

        Object.entries(tracks).map(([key, value]) => {
            items.push(<SongItem songTitle={value.title} songDuration={value.duration}
                songArtist={'Artiste'} />);
        })
        return (items);

        // tracks.map((track) => {
        //    return (<SongItem songTitle={track.title} songDuration={track.duration} songArtist={track.artist} />)
        // })
    }

    let tracks = {};

    axiosInstance.get("/api/v1/tracks")
        .then((res) => {
            // console.log(res.data.tracks);
            tracks = JSON.parse(JSON.stringify(res.data.tracks));
        })
        .catch((err) => console.log(err));

    // const tracks = [
    //     { title: "Hello", artist: "Adele", duration: "3:23" },
    //     { title: "Roar", artist: "Dusin Oyekan", duration: "3:46" }
    // ]
    console.log(tracks);
    return (
        <div className='player_container'>
            <img src={bgImage} alt="bg image" className="bg_img" />

            <div className='player'>
                <div className="list_body">
                    <div className='search_bar'>
                        <input className='search_text' type='search' />
                    </div>

                    <div className='list_item'>
                        {populateTracks(tracks)}
                    </div>



                </div>
            </div>

        </div>
    )
}
