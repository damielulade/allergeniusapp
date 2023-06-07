import React, { useState } from 'react';

export default function RadioComponent() {
    const [selectedOption, setSelectedOption] = useState(0);
    const handleOptionChange = (event) => {
        const value = event.target.value;
        setSelectedOption(value);
    };

    return (
        <div className = "view-setting">
            <label>
                <input
                    type = "radio" id="map-view" name="map-list-view"
                    value = {0} defaultChecked = {selectedOption === 0}
                    onChange = {handleOptionChange}
                />
                <span>Map View</span>
            </label>

            <label>
                <input
                    type = "radio" id="list-view" name="map-list-view"
                    value = {1} defaultChecked = {selectedOption === 1}
                    onChange = {handleOptionChange}
                />
                <span>List View</span>
            </label>

            {/*<p>Selected Option: {selectedOption}</p>*/}
        </div>
    );
}