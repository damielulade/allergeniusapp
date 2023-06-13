import React, {useEffect, useRef, useMemo, useState} from 'react';
import { Loader } from "@googlemaps/js-api-loader"
import axios from "axios";

export default function MapComponent() {
    const mapContainerRef = useRef(null);
    const mapInstanceRef = useRef(null);
    const markersRef = useRef([]);
    const infowindowRef = useRef(null);

    const options = useMemo(() => ({
        mapTypeControl: false,
        fullscreenControl: false,
        streetViewControl: false,
        keyboardShortcuts: false,
        styles: [
            {
                featureType: "poi",
                stylers: [{ visibility: "off" }]
            }
        ]
    }), []);

    const center = useMemo(() => ({
        lat: 51.4941082, //51.5074,
        lng: -0.1743669 //-0.1278,
    }), []);

    const [data, setData] = useState([]);
    useEffect(() => {
        const fetchData = () => {
            axios.get('/getRestaurantData')
                .then(response => {
                    setData(response.data);
                })
                .catch(error => console.log(error));
            };
            fetchData();
        }, []);

    // Define your marker positions
    // const markersData = useMemo(() => ([
    //     {position: {lat: 51.49436985814742, lng: -0.17354637119368557}, title: "Honest Burger"},
    //     {position: {lat: 51.49336985814742, lng: -0.17254637119368557}, title: "Marker 2"},
    //     {position: {lat: 51.49236985814742, lng: -0.17154637119368557}, title: "Marker 3"},
    // ]), []);

    const markersData = useMemo(() => {
        return data.map(item => (
            {
                position: {lat: item.location[0], lng: item.location[1]}, // Assuming `location` contains the latLng object
                title: item.name
            }
        ));
    }, [data]);

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

                infowindowRef.current = new window.google.maps.InfoWindow();

                // Create markers
                markersData.forEach(markerData => {
                    const marker = new window.google.maps.Marker({
                        position: markerData.position,
                        map: mapInstanceRef.current,
                        title: markerData.title
                    });
                    markersRef.current.push(marker);

                    // Add click listener to marker
                    marker.addListener('click', () => {
                        infowindowRef.current.setContent(markerData.title);
                        infowindowRef.current.open(mapInstanceRef.current, marker);
                    });
                });
            }
        });

        // Clean up the map instance on component unmount
        return () => {
            if (mapInstanceRef.current) {

                // markersRef.current.forEach(marker => {
                //     marker.setMap(null);
                // });

                mapInstanceRef.current = null;
            }
        };
    }, [center, options, markersData]);

    return (
        <div ref={mapContainerRef} className="map-container">
            {/* The map will be rendered inside this div */}
        </div>
    );
}