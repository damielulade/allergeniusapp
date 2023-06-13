import React, { useEffect, useState } from "react";

export default function AllergenCard(props) {
  const [checked, setChecked] = useState(false);
  // this state needs to be changed to take the db value for the allergen

  const handleChange = () => {
    setChecked(!checked);
    // update the db to set this allergen
  };

  return (
    <label className="checkbox-container" htmlFor={props.id}>
      <input
        type="checkbox"
        id={props.id}
        name={props.id}
        value={props.allergen}
        checked={checked}
        onChange={handleChange}
      />
      <span className="checkmark"></span> {props.allergen}
    </label>
  );
}
