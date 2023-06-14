import React, { useEffect, useState } from "react";

function GroupMember(props) {
  return (
    <div id="group-member-card">
      <div id="group-member-name">
        <p>{props.member}</p>
      </div>
      <button id="group-remove-user-button" onClick={props.removeUser}>
        <span>-</span>
      </button>
    </div>
  );
}

export default function GroupCard(props) {
  const memberCards = Object.values(props.members).map((member, index) => {
    return <GroupMember key={index} member={member} />;
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
        <button id="group-add-user-button" onClick={props.addUser}>
          <span>+</span>
        </button>
        <button id="group-remove-user-button" onClick={() => props.removeGroup(props.name)}>
          <span>X</span>
        </button>
        <button id="group-dropdown-button" onClick={viewDropdown}>
          <span>^</span>
        </button>
      </div>
      {dropdownState && <div id="group-dropdown">{memberCards}</div>}
    </div>
  );
}
