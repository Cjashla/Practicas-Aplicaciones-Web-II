import os


def limpiar_pantalla():
    # Clear screen command based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')
        



def mostrar_menu():
    print("|---------------------------------|")
    print("\nMenu de Opciones:")
    print("|---------------------------------|")
    print("1. Crear usuario en la base de datos")
    print("2. Lista de usuarios en la base de datos")
    print("3. Modificar un usuario")
    print("4. Eliminar un usuario")
    print("5. Crear un rol")
    print("6. Lista de Roles")
    print("7. Asignar un rol a un usuario")
    print("8. Respaldar base de datos")
    print("9. Restaurar base de datos")
    print("10. Generar PDF")
    print("11. Generar CRUD en procedimientos almacenados")
    print("12. Ver usuarios y roles")
    print("13. Salir")
    print("|---------------------------------|")
