import React, { useState, useEffect } from 'react';

function ConsultarUsuarios() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    const fetchUsuarios = async () => {
      const response = await fetch('/api/users');
      const data = await response.json();
      setUsuarios(data);
    };

    fetchUsuarios();
  }, []);

  return (
    <div>
      <h1>Usuarios Creados</h1>
      <ul>
        {usuarios.map((usuario) => (
          <li key={usuario.id}>{usuario.username} - {usuario.email}</li>
        ))}
      </ul>
    </div>
  );
}

export default ConsultarUsuarios;
