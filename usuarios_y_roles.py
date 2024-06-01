def crear_usuario_mariadb(cursor, nombre_usuario, contraseña):
    try:
        query = "CREATE USER %s@'localhost' IDENTIFIED BY %s"
        cursor.execute(query, (nombre_usuario, contraseña))
        print("Usuario creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el usuario: {e}")


# Mostrar usuarios 
def mostrar_usuarios(cursor):
    try:
        query = """
        SELECT User FROM mysql.user
        WHERE Host = 'localhost' AND User NOT IN ('mysql.session', 'mysql.sys', 'debian-sys-maint')
        ORDER BY User;
        """
        cursor.execute(query)
        usuarios = cursor.fetchall()
        if usuarios:
            print("Usuarios de la base de datos:")
            for index, usuario in enumerate(usuarios, start=1):
                print(f"{index}. {usuario[0]}")
            return usuarios 
        else:
            print("No hay usuarios disponibles.")
            return []
    except Exception as e:
        print(f"Error al obtener la lista de usuarios: {e}")
        return []


# Modificar usuarios
def cambiar_nombre_usuario(cursor, nombre_actual, nuevo_nombre):
    try:
        query = "RENAME USER %s@'localhost' TO %s@'localhost'"
        cursor.execute(query, (nombre_actual, nuevo_nombre))
        print("Nombre de usuario cambiado exitosamente.")
    except Exception as e:
        print(f"Error al cambiar el nombre del usuario: {e}")

def cambiar_contraseña_usuario(cursor, nombre_usuario, nueva_contraseña):
    try:
        query = "ALTER USER %s@'localhost' IDENTIFIED BY %s"
        cursor.execute(query, (nombre_usuario, nueva_contraseña))
        print("Contraseña cambiada exitosamente.")
    except Exception as e:
        print(f"Error al cambiar la contraseña del usuario: {e}")


# Eliminar usuarios
def eliminar_usuario_mariadb(cursor, nombre_usuario):
    try:
        query = "DROP USER %s@'localhost'"
        cursor.execute(query, (nombre_usuario,))
        print("Usuario eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")

# Crear un rol 
def crear_rol_mariadb(cursor, nombre_rol):
    try:
        query = "CREATE ROLE %s"
        cursor.execute(query, (nombre_rol,))
        print(f"Rol '{nombre_rol}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el rol: {e}")


# Mostrar roles
def mostrar_roles(cursor):
    try:
        cursor.execute("SELECT User FROM mysql.user WHERE Is_role = 'Y'")
        roles = cursor.fetchall()
        if roles:
            print("Roles disponibles en la base de datos:")
            for index, rol in enumerate(roles, start=1):
                print(f"{index}. {rol[0]}")
            return roles
        else:
            print("No hay roles disponibles.")
            return []
    except Exception as e:
        print(f"Error al obtener la lista de roles: {e}")
        return []


# Asignar un rol a un usuario 
def asignar_rol_a_usuario(cursor, nombre_usuario, nombre_rol):
    try:
        query = "GRANT %s TO %s@'localhost'"
        cursor.execute(query, (nombre_rol, nombre_usuario))
        print(f"Rol '{nombre_rol}' asignado exitosamente a '{nombre_usuario}'.")
    except Exception as e:
        print(f"Error al asignar el rol: {e}")



def obtener_roles_de_usuario(cursor, nombre_usuario):
    try:
        query = "SHOW GRANTS FOR %s@'localhost'"
        cursor.execute(query, (nombre_usuario,))
        roles = cursor.fetchall()
        if roles:
            print(f"Roles asignados al usuario '{nombre_usuario}':")
            for role in roles:
                print(role[0])
        else:
            print(f"No se encontraron roles asignados al usuario '{nombre_usuario}'.")
    except Exception as e:
        print(f"Error al obtener los roles del usuario: {e}")

def ver_usuarios_y_roles(cursor):
    usuarios = mostrar_usuarios(cursor)
    if usuarios:
        try:
            seleccion_usuario = int(input("Seleccione el número del usuario del que desea ver los roles: ")) - 1
            nombre_usuario = usuarios[seleccion_usuario][0]
            obtener_roles_de_usuario(cursor, nombre_usuario)
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except IndexError:
            print("Selección no válida. Por favor, elija un número de la lista.")

