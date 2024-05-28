import React from 'react';
import "./AuthPageStyle.css";
import bgImage from "../assets/music.jpg"

export default function LoginPage() {
    return (
        <div className='form_container'>
            <img src={bgImage} alt="login image" class="login__img" />


            <form action="" className="form">
                <h1 className="form__title">Log In</h1>

                <div className="form__div">
                    <input type="text" className="form__input" placeholder=" " />
                    <label for="" className="form__label">Email</label>
                </div>

                <div className="form__div">
                    <input type="password" className="form__input" placeholder=" " />
                    <label for="" className="form__label">Password</label>
                </div>

                <input type="submit" className="form__button" value="Log In" />
            </form>
        </div>
    )
}
