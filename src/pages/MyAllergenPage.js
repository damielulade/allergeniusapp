import React from "react";
import MainHeaderForAccount from "../components/MainHeaderForAccount";

export default function MyAllergenPage() {
  return (
      <div className = "section">
        <div className = "main">
          <MainHeaderForAccount />
          <div className="container-other">
            <h2 id="allergens-list-title">My Allergens</h2>
            <form id="allergenchecks">
              <label className="checkbox-container" htmlFor="allergen1">
                <input type="checkbox" id="allergen1" name="allergen1" value="Gluten"/>
                  <span className="checkmark"></span> Gluten
              </label>

              <label className="checkbox-container" htmlFor="allergen2">
                <input type="checkbox" id="allergen2" name="allergen2" value="Dairy"/>
                  <span className="checkmark"></span> Dairy
              </label>

              <label className="checkbox-container" htmlFor="allergen3">
                <input type="checkbox" id="allergen3" name="allergen3" value="Nuts"/>
                  <span className="checkmark"></span> Nuts
              </label>

              <label className="checkbox-container" htmlFor="allergen4">
                <input type="checkbox" id="allergen4" name="allergen4" value="Peanuts"/>
                  <span className="checkmark"></span> Peanuts
              </label>

              <label className="checkbox-container" htmlFor="allergen5">
                <input type="checkbox" id="allergen5" name="allergen5" value="Lupin"/>
                  <span className="checkmark"></span> Lupin
              </label>

              <label className="checkbox-container" htmlFor="allergen6">
                <input type="checkbox" id="allergen6" name="allergen6" value="Sesame Seeds"/>
                  <span className="checkmark"></span> Sesame Seeds
              </label>

              <label className="checkbox-container" htmlFor="allergen7">
                <input type="checkbox" id="allergen7" name="allergen7" value="Soya"/>
                  <span className="checkmark"></span> Soya
              </label>

              <label className="checkbox-container" htmlFor="allergen8">
                <input type="checkbox" id="allergen8" name="allergen8" value="Mustard"/>
                  <span className="checkmark"></span> Mustard
              </label>

              <label className="checkbox-container" htmlFor="allergen9">
                <input type="checkbox" id="allergen9" name="allergen9" value="Fish"/>
                  <span className="checkmark"></span> Fish
              </label>

              <label className="checkbox-container" htmlFor="allergen10">
                <input type="checkbox" id="allergen10" name="allergen10" value="Crustaceans"/>
                  <span className="checkmark"></span> Crustaceans
              </label>

              <label className="checkbox-container" htmlFor="allergen11">
                <input type="checkbox" id="allergen11" name="allergen11" value="Molluscs"/>
                  <span className="checkmark"></span> Molluscs
              </label>

              <label className="checkbox-container" htmlFor="allergen12">
                <input type="checkbox" id="allergen12" name="allergen12" value="Sulphites"/>
                  <span className="checkmark"></span> Sulphites
              </label>

              <label className="checkbox-container" htmlFor="allergen13">
                <input type="checkbox" id="allergen13" name="allergen13" value="Celery"/>
                  <span className="checkmark"></span> Celery
              </label>
            </form>
          </div>
        </div>
      </div>
  )
}


