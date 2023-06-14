import React, { useEffect, useState } from "react";
import axios from 'axios'
import userimg from "../static/images/user.png";

export default function FriendsCard(props) {

  return (
    <div id="friend1">
      <div id="friend-profile-picture">
        <img src={userimg} id="friends-page-img" alt="temp" />
      </div>
      <div id="friend-description-box">
        <p id="friend1-name">{props.firstName} {props.lastName}</p>
        <p id="friends-desc">Allergens: {props.allergens}</p>
      </div>
      {/* <img src={userimg} id="userimg1" /> */}
    </div>
  );
}
