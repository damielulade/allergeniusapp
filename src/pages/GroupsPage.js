import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import axios from "axios";
import GroupCard from "../components/GroupCard";

export default function GroupsPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const sse = new EventSource("api/get_first_user");

    function handleStream(e) {
      setData(JSON.parse(e.data));
    }

    sse.onmessage = (e) => {
      console.log(JSON.parse(e.data));
      handleStream(e);
    };

    sse.onerror = (e) => {
      sse.close();
    };

    return () => {
      sse.close();
    };
  });

  var groupsDisplay = data.map((user) => {
    var res = [];
    for (let group in user.groups) {
      res.push(
        <GroupCard key={group} name={group} members={user.groups[group]} />
      );
    }
    return res;
  });

  const addGroup = (event) => {
    const group = document.getElementById("search-groups-input").value;
    if (group) {
      axios
        .get(`/api/add_group/${group}`)
        .then([])
        .catch((error) => console.log(error));
    }
  };

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
          <div className="friends-scrollable">{groupsDisplay}</div>
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
