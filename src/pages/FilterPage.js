import React from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import FilterCuisineCard from "../components/FilterCuisineCard";
import { useState } from "react";
import { useEffect } from "react";
import axios from "axios";

export default function MyAllergenPage() {
  const cuisines = [
      "American",
      "Italian",
      "Greek",
      "Breakfast",
      "Fast Food",
      "Chinese",
      "Burgers",
      "Sushi",
      "Caribbean",
      "Vietnamese",
      "Korean",
      "Brazilian",
      "Pasta",
      "Lebanese",
      "Spanish"
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
