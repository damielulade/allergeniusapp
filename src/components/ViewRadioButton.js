import React from 'react';

export default function RadioButtonGroup(props) {
  return (
      <div className="view-setting" onChange={this.setGender.bind(this)}>
          <label>
              <input type="radio" name="map-list-view" value = {0} checked/>
              <span>Map View</span>
          </label>
          <label>
              <input type="radio" name="map-list-view" value = {1}/>
              <span>List View</span>
          </label>
      </div>
  );
}