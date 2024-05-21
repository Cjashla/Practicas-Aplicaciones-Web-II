import React from 'react';
export const create_usuario = (props) => {


  

  function CrearUsuario() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      const response = await fetch('/api/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
      });
      if (response.ok) {
        alert('Usuario creado con éxito');
      } else {
        alert('Error al crear el usuario');
      }
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <label>
          Nombre de usuario:
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
        </label>
        <label>
          Email:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        <label>
          Contraseña:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </label>
        <button type="submit">Crear Usuario</button>
      </form>
    );
  }
  


}