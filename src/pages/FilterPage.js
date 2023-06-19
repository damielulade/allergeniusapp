import React from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import FilterCuisineCard from "../components/FilterCuisineCard";
import { useState } from "react";
import { useEffect } from "react";
import axios from "axios";

export default function MyAllergenPage() {
  const cuisines = [
      "American",
      "Brazilian",
      "Breakfast",
      "Burgers",
      "Caribbean",
      "Chinese",
      "Fast Food",
      "Greek",
      "Italian",
      "Korean",
      "Lebanese",
      "Pasta",
      "Spanish",
      "Sushi",
      "Thai",
      "Vietnamese"
  ];

  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      axios
        .get("/api/set_restaurant_filter")
        .then((response) => setData(response.data))
        .catch((error) => console.log(error));
    };
    fetchData();
  }, []);

  const cuisineCards = cuisines.map((cuisine, index) => {
    return (
      <FilterCuisineCard
        key={index}
        id={`cuisine${index + 1}`}
        cuisine={cuisine}
        startState={data.includes(cuisine)}
      />
    );
  });

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-other">
          <form id="cuisinechecks">{cuisineCards}</form>
        </div>
      </div>
    </div>
  );
}
