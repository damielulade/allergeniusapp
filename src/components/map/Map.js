import React, {useEffect, useRef, useMemo, useState} from 'react';
import { Loader } from "@googlemaps/js-api-loader"
import axios from "axios";
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

function getMarkerColour(allergens, allergens_list, menu){
    console.log("\n\n")
    let total_unsafe_items = [];
    allergens.forEach(allergen => {
        const unsafe_items = allergens_list[allergen] || [];
        console.log("unsafe_items: ", unsafe_items);
        total_unsafe_items.push(...unsafe_items);
    })
    total_unsafe_items = [...new Set(total_unsafe_items)];
    console.log("total_unsafe_items: ", total_unsafe_items);

    let total_safe_items = menu.filter(item => !total_unsafe_items.includes(item));

    const percentage = parseInt(((total_safe_items.length/menu.length) * 100).toFixed());
    if (percentage >= 0 && percentage < 10) {
        return marker_00;
    } else if (percentage >= 10 && percentage < 20) {
        return marker_10;
    } else if (percentage >= 20 && percentage < 30) {
        return marker_20;
    } else if (percentage >= 30 && percentage < 40) {
        return marker_30;
    } else if (percentage >= 40 && percentage < 50) {
        return marker_40;
    } else if (percentage >= 50 && percentage < 60) {
        return marker_50;
    } else if (percentage >= 60 && percentage < 70) {
        return marker_60;
    } else if (percentage >= 70 && percentage < 80) {
        return marker_70;
    } else if (percentage >= 80 && percentage < 90) {
        return marker_80;
    } else if (percentage >= 90 && percentage < 100) {
        return marker_90;
    } else if (percentage === 100) {
        return marker_100;
    }

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
        lat: 51.49416381279757, //51.5074,
        lng: -0.17404775287090068 //-0.1278,
    }), []);

    const [data, setData] = useState([]);

    // const baseURL = "http://localhost:5000"; // development
    const baseURL = "" // production

    useEffect(() => {
        const fetchData = () => {
            axios
                .get(`${baseURL}/getRestaurantData`)
                .then((response) => {
                    setData(response.data);
                })
                .catch((error) => console.log(error));
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
                    zoom: 17,
                });

                infowindowRef.current = new window.google.maps.InfoWindow();

                // Create markers
                markersData.forEach(markerData => {
                    const marker_colour = getMarkerColour(["fish"], markerData.allergens, markerData.menu)
                    const marker = new window.google.maps.Marker({
                        position: markerData.position,
                        map: mapInstanceRef.current,
                        title: markerData.title,
                        icon: {url: marker_colour}
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