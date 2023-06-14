import React from "react";
import { Link } from "react-router-dom";
import userimg from "../static/images/user.png"
import MainHeaderVariant from "../components/main/MainHeaderVariant";

export default function AccountPage() {
  return (
    <div className = "section">
      <div className = "main">
        <MainHeaderVariant />
          <div className="container-other">
              <img src={userimg} id="userimg" alt = "temp"/>
              <p id="accountname">John Doe</p>
              <div id="allergenlist">
                  <Link to="/allergens" id = "allergen-button">
                    <span>My Allergens List</span>
                  </Link>
              </div>
              <div id="favoriteslist">
                  <Link to="/" id = "favourites-button">
                      <span>My Favourite Restaurants</span>
                  </Link>
              </div>
              <div id="privacysettings">
                  <Link to="/privacy" id = "privacy-settings-button">
                      <span>Privacy Settings</span>
                  </Link>
              </div>
              <Link to="/" id = "sign-out-button">
                  <span>Sign Out</span>
              </Link>
          </div>
      </div>
    </div>
  )
}