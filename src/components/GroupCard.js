import React, { useState } from "react";
import FriendsCard from "./FriendsCard";

function GroupMember(props) {
  return (
    <div id="group-member-card">
      <div id="group-member-name">
        <FriendsCard
          key={props.member}
          id={props.member}
          info={props.info}
          displayAllergens={false}
          hideProfilePhoto={true}
          noBorder={true}
        />
      </div>
      <button
        id="group-remove-user-button"
        onClick={() => props.removeUser(props.group, props.member)}
      >
        <span>-</span>
      </button>
    </div>
  );
}

export default function GroupCard(props) {
  const memberCards = Object.values(props.members).map((member, index) => {
    const memberInfo = props.friendsData.find((friend) => friend[0] === member);
    return (
      <GroupMember
        key={index}
        member={member}
        info={memberInfo[1]}
        group={props.name}
        removeUser={props.removeUser}
      />
    );
  });

  const [dropdownState, setDropdownState] = useState(false);

  const viewDropdown = () => {
    setDropdownState(!dropdownState);
  };

  return (
    <div id="group">
      <div id="group-header">
        <div id="group-title">
          <h3>{props.name}</h3>
        </div>
        {!props.hideButtons && (
          <section id="group-button-bar">
            <button
              id="group-add-user-button"
              onClick={() => {
                props.addUser(props.name, props.members);
              }}
            >
              <span>+</span>
            </button>
            <button id="group-dropdown-button" onClick={viewDropdown}>
              <span>{dropdownState ? "∨" : "∧"}</span>
            </button>
            <button
              id="group-delete-group-button"
              onClick={() => props.removeGroup(props.name)}
            >
              <span>x</span>
            </button>
          </section>
        )}
      </div>
      {dropdownState && <div id="group-dropdown">{memberCards}</div>}
    </div>
  );
}
