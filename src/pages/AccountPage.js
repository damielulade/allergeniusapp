import React, {useEffect, useState} from "react";
import { Link } from "react-router-dom";
import userimg from "../static/images/user.png";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import axios from "axios";

export default function AccountPage() {
  const signOut = () => {
    axios
      .get("/api/logout")
      .then(() => {
        window.location.href = "/";
      })
      .catch((error) => console.log(error));
  };

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-other">
          <img src={userimg} id="userimg" alt="temp" />
          <p id="accountname">John Doe</p>
          <div id="allergenlist">
            <Link to="/allergens" id="allergen-button">
              <span>My Allergens List</span>
            </Link>
          </div>
          <div id="favoriteslist">
            <Link to="/" id="favourites-button">
              <span>My Favourite Restaurants</span>
            </Link>
          </div>
          <div id="privacysettings">
            <Link to="/privacy" id="privacy-settings-button">
              <span>Privacy Settings</span>
            </Link>
          </div>
          <div id="sign-out-button" onClick={signOut}>
            <span>Sign Out</span>
          </div>
        </div>
      </div>
    </div>
  );
}
