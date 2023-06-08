import React, { useEffect, useState } from "react";
import searchresults1 from "../static/images/searchresults1.png";
import MainHeader from "../components/MainHeader";


export default function SearchPage() {

    const [data, setData] = useState([])

    useEffect(() => {
        fetch('/data').then(data => {
            setData(data);
        })
    }, [])

  return (
      <div className = "section">
          <div className = "main">
              <MainHeader />
              <div className="container-other">
                {data.map(r => (
                    <p>{r}</p> 
                ))}




                  {/* {data.map((r, index) => (
                      <p key={index}>{r.val}</p>
                  ))}
                  <img src={searchresults1} id="searchresults" alt = "temp"/> */}
              </div>
          </div>
      </div>
  )
}