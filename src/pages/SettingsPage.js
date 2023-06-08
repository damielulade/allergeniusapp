import React from "react";
import MainHeaderVariant from "../components/MainHeaderVariant";
import RadioComponent from '../components/ViewRadioButton';

export default function SettingsPage() {
    return (
      <div className="section">
          <div className="main">
              <MainHeaderVariant/>
              <div className="container-other">
                  <h2 id="settings-title">Settings</h2>
                  <RadioComponent />
              </div>
          </div>
      </div>
  )
}