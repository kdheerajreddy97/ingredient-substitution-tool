import React, { useState } from 'react';

const CommonSubstitutes = () => {
    const [substitutes, setSubstitutes] = useState([]);

    const fetchSubstitutes = async () => {
        const response = await fetch('http://localhost:8000/api/common-substitutes/');
        const data = await response.json();
        setSubstitutes(data.substitutes);
    };

    return (
        <div>
            <button onClick={fetchSubstitutes}>Get Common Substitutes</button>
            <ul>
                {substitutes.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
};

export default CommonSubstitutes;
