import React, { useEffect, useState } from "react";
import axios from "axios";
import userimg from "../static/images/user.png";

export default function FriendsCard(props) {
  const [dropdownState, setDropdownState] = useState(false);

  const viewDetails = () => {
    setDropdownState(!dropdownState);
  };

  const allergens = props.info.allergens.map((allergen) => {
    return <p>- {allergen}</p>;
  });

  return (
    <div id="friend1">
      <div id="friend-profile-picture">
        <img src={userimg} id="friends-page-img" alt="temp" />
      </div>
      <div id="friend-description-box">
        <p id="friend1-name">
          {props.info.firstName} {props.info.lastName}
        </p>
        <p id="friends-desc">{props.info.email}</p>
      </div>
      {props.info.privacy && (
        <div id="friend-delete-button" onClick={viewDetails}>
          <p>see allergens</p>
        </div>
      )}
      {dropdownState && (
        <div>
          <p id="friends-desc">Allergens</p>
          <div id="friends-desc">{allergens}</div>
        </div>
      )}
      {/* <img src={userimg} id="userimg1" /> */}
    </div>
  );
}
