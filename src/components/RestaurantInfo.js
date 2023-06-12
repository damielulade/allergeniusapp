function RestaurantInfo({ name, city, menu, allergens, ratings }) {
  return (
    <div className="restaurant-info">
      <h2>{name}</h2>
      <p>
        <strong>City:</strong> {city}
      </p>
      <p>
        <strong>Menu:</strong> {menu.join(', ')}
      </p>
      <div className="allergens">
        <p>
          <strong>Allergens:</strong>
        </p>
        <ul>
          {Object.entries(allergens).map(([allergen, items]) => (
            <li key={allergen}>
              <strong>{allergen}:</strong> {items.join(', ')}
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

export default RestaurantInfo