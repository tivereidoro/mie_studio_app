import React from 'react';
import "./Login.css";
import bgImage from "../assets/earpiece.jpg"

export default function LoginPage() {
    return (
        <div className='loginPage'>
            <img src={bgImage} alt="login image" class="login__img"></img>

            <form action="" className="form">
                <h1 className="form__title">Sign Up</h1>

                <div className="form__div">
                    <input type="text" className="form__input" placeholder=" " />
                    <label for="" className="form__label">Username</label>
                </div>

                <div className="form__div">
                    <input type="text" className="form__input" placeholder=" " />
                    <label for="" className="form__label">Email</label>
                </div>

                <div className="form__div">
                    <input type="password" className="form__input" placeholder=" " />
                    <label for="" className="form__label">Password</label>
                </div>

                <input type="submit" className="form__button" value="Sign up" />
            </form>
        </div>
    )
}
