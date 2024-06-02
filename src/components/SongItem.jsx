import React from 'react';
import albumArt from "../assets/album_art.jpg";

export default function SongItem({ songTitle = "Title", songArtist = "Artist", songDuration }) {
    return (
        <>

            <div className='song'>
                <img src={albumArt} style={{ width: '20px', height: '20px' }} />
            </div>

            <p className='song_title'>{songTitle}</p>
            <p className='song_artist'>{songArtist}</p>
            <p className='song_duration'>{songDuration}</p>

        </>
    )
}
