import axios from "axios";
import React, { useEffect, useState } from "react";

export default function SettingsGroupCard(props) {
  const [checked, setChecked] = useState(props.startState);

  useEffect(() => {
    setChecked(props.startState);
  }, [props.startState]);

  const handleChange = (e) => {
    const new_state = e.target.value;
    setChecked(new_state === props.id);
      axios
        .post(`/api/current_filter/setting`, {
          newState: new_state,
        })
        .then(() => {})
        .catch((error) => console.log(error));
  };

  return (
    <label className="checkbox-container" htmlFor={props.id}>
      <input
        type="radio"
        id={props.id}
        name="settings-filter-by-group"
        value={props.id}
        checked={checked}
        onChange={handleChange}
      />
      <span className="checkmark"></span> {props.id}
    </label>
  );
}
