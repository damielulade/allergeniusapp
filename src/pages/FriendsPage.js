import React from "react";
import MainHeaderVariant from "../components/MainHeaderVariant";
import FriendsCard from "../components/FriendsCard";

export default function FriendsPage() {
  return (
      <div className = "section">
          <div class = "main">
              <MainHeaderVariant />
              <div className="container-other">
                  <h2 id="friends-title">Friends</h2>
                  <FriendsCard />
                  <FriendsCard />
                  <FriendsCard />
              </div>
          </div>
      </div>
  )
}