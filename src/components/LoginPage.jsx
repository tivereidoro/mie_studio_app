import React from 'react';
import "./AuthPageStyle.css";
import bgImage from "../assets/music.jpg"
import axios from "axios";
import axiosInstance from "./api/axiosInstance";


export default function LoginPage() {
    function handleLogin(e) {
        e.preventDefault();
        const email = document.getElementById('Email').value;
        const passwd = document.getElementById('Password').value;

        // console.log(email, passwd);
        axios({
            method: 'post',
            url: '/api/v1/login',
            data: {
                email: email,
                password: passwd
            }
        })
            .then((res) => {
                // console.log(res);
                // alert("Login successful");

                window.location.href = '/tracks';
            })
            .catch((err) => {
                console.log(err);
                alert("Invalid login details");
            });
    }


    return (
        <div className='form_container'>
            <img src={bgImage} alt="login image" className="login__img" />


            <form action="" className="form">
                <h1 className="form__title">Log In</h1>

                <div className="form__div">
                    <input id='Email' type="text" className="form__input" placeholder=" " />
                    <label htmlFor="" className="form__label">Email</label>
                </div>

                <div className="form__div">
                    <input id='Password' type="password" className="form__input" placeholder=" " />
                    <label htmlFor="" className="form__label">Password</label>
                </div>

                <input onClick={handleLogin} type="submit" className="form__button" value="Log In" />
            </form>
        </div>
    )
}
