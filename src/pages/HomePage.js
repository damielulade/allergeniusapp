import React from "react";
import SidebarRight from "../components/EmptySidebar";
import Main from "../components/Main";
import SidebarLeft from "../components/SidebarLeft";

export default function HomePage() {
  return (    
		<div className='section'>
      <SidebarLeft />
      <Main />
      <SidebarRight />
    </div>
  )
}