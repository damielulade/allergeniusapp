import React, { useEffect, useState } from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import FriendsCard from "../components/FriendsCard";
import axios from "axios";
import { Link } from "react-router-dom";

export default function FriendsPage() {
  const [data, setData] = useState([]);

  // const baseURL = "http://localhost:5000"; // development
  const baseURL = "" // production

  useEffect(() => {
    const fetchData = () => {
      axios
          .get(`${baseURL}/getUserFriends`)
          .then((response) => {
            setData(response.data);
          })
          .catch((error) => console.log(error));
    };
    fetchData();
  }, []);

  const friends = data.map((user) => {
    return (
      <FriendsCard
        key={user.firstName}
        firstName={user.firstName}
        lastName={user.lastName}
        allergens={user.allergens}
      />
    );
  });

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-other">
          {/* <TwoOptionRadioButton option1={"Friends"} option2={"Groups"} /> */}

          <h2 id="friends-ID-title">Search for a user by user ID</h2>
          <div id="search-friends">
            <input
              type="text"
              placeholder="Search..."
              id="search-friends-input"
            />
            <button id="search-friends-button">
              <span>⌕</span>
            </button>
          </div>
          <h2 id="friends-title">Existing Friends</h2>
          {friends}
        </div>
        <div className="button-bar">
          <Link to="/friends" id="friends-button">
            {/* <img src={friends_img} id="friends-img" alt="temp" /> */}
            <span>View Friends</span>
          </Link>
          <Link to="/groups" id="account-button">
            {/* <img src={account_img} id="account-img" alt="temp" /> */}
            <span>View Groups</span>
          </Link>
        </div>
      </div>
    </div>
  );
}