import os
from utils import limpiar_pantalla, mostrar_menu
from conexion import conectar, desconectar
from informes import  obtener_datos_tabla, obtener_detalles_tablas, generar_pdf_con_datos
from usuarios_y_roles import cambiar_contraseña_usuario, crear_usuario_mariadb, eliminar_usuario_mariadb, cambiar_nombre_usuario, cambiar_contraseña_usuario, asignar_rol_a_usuario, crear_rol_mariadb, eliminar_usuario_mariadb, mostrar_roles, mostrar_usuarios
from procedimientos_crud import generar_procedimientos_crud, obtener_columnas
from restaurarDb import crear_base_de_datos, listar_archivos_de_respaldo, listar_bases_de_datos, realizar_respaldo, realizar_restauracion


def opcion1(cursor):
    limpiar_pantalla()
    print("Ejecutando Opción 1...")
    nombre_usuario = input("Ingrese el nombre del nuevo usuario de la base de datos: ")
    contraseña = input("Ingrese la contraseña para el nuevo usuario: ")
    crear_usuario_mariadb(cursor, nombre_usuario, contraseña)
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()


def opcion2(cursor):
    limpiar_pantalla()
    print("Ejecutando Opción 2...")
    mostrar_usuarios(cursor)
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()



def opcion3(cursor):
    limpiar_pantalla()
    print("Ejecutando Opción 3...")
    usuarios = mostrar_usuarios(cursor)
    if usuarios:
        try:
            eleccion = int(input("Seleccione el número del usuario a modificar: "))
            nombre_actual = usuarios[eleccion - 1][0] 
            nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
            nueva_contraseña = input("Ingrese la nueva contraseña del usuario: ")

            cambiar_nombre_usuario(cursor, nombre_actual, nuevo_nombre)
            cambiar_contraseña_usuario(cursor, nuevo_nombre, nueva_contraseña)  
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except IndexError:
            print("Selección no válida. Por favor, elija un número de la lista.")
    else:
        print("No hay usuarios para modificar.")
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()
    

def opcion4(cursor):
    limpiar_pantalla()
    print("Ejecutando Opción 4...")
    usuarios = mostrar_usuarios(cursor)
    if usuarios:
        try:
            eleccion = int(input("Seleccione el número del usuario a eliminar: "))
            nombre_usuario = usuarios[eleccion - 1][0]  
            confirmacion = input(f"Está seguro de que desea eliminar al usuario '{nombre_usuario}'? (s/n): ")
            if confirmacion.lower() == 's':
                eliminar_usuario_mariadb(cursor, nombre_usuario)
            else:
                print("Eliminación cancelada.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except IndexError:
            print("Selección no válida. Por favor, elija un número de la lista.")
    else:
        print("No hay usuarios para eliminar.")
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()

def opcion5(cursor):
    limpiar_pantalla()
    print("Ejecutando Opción 5...")
    nombre_rol = input("Ingrese el nombre del nuevo rol: ")
    crear_rol_mariadb(cursor, nombre_rol)
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()


def opcion6(cursor):
    limpiar_pantalla()
    print("Ejecutando Opción 6...")
    mostrar_roles(cursor)
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()

def opcion7(cursor):
    print("Ejecutando Opción 7...")
    usuarios = mostrar_usuarios(cursor)
    if usuarios:
        try:
            seleccion_usuario = int(input("Seleccione el número del usuario al que asignar el rol: ")) - 1
            nombre_usuario = usuarios[seleccion_usuario][0]
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return
        except IndexError:
            print("Selección no válida. Por favor, elija un número de la lista.")
            return

    roles = mostrar_roles(cursor)
    if roles:
        try:
            seleccion_rol = int(input("Seleccione el número del rol a asignar: ")) - 1
            nombre_rol = roles[seleccion_rol][0]
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return
        except IndexError:
            print("Selección no válida. Por favor, elija un número de la lista.")
            return

    asignar_rol_a_usuario(cursor, nombre_usuario, nombre_rol)
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()

def opcion8(cursor):
    print("Ejecutando Opción 8...")
    host = "localhost"
    database = "tienda"
    user = "root"
    password = "123"
    output_dir = r"C:\Users\byron\OneDrive\Documentos\BD-mariadb\BD-main\BD-main\respaldos"
    realizar_respaldo(host, database, user, password, output_dir)
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()


def opcion9(cursor):
    while True:
        limpiar_pantalla()
        print("Ejecutando Opción 9...")
        directorio_respaldo = r"C:\Users\byron\OneDrive\Documentos\BD-mariadb\BD-main\BD-main\respaldos"
        archivos = listar_archivos_de_respaldo(directorio_respaldo)
        if archivos:
            try:
                seleccion = int(input("Seleccione el número del archivo de respaldo a restaurar: ")) - 1
                respaldo_path = os.path.join(directorio_respaldo, archivos[seleccion])

                bases_de_datos = listar_bases_de_datos("localhost", "root", "123")
                if bases_de_datos:
                    print("Bases de datos disponibles:")
                    for idx, db in enumerate(bases_de_datos, start=1):
                        print(f"{idx}. {db}")
                    print(f"{idx+1}. Crear nueva base de datos")
                    seleccion_db = int(input("Seleccione el número de la base de datos a restaurar o ingrese el número de la opción para crear una nueva: "))
                    if seleccion_db <= idx:
                        nueva_db = bases_de_datos[seleccion_db - 1]
                    else:
                        nueva_db = input("Ingrese el nombre para la nueva base de datos: ")
                        crear_base_de_datos("localhost", "root", "123", nueva_db)

                    realizar_restauracion("localhost", nueva_db, "root", "123", respaldo_path)
                else:
                    print("No hay bases de datos disponibles.")
            except IndexError:
                print("Selección no válida. Por favor, elija un número de la lista.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
            except Exception as e:
                print(f"Error: {e}")

        # Opción para realizar una nueva restauración o regresar al inicio
        decision = input("¿Desea realizar otra restauración? (s/n): ").strip().lower()
        if decision != 's':
            break
    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()



def opcion10(cursor):
    database = 'tienda'
    print("Ejecutando Opción 10...")
    tablas = obtener_detalles_tablas(cursor, database)
    if not tablas:
        print("No se encontraron tablas disponibles.")
        return

    while True:
        print("Tablas disponibles:")
        for idx, tabla in enumerate(tablas.keys(), 1):
            print(f"{idx}. {tabla}")

        idx_tabla = int(input("Seleccione el número de la tabla: ")) - 1
        if idx_tabla < 0 or idx_tabla >= len(tablas):
            print("Selección de tabla inválida.")
            continue
        tabla_seleccionada = list(tablas.keys())[idx_tabla]

        print("Columnas disponibles en", tabla_seleccionada, ":")
        for idx, col in enumerate(tablas[tabla_seleccionada], 1):
            print(f"{idx}. {col}")

        idxs_columnas = input("Seleccione los números de las columnas (dejar en blanco para seleccionar todas): ")
        if not idxs_columnas.strip():
            columnas_seleccionadas = tablas[tabla_seleccionada]
        else:
            columnas_seleccionadas = [tablas[tabla_seleccionada][int(i) - 1] for i in idxs_columnas.split(",")]

        datos = obtener_datos_tabla(cursor, tabla_seleccionada, columnas_seleccionadas)

        output_dir = r"C:\Users\byron\OneDrive\Documentos\BD-mariadb\BD-main\BD-main\informes"
        generar_pdf_con_datos(tabla_seleccionada, datos, columnas_seleccionadas, output_dir)

        if input("¿Desea agregar otra tabla? (s/n): ").lower() != 's':
            break
    limpiar_pantalla()


def opcion11(cursor):
    database = 'tienda'
    print("Ejecutando Opción 11...")

    tablas = obtener_detalles_tablas(cursor, database)
    print("Tablas disponibles:")
    for i, tabla in enumerate(tablas, 1):
        print(f"{i}. {tabla}")

    seleccion_tabla = int(input("Seleccione el número de la tabla: ")) - 1
    if seleccion_tabla < 0 or seleccion_tabla >= len(tablas):
        print("Selección de tabla inválida.")
    else:
        tabla_seleccionada_nombre = list(tablas.keys())[seleccion_tabla]
        columnas = obtener_columnas(cursor, tabla_seleccionada_nombre)
        id_column = next((col[0] for col in columnas if 'id' in col[0].lower()), None)
        generar_procedimientos_crud(cursor, tabla_seleccionada_nombre, columnas, id_column)

    input("Presione Enter para regresar al menú principal...")
    limpiar_pantalla()
