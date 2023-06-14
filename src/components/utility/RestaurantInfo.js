import { useState } from 'react';

export default function RestaurantInfo({ name, city, menu, allergens, ratings }) {
  const [expandedMenu, setExpandedMenu] = useState(false);
  const [expandedAllergens, setExpandedAllergens] = useState([]);

  const toggleMenu = () => {
    setExpandedMenu(!expandedMenu);
  };

  const toggleAllergen = (allergen) => {
    if (expandedAllergens.includes(allergen)) {
      setExpandedAllergens(expandedAllergens.filter((item) => item !== allergen));
    } else {
      setExpandedAllergens([...expandedAllergens, allergen]);
    }
  };

  return (
    <div className="restaurant-info">
      <h2>{name}</h2>
      <p>
        <strong>City:</strong> {city}
      </p>
      <p>
        <strong>Menu: </strong>
        <button onClick={toggleMenu}>{expandedMenu ? 'Hide Menu' : 'Show Menu'}</button>
        {expandedMenu && (
          <ul>
            {menu.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        )}
      </p>
      <div className="allergens">
        <p>
          <strong>Allergens:</strong>
        </p>
        <ul>
          {Object.entries(allergens).map(([allergen, items]) => (
            <li key={allergen}>
              <button onClick={() => toggleAllergen(allergen)}>
                <strong>{allergen}:</strong>
              </button>
              {expandedAllergens.includes(allergen) && (
                <ul>
                  {items.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ul>
      </div>
      <p>
        <strong>Ratings:</strong> {ratings.join(', ')}
      </p>
    </div>
  );
}