import React from "react";
import MainHeader from "../components/MainHeader";
import SidebarRight from "../components/EmptySidebar";
import FriendsCard from "../components/FriendsCard";

export default function FriendsPage() {
  return (    
		<div className = "section">
			<div class = "sidebar-left">
      </div>
      <div class = "main">
        <MainHeader />
        <div class="container">
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