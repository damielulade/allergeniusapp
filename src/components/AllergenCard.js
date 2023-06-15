import axios from "axios";
import React, { useEffect, useState } from "react";

export default function AllergenCard(props) {
  const [checked, setChecked] = useState(props.startState);

  useEffect(() => {
    setChecked(props.startState);
  }, [props.startState]);

  const handleChange = () => {
    setChecked(!checked);
    axios
      .post(`/api/allergens`, {
        allergen: props.allergen,
        newState: !checked,
      })
      .then(() => {})
      .catch((error) => console.log(error));
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
