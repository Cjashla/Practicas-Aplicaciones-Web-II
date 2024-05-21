import React, { useState } from 'react';

function AsignarRol() {
  const [userId, setUserId] = useState('');
  const [roleId, setRoleId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch(`/api/users/${userId}/roles`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ roleId }),
    });
    if (response.ok) {
      alert('Rol asignado con éxito');
    } else {
      alert('Error al asignar el rol');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        ID del Usuario:
        <input type="text" value={userId} onChange={(e) => setUserId(e.target.value)} required />
      </label>
      <label>
        ID del Rol:
        <input type="text" value={roleId} onChange={(e) => setRoleId(e.target.value)} required />
      </label>
      <button type="submit">Asignar Rol</button>
    </form>
  );
}

export default AsignarRol;
