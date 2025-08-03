import pymysql
import bcrypt
import subprocess


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
    connection = connect_db()
    if not connection:
        return None, "Error de conexión a la base de datos."

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(
                "SELECT contrasena, rol FROM usuarios WHERE email = %s AND activo = TRUE",
                (email,),
            )
            result = cursor.fetchone()

            if not result:
                return None, "El usuario no existe."

            saved_hash = result["contrasena"].encode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), saved_hash):
                rol = result["rol"]
                return rol, "OK"
            else:
                return None, "Contraseña incorrecta."
    except Exception as e:
        print(f"ERROR DE LOGIN {e}")
        return None, "Error durante la validación."
    finally:
        connection.close()


#############################################################################################

# def insertar_usuarios_admin_prof():
#     usuarios = [
#         {
#             "numero_economico": "A010",
#             "nombre": "David",
#             "apellido_paterno": "Aranda",
#             "apellido_materno": "A",
#             "fecha_nacimiento": "2000-01-01",
#             "sexo": "M",
#             "telefono": "5550001234",
#             "email": "admin.david@admin.com",
#             "direccion": "CDMX",
#             "rol": "administrativo",
#             "contrasena": "admin",
#         },
#         {
#             "numero_economico": "P001",
#             "nombre": "Raziel",
#             "apellido_paterno": "Soto",
#             "apellido_materno": "J",
#             "fecha_nacimiento": "1995-08-20",
#             "sexo": "M",
#             "telefono": "5550005678",
#             "email": "prof.raziel@prof.com",
#             "direccion": "CDMX",
#             "rol": "profesor",
#             "contrasena": "admin",
#         },
#     ]

#     try:
#         conn = connect_db()
#         cursor = conn.cursor()

#         for u in usuarios:
#             hashed_password = bcrypt.hashpw(
#                 u["contrasena"].encode("utf-8"), bcrypt.gensalt()
#             ).decode("utf-8")

#             cursor.execute(
#                 """
#                 INSERT INTO usuarios (
#                     numero_economico, nombre, apellido_paterno, apellido_materno,
#                     fecha_nacimiento, sexo, telefono, email, direccion,
#                     rol, contrasena, activo
#                 ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """,
#                 (
#                     u["numero_economico"],
#                     u["nombre"],
#                     u["apellido_paterno"],
#                     u["apellido_materno"],
#                     u["fecha_nacimiento"],
#                     u["sexo"],
#                     u["telefono"],
#                     u["email"],
#                     u["direccion"],
#                     u["rol"],
#                     hashed_password,
#                     True,
#                 ),
#             )

#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("✅ Usuarios insertados correctamente.")
#     except Exception as e:
#         print(f"❌ Error al insertar usuarios: {e}")


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
