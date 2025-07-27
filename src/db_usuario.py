import sqlite3
import os


def conectar_bd(nombre_db):
    ruta_db = os.path.join(os.path.dirname(__file__), "..", "database", nombre_db)
    abs_path = os.path.abspath(ruta_db)
    print("Ruta abs: ", abs_path)
    return sqlite3.connect(abs_path)


def inicializar_bd(nombre_db):
    try:
        conexion = conectar_bd(nombre_db)
        cursor = conexion.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_economico TEXT,
                nombre TEXT,
                apellido_p TEXT,
                apellido_m TEXT,
                fecha_nacimiento TEXT,
                sexo TEXT,
                telefono TEXT,
                email TEXT,
                direccion TEXT,
                password TEXT,
                estado INTEGER
            );
        """
        )
        conexion.commit()
        conexion.close()
        print(" Base de datos inicializada correctamente")
    except Exception as e:
        print(f" Error al inicializar la base de datos: {e}")
