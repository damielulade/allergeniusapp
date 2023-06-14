import {Link} from "react-router-dom";
import React from "react";

export default function MainHeaderVariant() {
  return (
    <div className = "top-bar">
      <Link to="/home" id = "back-button"><span>〈</span></Link>
      <div id="top-title">Allergenius</div>
      <Link to="/" id = "back1-button"><span>〈</span></Link>
    </div>
  )
}