import React, { useEffect, useRef, useMemo } from 'react';
import { Loader } from "@googlemaps/js-api-loader"

export default function MapComponent() {
    const mapContainerRef = useRef(null);
    const mapInstanceRef = useRef(null);

    const options = useMemo(() => ({
        mapTypeControl: false,
        fullscreenControl: false,
        streetViewControl: false,
        keyboardShortcuts: false,
    }), []);

    const center = useMemo(() => ({
        lat: 51.4941082, //51.5074,
        lng: -0.1743669 //-0.1278,
    }), []);

    useEffect(() => {
        const loader = new Loader({
            apiKey: "AIzaSyA5lTihboPl_N7Yt8T3worfrbjvF1MDLWc",
            version: "weekly",
            libraries: ["places"]  // Specify the libraries you need
        });

        loader.load().then(() => {
            if (!mapInstanceRef.current) {
                // Load the map for the first time
                mapInstanceRef.current = new window.google.maps.Map(mapContainerRef.current, {
                    center: center,
                    options: options,
                    zoom: 15,
                });
            }
        });

        // Clean up the map instance on component unmount
        return () => {
            if (mapInstanceRef.current) {
                mapInstanceRef.current = null;
            }
        };
    }, [center, options]);

    return (
        <div ref={mapContainerRef} className="map-container">
            {/* The map will be rendered inside this div */}
        </div>
    );
}

// AIzaSyA5lTihboPl_N7Yt8T3worfrbjvF1MDLWc
//<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyA5lTihboPl_N7Yt8T3worfrbjvF1MDLWc&libraries=places"></script>