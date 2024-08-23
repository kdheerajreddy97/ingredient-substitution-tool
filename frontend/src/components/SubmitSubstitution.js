import React, { useState } from 'react';

const SubmitSubstitution = () => {
    const [ingredient, setIngredient] = useState('');
    const [substitute, setSubstitute] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:8000/api/submit-substitution/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ingredient, substitute }),
        });
        const data = await response.json();
        setMessage(data.message);
    };

    return (
        <div>
            <h2>Submit a New Substitution</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={ingredient}
                    onChange={(e) => setIngredient(e.target.value)}
                    placeholder="Enter the Ingredient"
                />
                <input
                    type="text"
                    value={substitute}
                    onChange={(e) => setSubstitute(e.target.value)}
                    placeholder="Enter the Substitute"
                />
                <button type="submit">Submit</button>
            </form>
            {message && <p className="message">{message}</p>}
        </div>
    );
};

export default SubmitSubstitution;
