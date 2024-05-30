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
                <div class="player_body">
                    <div class="body_cover">
                        <ul class="list list_cover">
                            <li>
                                <a class="list_link" href=""><i class="bi bi-list"></i></a>
                            </li>

                            <li>
                                <a class="list_link" href=""></a>
                            </li>

                            <li>
                                <a class="list_link" href=""><i class="bi bi-search"></i></a>
                            </li>
                        </ul>

                        <img src={albumArt} alt="Album cover" />

                        <div class="range"></div>
                    </div>

                    <div class="body_info">
                        <div class="info_song">Song Title</div>

                        <div class="info_artist">Song Artist Name</div>
                    </div>

                    <div class="body_buttons">
                        <ul class="list list_buttons">
                            <li><a href="#" class="list_link"><i class="bi bi-skip-backward-fill"></i></a></li>

                            <li><a href="#" class="list_link"><i class="bi bi-play-circle"></i></a></li>

                            <li><a href="#" class="list_link"><i class="bi bi-skip-forward-fill"></i></a></li>
                        </ul>
                    </div>
                </div>

                <div class="player_footer">
                    <ul class="list list_footer">
                        <li><a href="#" class="list_link"><i class="bi bi-heart"></i></a></li>

                        <li><a href="#" class="list_link"><i class="bi bi-shuffle"></i></a></li>

                        <li><a href="#" class="list_link"><i class="bi bi-repeat"></i></a></li>

                    </ul>
                </div>
            </div>

        </div>
    )
}
