import React, { useEffect, useState } from "react";
import Main from "../components/main/Main";
import { Link } from "react-router-dom";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import axios from "axios";

export default function GroupsPage() {
  const [data, setData] = useState([]);

  // const baseURL = "http://localhost:5000"; // development
  const baseURL = "" // production

  useEffect(() => {
    const fetchData = () => {
      axios
        .get(`${baseURL}/getFirstUser`)
        .then((response) => {
          console.log(response.data)
          setData(response.data);
        })
        .catch((error) => console.log(error));
    };
    fetchData();
  }, []);

  const groups = data.map((user) => {
    // const grp = user.group;
    return (
      // <FriendsCard
      //   key={user.firstName}
      //   firstName={user.firstName}
      //   lastName={user.lastName}
      //   allergens={user.allergens}
      // />
      <div></div>
    );
  });

  return (
    <div className="section">
      <div class="main">
        <MainHeaderVariant />
        <div className="container-other">

          <h2 id="friends-ID-title">Create a new group of friends </h2>
          <div id="search-friends">
            <input
              type="text"
              placeholder="Enter group name..."
              id="search-friends-input"
            />
            <button id="search-friends-button">
              <span>+</span>
            </button>
          </div>
          <h2 id="friends-title">Existing Groups</h2>
          {groups}
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
