import os
from conexion import conectar, desconectar
from usuarios_y_roles import ver_usuarios_y_roles
from utils import limpiar_pantalla, mostrar_menu
from opciones import opcion1, opcion2, opcion3, opcion4, opcion5, opcion6, opcion7, opcion8, opcion9, opcion10, opcion11

def main():
    # Conectar a la base de datos
    conexion = conectar()
    cursor = conexion.cursor()

    # Bucle principal del programa
    while True:
        limpiar_pantalla()
        mostrar_menu()

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            opcion1(cursor)
        elif opcion == 2:
            opcion2(cursor)
        elif opcion == 3:
            opcion3(cursor)
        elif opcion == 4:
            opcion4(cursor)
        elif opcion == 5:
            opcion5(cursor)
        elif opcion == 6:
            opcion6(cursor)
        elif opcion == 7:
            opcion7(cursor)
        elif opcion == 8:
            opcion8(cursor)
        elif opcion == 9:
            opcion9(cursor)
        elif opcion == 10:
            opcion10(cursor)
        elif opcion == 11:
            opcion11(cursor)
        elif opcion == 12:
            ver_usuarios_y_roles(cursor)
        elif opcion == 13:
            break
        else:
            print("Opción no válida.")

    # Desconectar de la base de datos
    desconectar(conexion)

if __name__ == "__main__":
    main()
