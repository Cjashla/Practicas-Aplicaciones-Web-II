
import React, { useState } from 'react';

function ModificarUsuario() {
  const [userId, setUserId] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch(`/api/users/${userId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });
    if (response.ok) {
      alert('Usuario modificado con éxito');
    } else {
      alert('Error al modificar el usuario');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        ID del usuario:
        <input type="text" value={userId} onChange={(e) => setUserId(e.target.value)} required />
      </label>
      <label>
        Nuevo Email:
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </label>
      <label>
        Nueva Contraseña:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      </label>
      <button type="submit">Modificar Usuario</button>
    </form>
  );
}

export default ModificarUsuario;
