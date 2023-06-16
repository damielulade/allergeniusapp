import React, { useState } from "react";

function GroupMember(props) {
  return (
    <div id="group-member-card">
      <div id="group-member-name">
        <p>{props.member}</p>
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
    return (
      <GroupMember
        key={index}
        member={member}
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
          <section>
            <button
              id="group-add-user-button"
              onClick={() => {
                props.addUser(props.name, props.members);
              }}
            >
              <span>+</span>
            </button>
            <button id="group-dropdown-button" onClick={viewDropdown}>
              <span>^</span>
            </button>
            <button
              id="group-remove-user-button"
              onClick={() => props.removeGroup(props.name)}
            >
              <span>X</span>
            </button>
          </section>
        )}
      </div>
      {dropdownState && <div id="group-dropdown">{memberCards}</div>}
      {/* {false && <AddUserToGroup members={props.members}/>} */}
    </div>
  );
}
