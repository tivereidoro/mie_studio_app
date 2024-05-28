import React from 'react';
import "./Login.css";

export default function LoginPage() {
    return (
        <div className='loginPage'>
            <form action="" class="form">
                <h1 class="form__title">Sign In</h1>

                <div class="form__div">
                    <input type="text" class="form__input" placeholder=" " />
                    <label for="" class="form__label">Email</label>
                </div>

                <div class="form__div">
                    <input type="password" class="form__input" placeholder=" " />
                    <label for="" class="form__label">Password</label>
                </div>

                <input type="submit" class="form__button" value="Sign In" />
            </form>
        </div>
    )
}
