import React, {useEffect, useRef, useMemo, useState} from 'react';
import { Loader } from "@googlemaps/js-api-loader"
import axios from "axios";
import marker_00 from "../../static/images/marker00.png";   // #FF0000
import marker_10 from "../../static/images/marker10.png";   // #FF3300
import marker_20 from "../../static/images/marker20.png";   // #FF6600
import marker_30 from "../../static/images/marker30.png";   // #FF9900
import marker_40 from "../../static/images/marker40.png";   // #FFCC00
import marker_50 from "../../static/images/marker50.png";   // #FFFF00
import marker_60 from "../../static/images/marker60.png";   // #CCFF00
import marker_70 from "../../static/images/marker70.png";   // #99FF00
import marker_80 from "../../static/images/marker80.png";   // #66FF00
import marker_90 from "../../static/images/marker90.png";   // #33FF00
import marker_100 from "../../static/images/marker100.png"; // #0080FF

function getMarkerColour(allergens, allergens_list, menu){
    let fixedAllergens = allergens
        .filter(item => item !== null)
        .map(item => {
            let lowerCaseItem = item.toLowerCase();
            return lowerCaseItem === "dairy" ? "milk" : lowerCaseItem;
        });

    let total_unsafe_items = [];
    fixedAllergens.forEach(allergen => {
        const unsafe_items = allergens_list[allergen] || [];
        total_unsafe_items.push(...unsafe_items);
    })
    total_unsafe_items = [...new Set(total_unsafe_items)];

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
        lat: 51.4941082, //51.5074,
        lng: -0.1743669 //-0.1278,
    }), []);

    const [restaurantData, setRestaurantData] = useState([]);

    useEffect(() => {
        const fetchRestaurantData = () => {
            axios
                .get(`/api/getRestaurantData`)
                .then((response) => {
                    setRestaurantData(response.data);
                })
                .catch((error) => console.log(error));
        };
        fetchRestaurantData();
    }, []);

    const markersData = useMemo(() => {
        return restaurantData.map(item => (
            {
                position: {lat: item.location[0], lng: item.location[1]},
                title: item.name,
                menu: item.menu,
                allergens: item.allergens
            }
        ))
    }, [restaurantData]);

    const [userData, setUserData] = useState([]);

    useEffect(() => {
        const fetchUserData = () => {
            axios
                .get(`/api/allergens`)
                .then((response) => {
                    setUserData(response.data);
                })
                .catch((error) => console.log(error));
        };
        fetchUserData();
    }, []);

    const thisUserAllergens = useMemo(() => {
        return userData
    }, [userData]);

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
                    const marker_colour = getMarkerColour(thisUserAllergens, markerData.allergens, markerData.menu)
                    const marker = new window.google.maps.Marker({
                        position: markerData.position,
                        map: mapInstanceRef.current,
                        title: markerData.title,
                        icon: {url: marker_colour}
                    });
                    markersRef.current.push(marker);

                    // Add click listener to marker
                    marker.addListener('click', () => {
                        infowindowRef.current.setContent(`
                          <div>
                            <h3>${markerData.title}</h3>
                            <span><a href='/restaurant-info/${markerData.title}' class = "restaurant-page-link">View Restaurant</a></span>
                          </div>
                        `);

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
    }, [center, options, markersData, thisUserAllergens]);

    return (
        <div ref={mapContainerRef} className="map-container">
            {/* The map will be rendered inside this div */}
        </div>
    );
}