import React, { useEffect, useState } from "react";
import { useParams } from 'react-router-dom';
import MainHeaderVariant from "../main/MainHeaderVariant";
import RestaurantInfoPage from "../utility/RestaurantInfoPage";
import axios from 'axios'


export default function RestaurantPage() {
    const { id } = useParams();
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = () => {
            axios
                .get(`/api/getRestaurantData`)
                .then((response) => {
                    setData(response.data);
                })
                .catch((error) => console.log(error));
        };
        fetchData();
    }, []);

    return (
        <div className = "section">
            <div className = "main">
                <MainHeaderVariant />
                <div className="container-other">
                    {data
                        .filter(restaurant => restaurant.name.includes(id))
                        .map((restaurant, index) => (
                            <RestaurantInfoPage key={index} {...restaurant} />
                        ))
                    }
                </div>
            </div>
        </div>
    )
}