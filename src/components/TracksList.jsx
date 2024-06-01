import React from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import "./playerStyle.css";
import bgImage from "../assets/earpiece.jpg"
import albumArt from "../assets/album_art.jpg";
import SongItem from './SongItem';
import axiosInstance from './api/axiosInstance';
import { useState, useEffect } from 'react';


function TracksList() {

    const tracksTemplate = [
        { title: "Hello", artist: "Adele", duration: "3:23" },
        { title: "Roar", artist: "Dusin Oyekan", duration: "3:46" }
    ]

    const [tracks, setTracks] = useState([]);

    useEffect(() => {
        // This code will run once when the component mounts (onload)
        axiosInstance.get('/api/v1/tracks')
            .then((res) => {
                // Set the state with the fetched data
                // console.log(res.data.tracks)
                setTracks(Object.values(res.data.tracks));
            })
            .catch((err) => console.log(err));
    }, []);

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
                            return (<SongItem songTitle={track.title} songDuration={track.duration} songArtist={'Artist'} key={track.id} />)
                        })}
                    </div>
                </div>
            </div>
        </div>
    )
};

export default TracksList;
