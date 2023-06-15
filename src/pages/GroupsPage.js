import React, { useEffect, useState } from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import GroupCard from "../components/GroupCard";
import { Link } from "react-router-dom";
import axios from "axios";

export default function GroupsPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      axios
        .get(`/api/get_groups`)
        .then((response) => setData(response.data))
        .catch((error) => console.log(error));
    };
    fetchData();
  }, []);

  const addGroup = () => {
    const group = document.getElementById("search-groups-input").value;
    if (group) {
      axios
        .get(`/api/add_group/${group}`)
        .then((response) => setData(response.data))
        .catch((error) => console.log(error));
      // window.location.reload(false);
    }
  };

  const removeGroup = (group) => {
    axios
      .get(`/api/remove_group/${group}`)
      .then((response) => setData(response.data))
      .catch((error) => console.log(error));
    // window.location.reload(false);
  };

  const addUserToGroup = (event) => {};

  const removeUserFromGroup = (event) => {};

  var groups = Object.entries(data).map((group) => {
    return (
      <GroupCard
        key={group}
        name={group[0]}
        members={group[1]}
        removeGroup={removeGroup}
        addUser={addUserToGroup}
        removeUser={removeUserFromGroup}
      />
    );
  });

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-friends">
          <h2 id="friends-ID-title">Create a new group of friends </h2>
          <div id="search-groups">
            <input
              type="text"
              placeholder="Enter group name..."
              id="search-groups-input"
            />
            <button id="search-friends-button" onClick={addGroup}>
              <span>+</span>
            </button>
          </div>
          <h2 id="friends-title">Existing Groups</h2>
          <div className="friends-scrollable">{groups}</div>
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
