import React from "react";
import userimg from "../static/images/user.png"
import MainHeader from "../components/MainHeader";

export default function AccountPage() {
  return (
    <div className = "section">
      <div class = "sidebar-left">
      </div>
      <div class = "main">
        <MainHeader />	
        <div class="container">
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
      </div>
      <div class = "sidebar-right">
      </div>
    </div>
  )
}