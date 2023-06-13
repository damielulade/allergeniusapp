import React, { useEffect, useState } from "react";
import MainHeader from "../components/main/MainHeader";
import RestaurantInfo from "../components/utility/RestaurantInfo";
import axios from 'axios'
import MainHeaderVariant from "../components/main/MainHeaderVariant";


export default function SearchPage() {

    const [data, setData] = useState([])

    useEffect(() => {
        const fetchData = () => {
            axios.get('/getRestaurantData').then(
                response => {
                    setData(response.data)
                }
            ).catch(error => console.log(error))
        }
        fetchData();
    }, [])

    return (
        <div className = "section">
            <div className = "main">
                <MainHeaderVariant />
                <div className="container-other">
                    {data.map((restaurant, index) => (
                        <RestaurantInfo key={index} {...restaurant} />
                    ))}
                </div>
            </div>
        </div>
    )
}