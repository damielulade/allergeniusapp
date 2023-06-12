import React from "react";
import MainHeaderVariant from "../components/MainHeaderVariant";

export default function FilterPage() {
  return (
      <div className = "section">
        <div className = "main">
          <MainHeaderVariant />
          <div className="container-other">
            <form id="restaurant-filter-checks">
              <label className="checkbox-container" htmlFor="filter1">
                <input type="checkbox" id="filter1" className="restaurant-checkbox" name="filter1" value="American"/>
                  <span className="checkmark"></span> American
              </label>

              <label className="checkbox-container" htmlFor="filter2">
                <input type="checkbox" id="filter2" className="restaurant-checkbox" name="filter2" value="Italian"/>
                  <span className="checkmark"></span> Italian
              </label>

              <label className="checkbox-container" htmlFor="filter3">
                <input type="checkbox" id="filter3" className="restaurant-checkbox" name="filter3" value="Greek"/>
                  <span className="checkmark"></span> Greek
              </label>

              <label className="checkbox-container" htmlFor="filter4">
                <input type="checkbox" id="filter4" className="restaurant-checkbox" name="filter4" value="Breakfast"/>
                  <span className="checkmark"></span> Breakfast
              </label>

              <label className="checkbox-container" htmlFor="filter5">
                <input type="checkbox" id="filter5" className="restaurant-checkbox" name="filter5" value="Fast Food"/>
                  <span className="checkmark"></span> Fast Food
              </label>

              <label className="checkbox-container" htmlFor="filter6">
                <input type="checkbox" id="filter6" className="restaurant-checkbox" name="filter6" value="Chinese"/>
                  <span className="checkmark"></span> Chinese
              </label>

              <label className="checkbox-container" htmlFor="filter7">
                <input type="checkbox" id="filter7" className="restaurant-checkbox" name="filter7" value="Burgers"/>
                  <span className="checkmark"></span> Burgers
              </label>

              <label className="checkbox-container" htmlFor="filter8">
                <input type="checkbox" id="filter8" className="restaurant-checkbox" name="filter8" value="Sushi"/>
                  <span className="checkmark"></span> Sushi
              </label>

              <label className="checkbox-container" htmlFor="filter9">
                <input type="checkbox" id="filter9" className="restaurant-checkbox" name="filter9" value="Caribbean"/>
                  <span className="checkmark"></span> Caribbean
              </label>

              <label className="checkbox-container" htmlFor="filter10">
                <input type="checkbox" id="filter10" className="restaurant-checkbox" name="filter10" value="Vietnamese"/>
                  <span className="checkmark"></span> Vietnamese
              </label>

              <label className="checkbox-container" htmlFor="filter11">
                <input type="checkbox" id="filter11" className="restaurant-checkbox" name="filter11" value="Korean"/>
                  <span className="checkmark"></span> Korean
              </label>

              <label className="checkbox-container" htmlFor="filter12">
                <input type="checkbox" id="filter12" className="restaurant-checkbox" name="filter12" value="Brazilian"/>
                  <span className="checkmark"></span> Brazilian
              </label>

              <label className="checkbox-container" htmlFor="filter13">
                <input type="checkbox" id="filter13" className="restaurant-checkbox" name="filter13" value="Pasta"/>
                  <span className="checkmark"></span> Pasta
              </label>
            </form>
          </div>
        </div>
      </div>
  )
}


