import marker_00 from "../../static/images/marker00.png";
import marker_10 from "../../static/images/marker10.png";
import marker_20 from "../../static/images/marker20.png";
import marker_30 from "../../static/images/marker30.png";
import marker_40 from "../../static/images/marker40.png";
import marker_50 from "../../static/images/marker50.png";
import marker_60 from "../../static/images/marker60.png";
import marker_70 from "../../static/images/marker70.png";
import marker_80 from "../../static/images/marker80.png";
import marker_90 from "../../static/images/marker90.png";
import marker_100 from "../../static/images/marker100.png";
import React from "react";

export default function MapColorKey() {
  return (
      <div className = "outer-map-key-box">
          <p id = "map-key-title">Percentage of safe dishes per restaurant</p>
          <div className="map-color-key-box">
              <div className = "marker-key-box">
                  <span className = "key-percentage">0</span>
                  <img src={marker_00} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">10</span>
                  <img src={marker_10} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">20</span>
                  <img src={marker_20} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">30</span>
                  <img src={marker_30} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">40</span>
                  <img src={marker_40} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">50</span>
                  <img src={marker_50} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">60</span>
                  <img src={marker_60} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">70</span>
                  <img src={marker_70} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">80</span>
                  <img src={marker_80} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">90</span>
                  <img src={marker_90} className="marker-key-image" alt = "temp"/>
              </div>
              <div className = "marker-key-box">
                  <span className = "key-percentage">100</span>
                  <img src={marker_100} className="marker-key-image" alt = "temp"/>
              </div>
          </div>
      </div>
  )
}