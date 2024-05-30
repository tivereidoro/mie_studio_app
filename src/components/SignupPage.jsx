import React from 'react';
import "./AuthPageStyle.css";
import bgImage from "../assets/music.jpg"
import axios from 'axios';

export default function SignupPage() {

    function handleSignup(e) {
        e.preventDefault();
        const username = document.getElementById('userName').value;
        const email = document.getElementById('Email').value;
        const password = document.getElementById('Password').value;

        // console.log(username, email, password);
        axios({
            method: 'post',
            url: 'https://api-miestudio.onrender.com/api/v1/signup',
            data: {
                username: username,
                email: email,
                password: password
            }
        })
            .then((res) => {
                // console.log(res);
                alert("Signup successful");
            })
            .catch((err) => {
                console.log(err);
                alert("Invalid signup details");
            }
            );
    }

    return (
        <div className='form_container'>
            <img src={bgImage} alt="login image" className="login__img" />

            <form action="" className="form">
                <h1 className="form__title">Sign Up</h1>

                <div className="form__div">
                    <input id='userName' type="text" className="form__input" placeholder=" " />
                    <label htmlFor="" className="form__label">Username</label>


                </div>

                <div className="form__div">
                    <input id='Email' type="text" className="form__input" placeholder=" " />
                    <label htmlFor="" className="form__label">Email</label>
                </div>

                <div className="form__div">
                    <input id='Password' type="password" className="form__input" placeholder=" " />
                    <label htmlFor="" className="form__label">Password</label>
                </div>

                <input onClick={handleSignup} type="submit" className="form__button" value="Sign up" />
            </form>
        </div>
    )
}
