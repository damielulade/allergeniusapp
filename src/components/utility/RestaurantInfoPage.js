import {useEffect, useState} from 'react';
import axios from "axios";

export default function RestaurantInfoPage({ name, city, menu, allergens, ratings }) {
  const [expandedMenu, setExpandedMenu] = useState(false);

  const [userAllergens, setUserData] = useState([]);
  useEffect(() => {
    const fetchUserData = () => {
        axios
            .get(`/api/getUserFriends`)
            .then((response) => {
                setUserData(response.data);
            })
            .catch((error) => console.log(error));
    };
    fetchUserData();
  }, []);

  const toggleMenu = () => {
    setExpandedMenu(!expandedMenu);
  };

  let fixedAllergens = userAllergens
    .filter(item => item !== null)
      .map(item => {
        let lowerCaseItem = item.toLowerCase();
        return lowerCaseItem === "dairy" ? "milk" : lowerCaseItem;
      });

  let total_unsafe_items = [];
  fixedAllergens.forEach(allergen => {
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