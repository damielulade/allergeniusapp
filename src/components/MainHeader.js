import React from "react";
import { Link } from "react-router-dom";

export default function MainHeader() {
  return (
    <div className = "top-bar">
      <Link to="/" id = "back-button"><span>〈</span></Link>
      <div id="top-title">Allergenius</div>
      <Link to="/settings" id = "settings-button"><span>⚙</span></Link>
    </div>
  )
}