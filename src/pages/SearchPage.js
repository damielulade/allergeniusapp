import React from "react";
import searchresults1 from "../static/images/searchresults1.png";
import MainHeader from "../components/MainHeader";
import SidebarLeft from "../components/SidebarLeft";
import SidebarRight from "../components/EmptySidebar";

export default function SearchPage() {
  return (    
		<div className = "section">
			<SidebarLeft />
      <div class = "main">
        <MainHeader />
        <div class="container">
          <img src={searchresults1} id="searchresults" />
        </div>	
      </div>
      <SidebarRight />
		</div>
  )
}