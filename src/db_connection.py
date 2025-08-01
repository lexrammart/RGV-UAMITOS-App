import pymysql
import bcrypt

HOST = "uamitos-db.cvskmasm6ar9.us-east-2.rds.amazonaws.com"
USER = "admin"
PASSWORD = "mictl4n.!uamitos"
DATABASE = "uamitos"
PORT = 3306


def connect_db():
    try:
        connection = pymysql.connect(
            host=HOST, user=USER, password=PASSWORD, database=DATABASE, port=PORT
        )

        print("Conexión a RDS establecida")

        return connection

    except Exception as e:
        print(f"Error al conectar RDS: {e}")
        return None


def login_validation(email, password):
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("SELECT contrasena FROM usuarios WHERE email = %s", (email,))

        result = cursor.fetchone()

        if result:
            saved_hash = result[0]
            if bcrypt.checkpw(password.encode("utf-8"), saved_hash.encode("utf-8")):
                print("Login exitoso...")
                pass
            else:
                print("Constraseña incorrecta...")
        else:
            print("Usuario no encontrado...")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"ERROR DE LOGIN {e}")


# Inserta usuarios temporales automáticamente al establecer la primera conexión
# def insertar_usuarios_temporales():
#     usuarios = [
#         (
#             "U001",
#             "Alejandro",
#             "Ramírez",
#             "M",
#             "2000-01-01",
#             "M",
#             "5551234567",
#             "ale@mail.com",
#             "CDMX",
#             "profesor",
#         ),
#         (
#             "U002",
#             "Gustavo",
#             "González",
#             "C",
#             "2000-01-02",
#             "M",
#             "5557654321",
#             "gus@mail.com",
#             "CDMX",
#             "profesor",
#         ),
#         (
#             "U003",
#             "Leonardo",
#             "Vallejo",
#             "O",
#             "2000-01-03",
#             "M",
#             "5550001111",
#             "leo@mail.com",
#             "CDMX",
#             "profesor",
#         ),
#     ]

#     try:
#         connection = connect_db()
#         cursor = connection.cursor()

#         hashed_password = bcrypt.hashpw(
#             "1234".encode("utf-8"), bcrypt.gensalt()
#         ).decode("utf-8")

#         for u in usuarios:
#             cursor.execute(
#                 """
#                 INSERT INTO usuarios (
#                     numero_economico, nombre, apellido_paterno, apellido_materno,
#                     fecha_nacimiento, sexo, telefono, email, direccion,
#                     rol, contrasena, activo
#                 ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """,
#                 (*u, hashed_password, True),
#             )

#         connection.commit()
#         cursor.close()
#         connection.close()
#         print("✅ Usuarios temporales insertados correctamente")
#     except Exception as e:
#         print(f"❌ Error al insertar usuarios temporales: {e}")
