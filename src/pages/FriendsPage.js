import React from "react";
import MainHeaderVariant from "../components/MainHeaderVariant";
import SidebarRight from "../components/SidebarRight";
import FriendsCard from "../components/FriendsCard";

export default function FriendsPage() {
  return (    
		<div className = "section">
			<div class = "sidebar-left">
      </div>
      <div class = "main">
        <MainHeaderVariant />
        <div className="container-other">
          <h2 id="friends-title">Friends</h2>
          <FriendsCard />
          <FriendsCard />
          <FriendsCard />
        </div>
      </div>
      <SidebarRight />
		</div>
  )
}