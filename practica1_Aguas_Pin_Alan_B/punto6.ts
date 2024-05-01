
//6. Buscar un servicio REST de acceso libre en el internet distinto al utilizado en clases,
//tipar la respuesta aplicando una interfaz y aplicar Fetch para consultar los datos y
//validar que su respuesta cumpla con la interfaz.

interface Usuario {
    id: number;
    name: string;
    username: string;
    email: string;
    address: {
      street: string;
      suite: string;
      city: string;
      zipcode: string;
      geo: {
        lat: string;
        lng: string;
      };
    };
    phone: string;
    website: string;
    company: {
      name: string;
      catchPhrase: string;
      bs: string;
    };
  }

  async function obtenerUsuarios(): Promise<Usuario[]> {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!response.ok) {
      throw new Error('Error al obtener usuarios');
    }
    const usuarios: Usuario[] = await response.json();
    return usuarios;
  }
  
  // Función para validar que la respuesta cumpla con la interfaz Usuario
  function validarRespuesta(respuesta: any): respuesta is Usuario[] {
    if (!Array.isArray(respuesta)) return false;
    return respuesta.every((usuario) => {
      return (
        typeof usuario.id === 'number' &&
        typeof usuario.name === 'string' &&
        typeof usuario.username === 'string' &&
        typeof usuario.email === 'string' &&
        typeof usuario.address === 'object' &&
        typeof usuario.phone === 'string' &&
        typeof usuario.website === 'string' &&
        typeof usuario.company === 'object'
      );
    });
  }
  
  // Llamada a la función para obtener los usuarios y validar la respuesta
  obtenerUsuarios()
    .then((usuarios) => {
      if (validarRespuesta(usuarios)) {
        console.log('Respuesta válida:');
        console.log(usuarios);
      } else {
        console.log('La respuesta no cumple con la interfaz Usuario.');
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  