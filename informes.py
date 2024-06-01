
 #GENERAR PDF
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def obtener_datos_tabla(cursor, tabla, columnas):
    try:
        columnas_sql = ", ".join(columnas)
        query = f"SELECT {columnas_sql} FROM {tabla}"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener datos de la tabla {tabla}: {e}")
        return []

def generar_pdf_con_datos(tabla, datos, columnas, output_dir):
    try:
        # Generar un nombre de archivo único basado en la fecha y hora actuales
        fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(output_dir, f"{tabla}_informe_{fecha_hora}.pdf")

        doc = SimpleDocTemplate(output_path, pagesize=letter)
        story = []

        # Encabezados de la tabla
        data = [columnas]

        # Agregar los datos de la tabla
        for fila in datos:
            data.append([str(dato) for dato in fila])

        # Crear la tabla con los datos
        t = Table(data)

        # Estilos de la tabla
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ]))

        story.append(t)
        doc.build(story)
        print(f"Informe generado en: {output_path}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")

def obtener_detalles_tablas(cursor, database):
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        tablas = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()
            tablas[table_name] = [col[0] for col in columns]
        return tablas
    except Exception as e:
        print(f"Error al obtener detalles de las tablas: {e}")
        return {}
