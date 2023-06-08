import React from 'react';
import { GoogleMap, LoadScript } from '@react-google-maps/api';

export default function MapComponent() {
    const options = {
        mapTypeControl: false,
        fullscreenControl: false,
        streetViewControl: false,
        // zoomControlOptions: {
        //     position: window.google.maps.ControlPosition.BOTTOM_LEFT,
        // },
    };

    const center = {
        lat: 51.5074,
        lng: -0.1278,
    };

      return (
          <LoadScript googleMapsApiKey="AIzaSyA5lTihboPl_N7Yt8T3worfrbjvF1MDLWc">
              <GoogleMap
                  mapContainerClassName="map-container"
                  center = {center}
                  options = {options}
                  zoom = {10}
              />
          </LoadScript>
      );
}


