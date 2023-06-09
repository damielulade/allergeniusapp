import React, { useEffect, useState } from "react";
import MainHeader from "../components/MainHeader";
import axios from 'axios'

const backend = axios.create({
    baseURL:  `${window.location.protocol}//${window.location.hostname}:5000`
})


export default function SearchPage() {

    const [data, setData] = useState({})

    useEffect(() => {
        const fetchData = async () => {
            try {
                const {data: response} = await backend.get('/getRestaurantData');
                console.log((Object.entries(response)))
                setData(response);
            } catch (error) {
                console.error(error.message)
            }
        }

        fetchData();
    }, [])

  return (
      <div className = "section">
          <div className = "main">
              <MainHeader />
              <div className="container-other">
                {Object.entries(data).map(entry => {
                    const [key, value] = entry
                    return (
                        <div>
                            <h3>{key}: {value}</h3>
                        </div>
                    )
                })}
              </div>
          </div>
      </div>
  )
}