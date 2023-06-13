import React, { useRef } from 'react';
import { Link, useNavigate } from "react-router-dom";
import friends_img from "../../static/images/friends.png";
import account_img from "../../static/images/account.png";
import MainHeader from "./MainHeader";
import MapComponent from "../map/Map";
import MapColorKey from "../map/MapColorKey"

export default function Main() {
    const inputRef = useRef(null);

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

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            routeChange();
        }
    };

    return (
        <div className = "main">
            <MainHeader />
            <div className = "container-index">
                <MapComponent />
                <div className="map-block">
                    <div id="search-box">
                        {/* <input type="text" placeholder="Search..." id = "search-input" ref={inputRef} onKeyDown={handleKeyPress}/>
                        <button onClick ={routeChange} id = "search-button"><span>⌕</span></button> */}
                    </div>
                    <Link to="/filter" id="filter-button">
                        <span>Filter</span>
                    </Link>
                </div>
                <MapColorKey />
            </div>
            <div className = "button-bar">
                <Link to="/friends" id = "friends-button">
                    <img src={friends_img} id = "friends-img" alt = "temp"/>
                    <span>Friends</span>
                </Link>
                <Link to="/account" id = "account-button">
                    <img src={account_img} id = "account-img" alt = "temp"/>
                    <span>Account</span>
                </Link>
            </div>
        </div>
  )
}