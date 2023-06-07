import React from "react";
import { Link } from "react-router-dom";

export default function MainHeader() {
  return (
    <div className = "top-bar">
      <Link to="/" id = "back-button">〈</Link>
      <h1 id="top-title">Allergenius</h1>
      <Link to="/" id = "back1-button">〈</Link>      
    </div>
  )
}