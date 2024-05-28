import React from 'react';
import "./AuthPageStyles.css";

export default function LoginPage() {
    return (
        <div className='form_container'>
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
