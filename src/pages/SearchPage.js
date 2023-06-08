import React, { useEffect, useState } from "react";
import searchresults1 from "../static/images/searchresults1.png";
import MainHeader from "../components/MainHeader";
import { async } from "q";
import axios from 'axios'

axios.defaults.baseURL = "http://localhost:5000"


export default function SearchPage() {

    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const {data: response} = await axios.get('/collectData');
                // console.log(response);
                const arr = Object.entries(response).map(x => Object.entries(x[1]));

                console.log(arr);
                setData(arr);
            } catch (error) {
                console.error(error.message)
            }
            setLoading(false);
        }

        fetchData();

        // fetch('/collectData').then(data => {
        //     // setData(data);
        //     console.log(data);
        // })
    }, [])

  return (
      <div className = "section">
          <div className = "main">
              <MainHeader />
              <div className="container-other">
                {data.map(entry => (
                    <div>
                        <h3>{entry[1]} {entry[2]}</h3>
                        <p>aaa</p>
                    </div>
                ))}

                {/* <p>{data}</p> */}


                  {/* {data.map((r, index) => (
                      <p key={index}>{r.val}</p>
                  ))}
                  <img src={searchresults1} id="searchresults" alt = "temp"/> */}
              </div>
          </div>
      </div>
  )
}