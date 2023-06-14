import { useState } from 'react';

export default function RestaurantInfoPage({ name, city, menu, allergens, ratings }) {
  const [expandedMenu, setExpandedMenu] = useState(false);

  const my_allergens = ["milk"];
  const toggleMenu = () => {
    setExpandedMenu(!expandedMenu);
  };

  let total_unsafe_items = [];
  my_allergens.forEach(allergen => {
      const unsafe_items = allergens[allergen] || [];
      total_unsafe_items.push(...unsafe_items);
  })
  total_unsafe_items = [...new Set(total_unsafe_items)];
  let total_safe_items = menu.filter(item => !total_unsafe_items.includes(item));

  return (
    <div className="restaurant-info">
      <h2>{name}</h2>
      <p>
        <strong>City:</strong> {city}
      </p>
      <p>
        <strong>Safe menu items: </strong>
        <button onClick={toggleMenu}>{expandedMenu ? 'Hide Menu' : 'Show Menu'}</button>
        {expandedMenu && (
          <ul>
            {total_safe_items.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        )}
      </p>
      <p>
        <strong>Ratings:</strong> {ratings.join(', ')}
      </p>
    </div>
  );
}