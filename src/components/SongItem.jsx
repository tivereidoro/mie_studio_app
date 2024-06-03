import React from 'react';
import "./playerStyle.css";

export default function SongItem({ songTitle = "Title", songArtist = "Artist", songDuration }) {
    return (
        <>
            <li className='song_list_item'>
                <div>
                    <span className='song_title'>{songTitle}</span>
                    <p className='song_artist'>{songArtist}</p>
                </div>

                <span className='song_duration'>{songDuration}</span>
            </li>
        </>
    )
}
