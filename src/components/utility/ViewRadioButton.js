import axios from "axios";
import React, { useState } from "react";
import { useEffect } from "react";

export default function TwoOptionRadioButton(props) {
  const [selectedOption, setSelectedOption] = useState(props.startState);

  useEffect(() => {
    setSelectedOption(props.startState);
  }, [props.startState]);

  const handleOptionChange = (event) => {
    const value = event.target.value;
    setSelectedOption(value);
    axios
      .post("/api/view", {
        newState: value,
      })
      .then(() => {})
      .catch((error) => console.log(error));
  };

  return (
    <div className="view-setting">
      <label>
        <input
          type="radio"
          id="map-view"
          name="map-list-view"
          value={"map"}
          defaultChecked={selectedOption === "map"}
          onChange={handleOptionChange}
        />
        <span>Map View</span>
      </label>

      <label>
        <input
          type="radio"
          id="list-view"
          name="map-list-view"
          value={"list"}
          defaultChecked={selectedOption === "list"}
          onChange={handleOptionChange}
        />
        <span>List View</span>
      </label>

      {/*<p>Selected Option: {selectedOption}</p>*/}
    </div>
  );
}
