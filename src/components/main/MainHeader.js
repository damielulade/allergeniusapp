import React from "react";
import { Link } from "react-router-dom";
import settings from "../../static/images/settings.png";

export default function MainHeader() {
  return (
    <div className = "top-bar">
      {/* <Link to="/" id = "back-button"><span>〈</span></Link> */}
      <div id="back-button"></div>
      <div id="top-title">Allergenius</div>
      <Link to="/settings" id = "settings-button"><img src={settings} id = "settings-img" alt = "temp"/></Link>
    </div>
  )
}