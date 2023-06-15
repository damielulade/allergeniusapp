import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import blank_user_img from "../static/images/user.png";
import mark from "../static/images/user_images/mark_long_hair.png"
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import axios from "axios";

export default function AccountPage() {
    const imageMap = {
        "mark_long_hair": mark,
    };

    function parseImage(userImage) {
        console.log(userImage);
        if (userImage === null || userImage === "" || userImage === "default") {
            return blank_user_img;
        } else {
            return imageMap[userImage];
        }
    }

    const [userName, setUserName] = useState([]);
    useEffect(() => {
        const fetchUserName = () => {
            axios
                .get(`/api/get_name`)
                .then((response) => {
                    setUserName(response.data);
                })
                .catch((error) => console.log(error));
        };
        fetchUserName();
        }, []);

    let [userImage, setUserImage] = useState("");
    useEffect(() => {
        const fetchUserImage = () => {
            axios
                .get(`/api/get_user_image`)
                .then((response) => {
                    setUserImage(response.data);
                })
                .catch((error) => console.log(error));
        };
        fetchUserImage();
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
                    <div className = "user-image-box">
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
                    <div id="privacysettings">
                        <Link to="/privacy" id="privacy-settings-button">
                            <span>Privacy Settings</span>
                        </Link>
                    </div>
                    <div id="sign-out-button" onClick={signOut}>
                        <span>Sign Out</span>
                    </div>
                </div>
            </div>
        </div>
    );
}
