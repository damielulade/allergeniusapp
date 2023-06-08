import React from "react";
import searchresults1 from "../static/images/searchresults1.png";
import MainHeader from "../components/MainHeader";

export default function SearchPage() {
  return (
      <div className = "section">
          <div class = "main">
              <MainHeader />
              <div className="container-other">
                  <img src={searchresults1} id="searchresults" alt = "temp"/>
              </div>
          </div>
      </div>
  )
}