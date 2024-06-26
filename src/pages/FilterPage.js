import React from "react";
import MainHeaderVariant from "../components/MainHeaderVariant";

export default function FilterPage() {
  return (
      <div className = "section">
        <div class = "main">
          <MainHeaderVariant />
          <div class="container-other">
            <form id="allergenchecks">
              <input type="checkbox" id="allergen1" name="allergen1" value="Gluten" />
              <label for="allergen1"> American </label><br />

              <input type="checkbox" id="allergen2" name="allergen2" value="Dairy" />
              <label for="allergen2"> Italian </label><br />
            
              <input type="checkbox" id="allergen3" name="allergen3" value="Nuts" />
              <label for="allergen3"> Greek </label><br />
          
              <input type="checkbox" id="allergen4" name="allergen4" value="Peanuts" />
              <label for="allergen4"> Breakfast </label><br />
          
              <input type="checkbox" id="allergen5" name="allergen5" value="Lupin" />
              <label for="allergen5"> Fast Food </label><br />
          
              <input type="checkbox" id="allergen6" name="allergen6" value="Sesame Seeds" />
              <label for="allergen6"> Chinese </label><br />
          
              <input type="checkbox" id="allergen7" name="allergen7" value="Soya" />
              <label for="allergen7"> Burgers </label><br />
          
              <input type="checkbox" id="allergen8" name="allergen8" value="Mustard" />
              <label for="allergen8"> Sushi </label><br />
          
              <input type="checkbox" id="allergen9" name="allergen9" value="Fish" />
              <label for="allergen9"> Caribbean </label><br />
          
              <input type="checkbox" id="allergen10" name="allergen10" value="Crustaceans" />
              <label for="allergen10"> Vietnamese </label><br />
          
              <input type="checkbox" id="allergen11" name="allergen11" value="Molluscs" />
              <label for="allergen11"> Korean </label><br />
          
              <input type="checkbox" id="allergen12" name="allergen12" value="Sulphites" />
              <label for="allergen12"> Brazillian </label><br />
          
              <input type="checkbox" id="allergen13" name="allergen13" value="Celery" />
              <label for="allergen13"> Pasta </label><br />
            </form>
          </div>
        </div>
      </div>
  )
}


