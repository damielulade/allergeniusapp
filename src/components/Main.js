import React from "react";
import { Link, useNavigate } from "react-router-dom";
// import mapimg from "../static/images/staticmap2.png";
import friendsimg from "../static/images/friends.png";
import accountimg from "../static/images/account.png";
import MainHeader from "./MainHeader";
import MapComponent from "./Map";

export default function Main() {
    
    let navigate = useNavigate();
    const routeChange = () => {
        const query = document.getElementById("search-input").value;
        let path; 
        if (query === "american"){
            path = "/search";
        } else {
            path = "/search";
        }
        navigate(path);
    }

    return (
        <div className = "main">
            <MainHeader />
            <div className = "container-index">
				{/*<img src={mapimg} id="map-img" alt = "temp" />*/}
                <MapComponent/>
                <div className="map-block">
                    <div id="search-box">
                        <input type="text" placeholder="Search..." id = "search-input" />
                        <button onClick ={routeChange} id = "search-button"><span>⌕</span></button>
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