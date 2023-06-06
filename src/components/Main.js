import React from "react";
import mapimg from "../static/images/staticmap1.png";
import friendsimg from "../static/images/friends.png";
import accountimg from "../static/images/account.png";

export default function Main() {
  return (    
		<div className = "main">
			<div className = "top-bar">
        <button onclick = "window.location.href = '/';" id = "back-button">〈</button>  
				<h1 id="top-title">Allergenius</h1>
        <button onclick = "window.location.href = '/';" id = "back1-button">〈</button>  
			</div>	
			<div className = "container">
				<img src={mapimg} id="mapimg" />
        <div className="map-block">
          <div id="search-box">
            <input type="text" placeholder="Search..." id = "search-input" />
            <button onclick = "exampleQuery()" id = "search-button">⌕</button>  
          </div>
					<button onclick = "window.location.href = 'filter';" id = "filter-button"> Filter </button>
        </div>
			</div>	
      <div className = "button-bar">
        <button onclick = "window.location.href = 'friends';" id = "friends-button">
          <img src={friendsimg} id="friendsimg" />
        </button>  
        <button onclick = "window.location.href = 'account';" id = "account-button">
          <img src={accountimg} id="accountimg" />
        </button>  
      </div>  
		</div>
  )
}