import sys
import mysql.connector

def conectar():
    """
    Establece una conexión a la base de datos MySQL.

    Retorna:
        Objeto de conexión a la base de datos MySQL.
    """
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="root",
            password="Akuita@09052003",
            database="tutoriagestion",
            auth_plugin='caching_sha2_password' 
        )
        print("Conectado a la base de datos MySQL.")
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        sys.exit(1)

def desconectar(conexion):
    """
    Cierra la conexión a la base de datos MySQL.

    Args:
        conexion (objeto de conexión): Objeto de conexión a la base de datos MySQL.
    """
    try:
        conexion.close()
        print("Conexión a la base de datos cerrada.")
    except Exception as e:
        print(f"Error al cerrar la conexión: {e}")
