import React, { useState } from 'react';

export default function RadioComponent() {
    const [selectedOption, setSelectedOption] = useState(0);
    const handleOptionChange = (event) => {
        const value = event.target.value;
        setSelectedOption(value);
    };

    return (
        <div className = "privacy-setting">
            <label>
                <input
                    type = "radio" id="public" name="public-private-privacy"
                    value = {0} defaultChecked = {selectedOption === 0}
                    onChange = {handleOptionChange}
                />
                <span>Yes</span>
            </label>

            <label>
                <input
                    type = "radio" id="private" name="public-private-privacy"
                    value = {1} defaultChecked = {selectedOption === 1}
                    onChange = {handleOptionChange}
                />
                <span>No</span>
            </label>

            {/*<p>Selected Option: {selectedOption}</p>*/}
        </div>
    );
}