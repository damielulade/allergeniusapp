import React from "react";
import userimg from '../static/images/user.png'

export default function FriendsCard() {
  return (
    <div id="friend1">
        <div id = "friend-profile-picture">
            <img src={userimg} id = "friends-page-img" alt = "temp"/>
        </div>
        <div id = "friend-description-box">
            <p id="friend1-name">Lorem Ipsum</p>
            <p id="friends-desc">text text text</p>
        </div>
      {/* <img src={userimg} id="userimg1" /> */}
    </div>
  )
}



