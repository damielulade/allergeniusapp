import React from "react";
import MainHeaderVariant from "../components/MainHeaderVariant";
import FriendsCard from "../components/FriendsCard";

export default function FriendsPage() {
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
                  <FriendsCard />
                  <FriendsCard />
                  <FriendsCard />
              </div>
          </div>
      </div>
  )
}