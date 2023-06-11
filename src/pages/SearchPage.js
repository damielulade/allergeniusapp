import React, { useEffect, useState } from "react";
import MainHeader from "../components/MainHeader";
import axios from 'axios'


export default function SearchPage() {

    const [data, setData] = useState({})

    useEffect(() => {
        const fetchData = () => {
            axios.get('http://localhost:5000/getRestaurantData').then(
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