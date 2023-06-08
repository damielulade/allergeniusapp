import React, { useEffect, useRef } from 'react';
import { GoogleMap, LoadScript } from '@react-google-maps/api';

export default function MapComponent() {
    const mapContainerRef = useRef(null);
    const mapInstanceRef = useRef(null);

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

    useEffect(() => {
        if (!mapInstanceRef.current) {
            // Load the map for the first time
            mapInstanceRef.current = new window.google.maps.Map(mapContainerRef.current, {
                center,
                options,
                zoom: 10,
            });
        }

        // Clean up the map instance on component unmount

        return () => {
            if (mapInstanceRef.current) {
                mapInstanceRef.current = null;
            }
        };
    }, []);

    return (
        <div ref={mapContainerRef} className="map-container">
            {/* The map will be rendered inside this div */}
        </div>
    );
}


// AIzaSyA5lTihboPl_N7Yt8T3worfrbjvF1MDLWc