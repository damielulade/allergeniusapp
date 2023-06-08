import React, {useEffect, useRef, useMemo} from 'react';

export default function MapComponent() {
    const mapContainerRef = useRef(null);
    const mapInstanceRef = useRef(null);

    const options = useMemo(() => ({
        mapTypeControl: false,
        fullscreenControl: false,
        streetViewControl: false,
        keyboardShortcuts: false,
        // zoomControlOptions: {
        //     position: window.google.maps.ControlPosition.BOTTOM_LEFT,
        // },
    }), []);

    const center = useMemo(() => ({
        lat: 51.5074,
        lng: -0.1278,
        // lat: 51.4018,
        // lng: -0.079,
    }), []);

    useEffect(() => {
        if (!mapInstanceRef.current) {
            // Load the map for the first time
            mapInstanceRef.current = new window.google.maps.Map(mapContainerRef.current, {
                center: center,
                options: options,
                zoom: 10,
            });
        }

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