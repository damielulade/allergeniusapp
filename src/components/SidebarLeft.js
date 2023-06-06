import React from "react";
import userimg from "../static/images/user.png";

export default function SidebarLeft() {
  return (
    <div className="sidebar-left">
      <img src={userimg} id="userimg" />
      <p id="accountname">John Doe</p>
      <div id="allergenlist">
        <p>My Allergens List (1)</p>
      </div>
      <div id="favoriteslist">
        <p>My Favourite Restaurants (3)</p>
      </div>
      <div id="privacysettings">
        <p>Privacy Settings</p>
      </div>
      <p id="signout">Sign Out</p>
    </div>
  )
}