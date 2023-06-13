import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import axios from "axios";
import GroupCard from "../components/GroupCard";

export default function GroupsPage() {
  const [data, setData] = useState([]);

  // const baseURL = "http://localhost:5000"; // development
  const baseURL = "" // production

  useEffect(() => {
    const fetchData = () => {
      axios
        .get(`${baseURL}/getFirstUser`)
        .then((response) => {
          setData(response.data);
        })
        .catch((error) => console.log(error));
    };
    fetchData();
  }, []);

  const groups = data.map((user) => {
    var res = [];
    for (let group in user.groups) {
      res.push(
        <GroupCard key={group} name={group} members={user.groups[group]} />
      );
    }
    return res;
  });

  return (
    <div className="section">
      <div className="main">
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
