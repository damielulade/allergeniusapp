import React, { useEffect, useState } from "react";
import axios from "axios";
import userimg from "../static/images/user.png";

export default function AllergenCard(props) {
  return (
    <label className="checkbox-container" htmlFor={props.id}>
      <input type="checkbox" id={props.id} name={props.id} value={props.allergen} />
      <span className="checkmark"></span> {props.allergen}
    </label>
  );
}
