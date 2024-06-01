
 #PROCEDIMIENTO ALMACENADO
import os


def obtener_datos_tabla(cursor, tabla, columnas):
    try:
        columnas_sql = ", ".join(columnas)
        query = f"SELECT {columnas_sql} FROM {tabla}"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener datos de la tabla {tabla}: {e}")
        return []

def obtener_columnas(cursor, tabla):
    cursor.execute(f"SHOW COLUMNS FROM {tabla}")
    return [row for row in cursor.fetchall()]

def generar_procedimiento_insert(tabla, columnas):
    columnas_insertar = [col for col in columnas if col[1] is None or not col[1].startswith('nextval')]
    cols = ", ".join([col[0] for col in columnas_insertar])
    param_definitions = ", ".join([f"IN p_{col[0]} {col[1]}" for col in columnas_insertar])
    valores = ", ".join([f"p_{col[0]}" for col in columnas_insertar])

    proc_insert = f"""
    DELIMITER $$
    CREATE PROCEDURE {tabla}_insert({param_definitions})
    BEGIN
        INSERT INTO {tabla} ({cols}) VALUES ({valores});
    END$$
    DELIMITER ;
    """
    return proc_insert

def generar_procedimiento_select(tabla):
    proc_select = f"""
    DELIMITER $$
    CREATE PROCEDURE {tabla}_select()
    BEGIN
        SELECT * FROM {tabla};
    END$$
    DELIMITER ;
    """
    return proc_select

def generar_procedimiento_update(tabla, columnas, id_column):
    columnas_update = [col for col in columnas if col[0] != id_column]
    param_definitions = ", ".join([f"IN p_{col[0]} {col[1]}" for col in columnas_update])
    set_values = ", ".join([f"{col[0]} = p_{col[0]}" for col in columnas_update])

    proc_update = f"""
    DELIMITER $$
    CREATE PROCEDURE {tabla}_update({param_definitions}, IN p_{id_column} INT)
    BEGIN
        UPDATE {tabla} SET {set_values} WHERE {id_column} = p_{id_column};
    END$$
    DELIMITER ;
    """
    return proc_update

def generar_procedimiento_delete(tabla, id_column):
    proc_delete = f"""
    DELIMITER $$
    CREATE PROCEDURE {tabla}_delete(IN p_{id_column} INT)
    BEGIN
        DELETE FROM {tabla} WHERE {id_column} = p_{id_column};
    END$$
    DELIMITER ;
    """
    return proc_delete

def generar_procedimientos_crud(cursor, tabla, columnas, id_column):
    try:
        procedimientos_dir = r"C:\Users\byron\OneDrive\Documentos\BD-mariadb\BD-main\BD-main\procedimientos"
        if not os.path.exists(procedimientos_dir):
            os.makedirs(procedimientos_dir)

        with open(os.path.join(procedimientos_dir, f"{tabla}_crud.sql"), "w") as f:
            f.write(generar_procedimiento_insert(tabla, columnas))
            f.write("\n")
            f.write(generar_procedimiento_select(tabla))
            f.write("\n")
            f.write(generar_procedimiento_update(tabla, columnas, id_column))
            f.write("\n")
            f.write(generar_procedimiento_delete(tabla, id_column))
        print(f"Procedimientos CRUD para la tabla {tabla} creados exitosamente en la carpeta 'procedimientos'.")
    except Exception as e:
        print(f"Error al generar procedimientos CRUD: {e}")
