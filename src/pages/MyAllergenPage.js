import React from "react";
import MainHeaderForAccount from "../components/main/MainHeaderForAccount";
import AllergenCard from "../components/AllergenCard";
import { useState } from "react";
import { useEffect } from "react";
import axios from "axios";

export default function MyAllergenPage() {
  const allergens = [
    "Gluten",
    "Dairy",
    "Nuts",
    "Peanuts",
    "Lupin",
    "Sesame Seeds",
    "Soya",
    "Mustard",
    "Fish",
    "Crustaceans",
    "Molluscs",
    "Sulphites",
    "Celery",
  ];

  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      axios
        .get("/api/allergens")
        .then((response) => setData(response.data))
        .catch((error) => console.log(error));
    };
    fetchData();
  }, []);

  const allergenCards = allergens.map((allergen, index) => {
    return (
      <AllergenCard
        key={index}
        id={`allergen${index + 1}`}
        allergen={allergen}
        startState={data.includes(allergen)}
      />
    );
  });

  return (
    <div className="section">
      <div className="main">
        <MainHeaderForAccount />
        <div className="container-other">
          <h2 id="allergens-list-title">My Allergens</h2>
          <form id="allergenchecks">{allergenCards}</form>
        </div>
      </div>
    </div>
  );
}
