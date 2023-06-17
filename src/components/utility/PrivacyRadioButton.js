import axios from "axios";
import React, { useState } from "react";
import { useEffect } from "react";

export default function RadioComponent(props) {
  const [selectedOption, setSelectedOption] = useState(props.startState);

  useEffect(() => {
    setSelectedOption(props.startState);
  }, [props.startState]);

  const handleOptionChange = (event) => {
    const value = event.target.value;
    setSelectedOption(JSON.parse(value));
    console.log();
    axios
      .post("/api/privacy", {
        newState: JSON.parse(value),
      })
      .then(() => {})
      .catch((error) => console.log(error));
  };

  return (
    <div className="privacy-setting">
      <label>
        <input
          type="radio"
          id="public"
          name="public-private-privacy"
          value={false}
          defaultChecked={!selectedOption}
          onChange={handleOptionChange}
        />
        <span>Yes</span>
      </label>

      <label>
        <input
          type="radio"
          id="private"
          name="public-private-privacy"
          value={true}
          defaultChecked={selectedOption}
          onChange={handleOptionChange}
        />
        <span>No</span>
      </label>
    </div>
  );
}
