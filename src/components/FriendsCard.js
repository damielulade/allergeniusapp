import React, { useState } from "react";
import mark from "../static/images/user_images/mark_long_hair.png";
import konst from "../static/images/user_images/konst.png";
import blank_user_img from "../static/images/user.png";

export default function FriendsCard(props) {
    const [dropdownState, setDropdownState] = useState(false);
    const viewDetails = () => {
        setDropdownState(!dropdownState);
    };

    const allergens = props.info.allergens?.map((allergen) => {
        return <li>{allergen}</li>;
    });

    const imageMap = {
        "mark_long_hair": mark,
        "konst": konst,
    };

    function parseImage(userImage) {
        // console.log(userImage);
        if (userImage === null || userImage === "" || userImage === "default") {
            return blank_user_img;
        } else {
            return imageMap[userImage];
        }
    }

    return (
        <div className="friend-card">
            <div className="friend-profile-picture">
                <img src={parseImage(props.info.userImage)} id="friends-page-img" alt="temp" />
            </div>
            <div className="friend-details">
                <div className="friend-description-box">
                    <p className="friend-name">
                        {props.info.firstName} {props.info.lastName}
                    </p>
                    <p className="friends-desc">{props.info.email}</p>
                </div>
                <div className="friend-allergen-box">
                    {!props.info.privacy && props.displayAllergens && (
                    <div className="friend-delete-button">
                        <p className="view-hide" onClick={viewDetails}>{dropdownState ? "Hide" : "View"} Allergens</p>
                    </div>
                    )}
                    {dropdownState && (
                        <div>
                            {props.info.allergens && (
                                <div className = "friends-allergen-block">
                                    <p className="friends-allergen-list-title">Allergens:</p>
                                    <div className="friends-allergen-list">{allergens}</div>
                                </div>
                            )}
                            {!props.info.allergens && (
                                <div className = "friends-allergen-block">
                                    <p className="friends-allergen-list-title">Allergens: N/A</p>
                                    <div className="friends-allergen-list"></div>
                                </div>
                            )}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );

}
