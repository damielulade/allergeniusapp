import React from "react";
import searchresults1 from "../static/images/searchresults1.png";
import MainHeader from "../components/MainHeader";

export default function SearchPage() {
    const data = [
        { val: 'Value 1' },
        { val: 'Value 2' },
        { val: 'Value 3' },
    ];
  return (
      <div className = "section">
          <div class = "main">
              <MainHeader />
              <div className="container-other">
                  {data.map((r, index) => (
                      <p key={index}>{r.val}</p>
                  ))}
                  {/*<img src={searchresults1} id="searchresults" alt = "temp"/>*/}
              </div>
          </div>
      </div>
  )
}