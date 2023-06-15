import axios from "axios";
import React, { useState } from "react";
import { useEffect } from "react";

export default function RadioComponent() {
  const [selectedOption, setSelectedOption] = useState();

  const fetchData = async () => {
    try {
      let response = await axios.get('/api/privacy');
      let data = await JSON.parse(response.data);
      console.log("collected data is " + data)
      setSelectedOption(data ? 'no' : 'yes');
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  const handleOptionChange = (event) => {
    const value = event.target.value;
    setSelectedOption(value);
    console.log("updated data is " + value);
    axios
      .post("/api/privacy", {
        newState: value === 'no',
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
          value={"yes"}
          defaultChecked={selectedOption === "yes"}
          onChange={handleOptionChange}
        />
        <span>Yes</span>
      </label>

      <label>
        <input
          type="radio"
          id="private"
          name="public-private-privacy"
          value={"no"}
          defaultChecked={selectedOption === "no"}
          onChange={handleOptionChange}
        />
        <span>No</span>
      </label>
    </div>
  );
}
