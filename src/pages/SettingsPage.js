import React from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import TwoOptionRadioButton from "../components/utility/ViewRadioButton";

export default function SettingsPage() {
  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-other">
          <h2 id="settings-title">Settings</h2>
          <TwoOptionRadioButton
            option1={"Map View"}
            option2={"List View"}
          />
        </div>
      </div>
    </div>
  );
}
