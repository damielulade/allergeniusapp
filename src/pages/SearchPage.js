import React, { useEffect, useState } from "react";
import MainHeader from "../components/MainHeader";
import axios from 'axios'

const backend = axios.create({
    baseURL:  `${window.location.protocol}//${window.location.hostname}:5000`
})


export default function SearchPage() {

    const [data, setData] = useState({})

    useEffect(() => {
        const fetchData = () => {
            backend.get('/getRestaurantData').then(
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
              <MainHeader />
              <div className="container-other">
                {Object.entries(data).map(entry => {
                    const [key, value] = entry
                    return (
                        <div key={key}>
                            <h3>{key}: {value}</h3>
                        </div>
                    )
                })}
              </div>
          </div>
      </div>
  )
}