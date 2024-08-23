import React, { useState } from "react";
import IngredientForm from "./components/IngredientForm";
import SubstituteResult from "./components/SubstituteResult";
import CommonSubstitutes from "./components/CommonSubstitutes";
import SubmitSubstitution from "./components/SubmitSubstitution";
import './App.css';  // Add this line to import the CSS

const App = () => {
    const [substitute, setSubstitute] = useState('');

    const handleSearch = async (ingredient) => {
        const response = await fetch(`http://localhost:8000/api/get-substitute/?ingredient=${ingredient}`);
        const data = await response.json();
        setSubstitute(data.substitute);
    };

    return (
        <div className="container">
            <h1>Ingredient Substitution Tool</h1>
            <IngredientForm onSearch={handleSearch} />
            {substitute && <SubstituteResult substitute={substitute} />}
            <CommonSubstitutes />
            <SubmitSubstitution />
        </div>
    );
};

export default App;
