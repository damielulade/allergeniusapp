import React from "react";
import MainHeaderForAccount from "../components/MainHeaderForAccount";
import AllergenCard from "../components/AllergenCard";

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

  const allergenCards = allergens.map((allergen, index) => {
    return (
      <AllergenCard
        key={index}
        id={`allergen${index + 1}`}
        allergen={allergen}
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
