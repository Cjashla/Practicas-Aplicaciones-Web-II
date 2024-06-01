from datetime import datetime
import os
import MySQLdb
import mysql.connector
from mysql.connector import connect, Error
import subprocess
import os
from datetime import datetime
from pymysql import MySQLError
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas


 #RESPALDO DE BASE DE DATOS
def realizar_respaldo(host, database, user, password, output_dir):
    try:
        # Asegurarse de que el directorio de salida existe, si no, crearlo
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Directorio {output_dir} creado.")

        # Generar nombre de archivo basado en la fecha y hora actual
        fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"{database}_{fecha_hora}.sql"
        output_path = os.path.join(output_dir, nombre_archivo)

        # Conectar a la base de datos
        with MySQLdb.connector.connect(
            host=host,
            port=3308,
            user=user,
            password=password,
            database=database
        ) as connection:
            cursor = connection.cursor()

            # Escribir estructura y datos de las tablas en el archivo SQL
            with open(output_path, 'w') as file:
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                for table in tables:
                    table_name = table[0]
                    cursor.execute(f"SHOW CREATE TABLE {table_name}")
                    create_table_statement = cursor.fetchone()[1]
                    file.write(f"{create_table_statement};\n\n")
                    cursor.execute(f"SELECT * FROM {table_name}")
                    for row in cursor:
                        values = ", ".join([f"'{str(value)}'" if value is not None else "NULL" for value in row])
                        file.write(f"INSERT INTO {table_name} VALUES {row};\n")
                    file.write("\n")

            print(f"Respaldo realizado exitosamente en {output_path}")

    except mysql.connector.Error as e:
        print(f"Error al realizar el respaldo: {e}")
        
        
#restaurar db

#RESPALDO DE BASE DE DATOS
def listar_archivos_de_respaldo(directorio_respaldo):
    archivos = [f for f in os.listdir(directorio_respaldo) if f.endswith('.sql')]
    if archivos:
        print("Archivos de respaldo disponibles:")
        for idx, archivo in enumerate(archivos, start=1):
            print(f"{idx}. {archivo}")
    else:
        print("No hay archivos de respaldo disponibles.")
    return archivos

def eliminar_todas_las_tablas(cursor):
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        print("Todas las tablas han sido eliminadas.")
    except mysql.connector.Error as e:
        print(f"Error al eliminar las tablas: {e}")

def realizar_restauracion(host, database, user, password, respaldo_path):
    try:
        with open(respaldo_path, 'r') as file:
            sql_script = file.read()

        # Conectar a la base de datos
        with MySQLError.connector.connect(
            host=host,
            port=3308,
            user=user,
            password=password,
            database=database
        ) as connection:
            cursor = connection.cursor()

            # Eliminar todas las tablas existentes
            eliminar_todas_las_tablas(cursor)

            # Deshabilitar las restricciones de clave foránea
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

            # Separar las sentencias SQL
            sql_commands = sql_script.split(';')

            # Ejecutar cada consulta individual
            for command in sql_commands:
                if command.strip():  # Ignorar comandos vacíos
                    try:
                        cursor.execute(command)
                    except mysql.connector.Error as e:
                        print(f"Error al ejecutar el comando: {e}")
                        continue

            # Habilitar las restricciones de clave foránea
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        print(f"Base de datos restaurada exitosamente desde {respaldo_path} a la base de datos {database}")
    except mysql.connector.Error as e:
        print(f"Error al restaurar la base de datos: {e}")

def listar_bases_de_datos(host, user, password):
    try:
        # Conectar al servidor de la base de datos
        with mysql.connector.connect(
            host=host,
            port=3308,
            user=user,
            password=password,
        ) as connection:
            # Obtener el cursor
            cursor = connection.cursor()
            # Ejecutar la consulta para obtener todas las bases de datos
            cursor.execute("SHOW DATABASES")
            # Obtener y retornar la lista de bases de datos
            return [database[0] for database in cursor.fetchall()]
    except mysql.connector.Error as e:
        print(f"Error al listar bases de datos: {e}")
        return []

def crear_base_de_datos(host, user, password, database):
    try:
        # Conectar al servidor de la base de datos
        with mysql.connector.connect(
            host=host,
            port=3308,
            user=user,
            password=password,
        ) as connection:
            cursor = connection.cursor()
            # Crear la nueva base de datos
            cursor.execute(f"CREATE DATABASE {database}")
            print(f"Base de datos {database} creada exitosamente.")
    except mysql.connector.Error as e:
        print(f"Error al crear la base de datos: {e}")
