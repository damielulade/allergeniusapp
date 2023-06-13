import React, {useEffect, useRef, useMemo, useState} from 'react';
import { Loader } from "@googlemaps/js-api-loader"
import axios from "axios";
import red_marker from "../static/images/marker_red.png";
import orange_marker from "../static/images/marker_orange.png";
import yellow_marker from "../static/images/marker_yellow.png";

function getPercentage(allergens, allergens_list, menu){

}

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

    // const baseURL = "http://localhost:5000"; // development
    const baseURL = "" // production

    useEffect(() => {
        const fetchData = () => {
            axios.get('${baseURL}/getRestaurantData')
                .then(response => {
                    setData(response.data);
                })
                .catch(error => console.log(error));
            };
            fetchData();
        }, []);

    const markersData = useMemo(() => {
        return data.map(item => (
            {
                position: {lat: item.location[0], lng: item.location[1]},
                title: item.name,
                menu: item.menu,
                allergens: item.allergens
            }
        ))
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
                        title: markerData.title,
                        icon: {url: red_marker}
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