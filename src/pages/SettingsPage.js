import React from "react";
import MainHeaderVariant from "../components/MainHeaderVariant";
import TwoOptionRadioButton from "../components/ViewRadioButton";

export default function SettingsPage() {
  const placeholderFunc = (event) => {};

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-other">
          <h2 id="settings-title">Settings</h2>
          <TwoOptionRadioButton
            option1={"Map View"}
            option2={"List View"}
            // onChangeFunc={placeholderFunc}
          />
        </div>
      </div>
    </div>
  );
}
