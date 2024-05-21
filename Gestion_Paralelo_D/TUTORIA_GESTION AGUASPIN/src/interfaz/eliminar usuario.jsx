import React from 'react';
export const eliminar_usuario = (props) => 

    function CrearRol() {
        const [roleName, setRoleName] = useState('');
      
        const handleSubmit = async (e) => {
          e.preventDefault();
          const response = await fetch('/api/roles', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: roleName }),
          });
          if (response.ok) {
            alert('Rol creado con éxito');
          } else {
            alert('Error al crear el rol');
          }
        };
      
        return (
          <form onSubmit={handleSubmit}>
            <label>
              Nombre del Rol:
              <input type="text" value={roleName} onChange={(e) => setRoleName(e.target.value)} required />
            </label>
            <button type="submit">Crear Rol</button>
          </form>
        );

}