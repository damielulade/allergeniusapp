import React from "react";
import userimg from "../static/images/user.png";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Friends />
  </React.StrictMode>
);

export default function Friends() {
  return (    
		<div className = "section">
			<div class = "sidebar-left">
      </div>
      <div class = "main">
        <div class = "top-bar">
          <button onclick = "window.location.href = '/';" id = "back-button">〈</button>  
          <h1 id="top-title">Allergenius</h1>
          <button onclick = "window.location.href = '/';" id = "back1-button">〈</button>  
        </div>	
        <div class="container">
          <h2 id="friends-title">Friends</h2>
          <div id="friend1">
            <h3>Lorem Ipsum</h3>
            <p>text text text</p>
            {/* <img src={userimg} id="userimg1" /> */}
          </div>
          <div id="friend2">
            <h3>Dolor Sit Amet</h3>
            {/* <img src={userimg} id="userimg1" /> */}
            <p>text text text</p>
          </div>
          <div id="friend3">
            <h3>Consectetur Adipiscing Elit</h3>
            <p>text text text</p>
            {/* <img src={userimg} id="userimg1" /> */}
          </div>
        </div>
      </div>
      <div class = "sidebar-right">
      </div>
		</div>
  )
}