import React from "react";
import userimg from "../static/images/user.png";
import searchresults1 from "../static/images/searchresults1.png";

export default function Search() {
  return (    
		<div className = "section">
			<div class = "sidebar-left">
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
      <div class = "main">
        <div class = "top-bar">
          <button onclick = "window.location.href = '/';" id = "back-button">〈</button>  
          <h1 id="top-title">Allergenius</h1>
          <button onclick = "window.location.href = '/';" id = "back1-button">〈</button>  
        </div>	
        <div class="container">
          <img src={searchresults1} id="searchresults" />
        </div>	
      </div>
      <div class = "sidebar-right">
        <p></p>
      </div>
		</div>
  )
}