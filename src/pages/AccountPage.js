import React from "react";
import { Link, useNavigate } from "react-router-dom";
import userimg from "../static/images/user.png"
import MainHeaderVariant from "../components/MainHeaderVariant";

export default function AccountPage() {
  return (
    <div className = "section">
      <div class = "main">
        <MainHeaderVariant />
          <div className="container-other">
              <img src={userimg} id="userimg" alt = "temp"/>
              <p id="accountname">John Doe</p>
              <div id="allergenlist">
                  <Link to="/allergens" id = "allergen-button">
                    <span>My Allergens List (1) </span>
                  </Link>
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
    </div>
  )
}