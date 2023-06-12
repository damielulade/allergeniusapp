import React from "react";
import MainHeaderForAccount from "../components/MainHeaderForAccount";
import RadioComponent from '../components/PrivacyRadioButton';

export default function PrivacyPage() {
    return (
      <div className="section">
          <div className="main">
              <MainHeaderForAccount/>
              <div className="container-other">
                  <h2 id="privacy-title">Do you want others to see your allergen info?</h2>
                  <RadioComponent />
              </div>
          </div>
      </div>
  )
}