import React from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './playerStyle.css'
import bgImage from "../assets/earpiece.jpg"
import albumArt from "../assets/album_art.jpg";

export default function Player() {
    return (
        <div className='player_container'>
            <img src={bgImage} alt="bg image" className="bg_img" />

            <div className='player'>
                <div className="player_body">
                    <div className="body_cover">
                        <ul className="list list_cover">
                            <li>
                                <a className="list_link" href=""><i className="bi bi-list"></i></a>
                            </li>

                            <li>
                                <a className="list_link" href=""></a>
                            </li>

                            <li>
                                <a className="list_link" href=""><i className="bi bi-search"></i></a>
                            </li>
                        </ul>

                        <img src={albumArt} alt="Album cover" />

                        <div className="range"></div>
                    </div>

                    <div className="body_info">
                        <div className="info_song">Song Title</div>

                        <div className="info_artist">Song Artist Name</div>
                    </div>

                    <div className="body_buttons">
                        <ul className="list list_buttons">
                            <li><a href="#" className="list_link"><i className="bi bi-skip-backward-fill"></i></a></li>

                            <li><a href="#" className="list_link"><i className="bi bi-play-circle"></i></a></li>

                            <li><a href="#" className="list_link"><i className="bi bi-skip-forward-fill"></i></a></li>
                        </ul>
                    </div>
                </div>

                <div className="player_footer">
                    <ul className="list list_footer">
                        <li><a href="#" className="list_link"><i className="bi bi-heart"></i></a></li>

                        <li><a href="#" className="list_link"><i className="bi bi-shuffle"></i></a></li>

                        <li><a href="#" className="list_link"><i className="bi bi-repeat"></i></a></li>

                    </ul>
                </div>

                {/* <div className='sticky'>This is a sticky demo</div> */}
            </div>

        </div>
    )
}
