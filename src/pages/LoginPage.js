import React, { useState, useRef } from "react";
import axios from "axios";
import LoginHeader from "../components/main/LoginHeader";

export default function LoginPage() {
  const [registerEmail, setRegisterEmail] = useState("");
  const [registerPassword, setRegisterPassword] = useState("");
  const [loginEmail, setLoginEmail] = useState("");
  const [loginPassword, setLoginPassword] = useState("");

  const [age, setAge] = useState("")
  const [fn, setFN] = useState("")
  const [ln, setLN] = useState("")

  const handleRegister = () => {
    // Send registration request to the backend using Axios
    axios
      .post(`/api/register`, {
        email: registerEmail,
        password: registerPassword,
        age: age,
        firstName: fn,
        lastName: ln
      })
      .then((response) => {
        console.log(response.data);
        // Handle successful registration
        window.location.href = "/home";
      })
      .catch((error) => {
        console.error("Error:", error.response.data);
        // Handle registration error
      });
  };

  const handleLogin = () => {
    // Send login request to the backend using Axios
    axios
      .post(`/api/login`, {
        email: loginEmail,
        password: loginPassword,
      })
      .then((response) => {
        console.log(response.data);
        // Handle successful login
        window.location.href = "/home"
      })
      .catch((error) => {
        console.error("Error:", error.response.data);
        // Handle login error
      });
  };

  return (
      <div className = "main">
          <LoginHeader />
          <div className = "container-login">
              <div className = "register-block">
                  <h2 id = "register-title">Registration</h2>
                  <input
                      type="email"
                      placeholder="Email"
                      value={registerEmail}
                      className = "register-input-block"
                      onChange={(e) => setRegisterEmail(e.target.value)}
                  />
                  <br />
                  <input
                      type="password"
                      placeholder="Password longer than 6 letters"
                      value={registerPassword}
                      className = "register-input-block"
                      onChange={(e) => setRegisterPassword(e.target.value)}
                  />
                  <br />
                  <input
                      type="email"
                      placeholder="Age"
                      value={age}
                      className = "register-input-block"
                      onChange={(e) => setAge(e.target.value)}
                  />
                  <br />
                  <input
                      type="email"
                      placeholder="First Name"
                      value={fn}
                      className = "register-input-block"
                      onChange={(e) => setFN(e.target.value)}
                  />
                  <br />
                  <input
                      type="email"
                      placeholder="Last Name"
                      value={ln}
                      className = "register-input-block"
                      onChange={(e) => setLN(e.target.value)}
                  />
                  <br />
                  <button className = 'register-button' onClick={handleRegister}>Register</button>
              </div>
              <div className = "login-block">
                  <h2 id = "login-title">Login</h2>
                  <input
                      type="email"
                      placeholder="Email"
                      value={loginEmail}
                      className = "login-input-block"
                      onChange={(e) => setLoginEmail(e.target.value)}
                  />
                  <br />
                  <input
                      type="password"
                      placeholder="Password"
                      value={loginPassword}
                      className = "login-input-block"
                      onChange={(e) => setLoginPassword(e.target.value)}
                  />
                  <br />
                  <button className = 'login-button' onClick={handleLogin}>Login</button>
              </div>
          </div>
      </div>
  );
}

