import React, { useEffect, useState } from "react";
import MainHeaderVariant from "../components/MainHeaderVariant";
import FriendsCard from "../components/FriendsCard";
import axios from "axios";

export default function FriendsPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    
    const fetchData = () => {
      axios
        .get("/getUserFriends")
        .then((response) => {
          setData(response.data);
        })
        .catch((error) => console.log(error));
    };
    fetchData();
  }, []);



  const formattedData = data.map(user => {
    return (
        <FriendsCard
            key={user.firstName}
            firstName={user.firstName}
            lastName={user.lastName}
            allergens={user.allergens}
        />
    )
  })

  return (
      <div className = "section">
          <div class = "main">
              <MainHeaderVariant />
              <div className="container-other">
                  <h2 id="friends-ID-title">Search for a user by user ID</h2>
                  <div id = "search-friends">
                        <input type="text" placeholder="Search..." id = "search-friends-input"/>
                        <button id = "search-friends-button"><span>⌕</span></button>
                  </div>
                  <h2 id="friends-title">Existing Friends</h2>
                  {formattedData}
              </div>
          </div>
      </div>
  );
}
