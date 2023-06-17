import React, { useEffect, useState } from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import GroupCard from "../components/GroupCard";
import { Link } from "react-router-dom";
import axios from "axios";

export default function GroupsPage() {
  const [data, setData] = useState([]);
  const [friends, setFriends] = useState([]);

  const getAllData = async () => {
    try {
      const groupResponse = await axios.get(`/api/groups`);
      const friendsResponse = await axios.get(`/api/friends`);
      setData(groupResponse.data);
      if (!(friendsResponse.data === undefined))
        setFriends(Object.entries(friendsResponse.data));
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getAllData();
  }, []);

  const addGroup = () => {
    const group = document.getElementById("search-groups-input").value;
    if (group) {
      axios
        .post(`/api/groups`, {
          mode: "group",
          action: "add",
          groupName: group,
        })
        .then((response) => setData(response.data))
        .catch((error) => console.log(error));
      // window.location.reload(false);
    }
  };

  const removeGroup = (group) => {
    axios
      .post(`/api/groups`, {
        mode: "group",
        action: "remove",
        groupName: group,
      })
      .then((response) => setData(response.data))
      .catch((error) => console.log(error));
    // window.location.reload(false);
  };

  const addUserToGroup = (group) => {
    window.location.href = `/groups/${group}`;
  };

  const removeUserFromGroup = async (group, member) => {
    try {
      await axios.post(`/api/groups`, {
        mode: "member",
        action: "remove",
        member: member,
        groupName: group,
      });
      await axios.get("/api/update_db/groups");
    } catch (error) {
      console.log(error);
    }
    window.location.href = `/groups`;
  };

  var groups = Object.entries(data).map((group) => {
    return (
      <GroupCard
        key={group}
        name={group[0]}
        members={group[1]}
        friendsData={friends}
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
