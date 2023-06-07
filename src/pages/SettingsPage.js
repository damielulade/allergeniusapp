import React, { useState } from "react";
import SidebarRight from "../components/EmptySidebar";
import SidebarLeft from "../components/SidebarLeft";
import MainHeader from "../components/MainHeader";
import RadioButtonGroup from "../components/ViewRadioButton";

export default function SettingsPage() {
    return (
      <div className="section">
          <SidebarLeft/>
          <div className="main">
              <MainHeader/>
              <div className="container">
                  <h2 id="settings-title">Settings</h2>
                  {/*<RadioButtonGroup selectedOption={selectedOption} handleChange={handleChange}/>*/}
              </div>
          </div>
          <SidebarRight />
      </div>
  )
}