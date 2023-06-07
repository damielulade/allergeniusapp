import React from "react";
import { Link } from "react-router-dom";
import mapimg from "../static/images/staticmap1.png";
import friendsimg from "../static/images/friends.png";
import accountimg from "../static/images/account.png";
import MainHeader from "./MainHeader";

export default function Main() {
  return (    
		<div className = "main">
			<MainHeader />	
			<div className = "container">
				<img src={mapimg} id="mapimg" />
        <div className="map-block">
          <div id="search-box">
            <input type="text" placeholder="Search..." id = "search-input" />
            <button onClick = "exampleQuery()" id = "search-button">⌕</button>
             {/* @TODO: fix/replace this button  */}
          </div>
					<Link to="/filter" id="filter-button">
            <button> Filter </button>
            </Link>
        </div>
			</div>	
      <div className = "button-bar">
        <Link to="/friends" id = "friends-button">
          <img src={friendsimg} id="friendsimg" />
        </Link>
        <Link to="/account" id = "account-button">
          <img src={accountimg} id="accountimg" />
        </Link>
      </div>  
		</div>
  )
}