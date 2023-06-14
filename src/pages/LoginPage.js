import React, { useState } from "react";
import axios from "axios";

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
    <div>
      <h2>Registration</h2>
      <input
        type="email"
        placeholder="Email"
        value={registerEmail}
        onChange={(e) => setRegisterEmail(e.target.value)}
      />
      <br />
      <input
        type="password"
        placeholder="Password longer than 6 letters"
        value={registerPassword}
        onChange={(e) => setRegisterPassword(e.target.value)}
      />
      <br />
      <input 
        type="email"
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
      />
      <br />
      <input 
        type="email"
        placeholder="First Name"
        value={fn}
        onChange={(e) => setFN(e.target.value)}
      />
      <br />
      <input 
        type="email"
        placeholder="Last Name"
        value={ln}
        onChange={(e) => setLN(e.target.value)}
      />
      <button onClick={handleRegister}>Register</button>
      <h2>Login</h2>
      <input
        type="email"
        placeholder="Email"
        value={loginEmail}
        onChange={(e) => setLoginEmail(e.target.value)}
      />
      <br />
      <input
        type="password"
        placeholder="Password"
        value={loginPassword}
        onChange={(e) => setLoginPassword(e.target.value)}
      />
      <br />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

