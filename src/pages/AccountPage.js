import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import blank_user_img from "../static/images/user.png";
import mark from "../static/images/user_images/mark_long_hair.png";
import konst from "../static/images/user_images/konst.png";
import avatar1 from "../static/images/user_images/avatar1.png";
import avatar2 from "../static/images/user_images/avatar2.png";
import avatar3 from "../static/images/user_images/avatar3.png";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import axios from "axios";
import RadioComponent from "../components/utility/PrivacyRadioButton";

export default function AccountPage() {
  const imageMap = {
    mark_long_hair: mark,
    konst: konst,
    avatar1: avatar1,
    avatar2: avatar2,
    avatar3: avatar3,
  };
  const [userName, setUserName] = useState([]);
  let [userImage, setUserImage] = useState("");
  const [selectedOption, setSelectedOption] = useState();

  function parseImage(userImage) {
    if (userImage === null || userImage === "" || userImage === "default") {
      return blank_user_img;
    } else {
      return imageMap[userImage];
    }
  }

  const getAllData = async () => {
    try {
      const nameResponse = await axios.get(`/api/get_name`);
      const imageResponse = await axios.get(`/api/get_user_image`);
      const privacyResponse = await axios.get("/api/privacy");
      setUserName(nameResponse.data);
      setUserImage(imageResponse.data);
      setSelectedOption(JSON.parse(privacyResponse.data));
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getAllData();
  }, []);

  const signOut = () => {
    axios
      .get("/api/logout")
      .then(() => {
        window.location.href = "/";
      })
      .catch((error) => console.log(error));
  };
  
  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-other">
          <div className="user-image-box">
            <img src={parseImage(userImage)} id="userimg" alt="temp" />
          </div>
          <p id="accountname">{userName}</p>
          <div id="allergenlist">
            <Link to="/allergens" id="allergen-button">
              <span>My Allergens List</span>
            </Link>
          </div>
          <div id="favoriteslist">
            <Link to="/" id="favourites-button">
              <span>My Favourite Restaurants</span>
            </Link>
          </div>
          <div>
            <h2 id="privacy-title">
              Do you want others to see your allergen info?
            </h2>
            {!(selectedOption === undefined) && (
              <RadioComponent startState={selectedOption} />
            )}
          </div>
          <div id="sign-out-button" onClick={signOut}>
            <span>Sign Out</span>
          </div>
        </div>
      </div>
    </div>
  );
}
