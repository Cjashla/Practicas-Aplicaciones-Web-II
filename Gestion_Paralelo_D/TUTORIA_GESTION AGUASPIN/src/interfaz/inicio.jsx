import React from 'react';

export const Header = (props) => {
    return (
    <div>
        <header>
            <div>
                <h1>Automatización de Tareas</h1>
            </div>
            <div>
                <h2>Por favor, escoge una opcion:</h2>
            </div>
            <ul>
                <center>
                <button onClick={() => props.onFormSwitch('creacion')}>Crear un Usuario</button><br></br>
                <button onClick={() => props.onFormSwitch('modificacion')}>Modificar un Usuario</button><br></br>
                <button onClick={() => props.onFormSwitch('eliminacion')}>Elimina un Usuario</button><br></br>
                <button onClick={() => props.onFormSwitch('rol')}>Crear un rol</button><br></br>
                <button onClick={() => props.onFormSwitch('asignacion')}>Asignar un rol</button><br></br>
                <button onClick={() => props.onFormSwitch('consulta')}>Consulta los Usuario Creados</button><br></br>
                <button onClick={() => props.onFormSwitch('roles')}>Consulta los Roles Creados</button><br></br>
                </center>
            </ul>
        </header>
    </div>    
      
    );
  };