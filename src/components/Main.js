import React from "react";
import { Link } from "react-router-dom";
import mapimg from "../static/images/staticmap2.png";
import friendsimg from "../static/images/friends.png";
import accountimg from "../static/images/account.png";
import MainHeader from "./MainHeader";

export default function Main() {
    function exampleQuery() {
        const query = document.getElementById("search-input").value;
        if (query === "american"){
            window.location.href = 'search';
        } else {
            window.location.href = 'search';
        }
    }

    return (
        <div className = "main">
            <MainHeader />
            <div className = "container-index">
				<img src={mapimg} id="map-img" alt = "temp" />
                <div className="map-block">
                    <div id="search-box">
                        <input type="text" placeholder="Search..." id = "search-input" />
                        <button onClick ={exampleQuery} id = "search-button"><span>⌕</span></button>
                        {/* @TODO: fix/replace this button  */}
                    </div>
                    <Link to="/filter" id="filter-button">
                        {/*<button> Filter </button>*/}
                        <span>Filter</span>
                    </Link>
                </div>
            </div>
            <div className = "button-bar">
                <Link to="/friends" id = "friends-button">
                    <img src={friendsimg} id = "friends-img" alt = "temp"/>
                    <span>Friends</span>
                </Link>
                <Link to="/account" id = "account-button">
                    <img src={accountimg} id = "account-img" alt = "temp"/>
                    <span>Account</span>
                </Link>
            </div>
        </div>
  )
}