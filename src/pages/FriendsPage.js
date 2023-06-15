import React, { useEffect, useState } from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import FriendsCard from "../components/FriendsCard";
import axios from "axios";
import { Link } from "react-router-dom";

export default function FriendsPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      axios
        .get(`/api/friends/live`)
        .then((response) => {
          if (response.data === undefined) {
            console.log(response.data);
          } else {
            console.log(Object.entries(response.data));
            setData(Object.entries(response.data));
          }
        })
        .catch((error) => console.log(error));
    };
    fetchData();
    // console.log(data)
  }, []);

  const [temp, setTemp] = useState(null);

  const findFriend = () => {
    const email = document.getElementById("search-friends-input").value;
    if (email) {
      // var user_key;
      axios
        .get(`/api/user_by_email/${email}`)
        .then((response) => {
          setTemp(response.data);
          // console.log(response.data);
        })
        .catch((error) => console.log(error));
      if (temp) {
        console.log(temp);
        axios
          .post(`/api/friends/live`, {
            mode: "add",
            friendKey: temp,
          })
          .then((response) => setData(response.data))
          .catch((error) => console.log(error));
      }
      // window.location.reload(false);
    }
  };

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-friends">
          <h2 id="friends-ID-title">Search for a user by email</h2>
          <div id="search-friends">
            <input
              type="text"
              placeholder="Search..."
              id="search-friends-input"
            />
            <button id="search-friends-button" onClick={findFriend}>
              {/* <span>⌕</span> */}
              <span>+</span>
            </button>
          </div>
          <h2 id="friends-title">Existing Friends</h2>
          <div className="friends-scrollable">
            {data?.map((friend) => {
              return (
                <FriendsCard
                  key={friend}
                  id={friend[0]}
                  info={friend[1]}
                  displayAllergens={true}
                />
              );
            })}
          </div>
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
