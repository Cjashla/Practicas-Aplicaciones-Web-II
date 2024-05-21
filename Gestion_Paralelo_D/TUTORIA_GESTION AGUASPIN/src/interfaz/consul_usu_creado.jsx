import React, { useState, useEffect } from 'react';

function ConsultarRoles() {
  const [roles, setRoles] = useState([]);

  useEffect(() => {
    const fetchRoles = async () => {
      const response = await fetch('/api/roles');
      const data = await response.json();
      setRoles(data);
    };

    fetchRoles();
  }, []);

  return (
    <div>
      <h1>Roles Creados</h1>
      <ul>
        {roles.map((rol) => (
          <li key={rol.id}>{rol.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default ConsultarRoles;
