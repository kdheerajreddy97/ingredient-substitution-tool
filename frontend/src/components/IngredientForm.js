import React, { useState } from 'react';

const IngredientForm = ({ onSearch }) => {
    const [ingredient, setIngredient] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch(ingredient);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={ingredient}
                onChange={(e) => setIngredient(e.target.value)}
                placeholder="Enter the Ingredient"
            />
            <button type="submit">Find Substitute</button>
        </form>
    );
};

export default IngredientForm;
