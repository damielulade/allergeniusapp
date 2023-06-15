import React, { useEffect, useState } from "react";
import { useParams } from "react-router";
import MainHeaderVariant from "../main/MainHeaderVariant";
import axios from "axios";
import FriendsCard from "../FriendsCard";

export default function AddUserToGroup(props) {
  const { id } = useParams();

  const [friends, setFriends] = useState([]);
  const [currentMembers, setCurrentMembers] = useState([]);

  useEffect(() => {
    const fetchFriends = () => {
      axios
        .get(`/api/friends/live`)
        .then((response) => {
          if (!(response.data === undefined)) {
            setFriends(Object.entries(response.data));
          }
        })
        .catch((error) => console.log(error));
    };
    fetchFriends();
  }, []);

  useEffect(() => {
    const fetchMembers = () => {
      axios
        .get(`/api/groups`)
        .then((response) => {
          if (!(response.data === undefined)) {
            setCurrentMembers(response.data[id]);
          }
        })
        .catch((error) => console.log(error));
    };
    fetchMembers();
  }, [id]);

  const addFriendToGroup = (friend) => {
    axios
      .post(`/api/groups`, {
        mode: "member",
        action: "add",
        member: friend,
        groupName: id,
      })
      .then(() => {})
      .catch((error) => console.log(error));
    axios
      .get("/api/update_db/groups")
      .then(() => {})
      .catch((error) => console.log(error));
    window.location.href = `/groups`;
  };

  var friendsDisplay = friends
    .filter((friend) => !currentMembers.includes(friend[0]))
    .map((friend) => (
      <div id={friend} onClick={() => addFriendToGroup(friend[0])}>
        <FriendsCard
          key={friend}
          id={friend[0]}
          info={friend[1]}
          displayAllergens={false}
        />
      </div>
    ));

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant path="/groups" />
        <div className="container-friends">
          <h2 id="friends-ID-title">
            {friendsDisplay.length !== 0 && `Pick a friend to add to group ${id}`}
            {friendsDisplay.length === 0 && `There are no friends who aren't already in the group ${id}.`}
          </h2>
          <div className="friends-scrollable">{friendsDisplay}</div>
        </div>
      </div>
    </div>
  );
}
