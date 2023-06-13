import React, { useState } from 'react';

export default function TwoOptionRadioButton(props) {
    const [selectedOption, setSelectedOption] = useState(0);
    const defaultOptionChange = (event) => {
        const value = event.target.value;
        setSelectedOption(value);
    };

    return (
        <div className = "view-setting">
            <label>
                <input
                    type = "radio" id="map-view" name="map-list-view"
                    value = {0} defaultChecked = {selectedOption === 0}
                    onChange = {defaultOptionChange}
                />
                <span>{props.option1}</span>
            </label>

            <label>
                <input
                    type = "radio" id="list-view" name="map-list-view"
                    value = {1} defaultChecked = {selectedOption === 1}
                    onChange = {defaultOptionChange}
                />
                <span>{props.option2}</span>
            </label>

            {/*<p>Selected Option: {selectedOption}</p>*/}
        </div>
    );
}