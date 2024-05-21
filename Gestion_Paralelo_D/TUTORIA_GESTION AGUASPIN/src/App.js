import React, { useState } from 'react';
import './App.css';
import {Header} from './interfaz/inicio';
import { create_usuario } from './interfaz/crea_usuario';


function App() {
    const [currentForm, setCurrentForm]= useState ('header');
    
    const toggleForm = (formName) => {
        setCurrentForm(formName);
    };

    const components={
        header:<Header onFormSwitch={toggleForm}/>,
        Create_usuario:<create_usuario onFormSwitch={toggleForm}/>,
    };

    const CurrentComponent = components[currentForm];

    return (
        <div className="App">
            {CurrentComponent}
        </div>
  );
}

export default App;