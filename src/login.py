import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer
from form_login import Ui_Form


# Nueva función para conectar a MySQL
def conectar_bd():
    import mysql.connector

    return mysql.connector.connect(
        host="crossover.proxy.rlwy.net",
        port=47969,
        user="root",
        password="SLaGFdbUHnvacvsiqkMpoeklIyGjelok",
        database="railway",
    )


def login():
    app = QApplication(sys.argv)
    conexion = conectar_bd()
    # Insertar usuario de prueba

    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            INSERT INTO usuarios (
                numero_economico,
                nombre,
                apellido_p,
                apellido_m,
                fecha_nacimiento,
                sexo,
                telefono,
                email,
                direccion,
                password,
                estado
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """,
            (
                "A001",
                "Alejandro",
                "Ramírez",
                "M",
                "2000-01-01",
                "M",
                "5551234567",
                "alejandro@example.com",
                "Calle Falsa 123",
                "1234",
                True,
            ),
        )
        conexion.commit()
        print("✅ Usuario de prueba insertado")
    except Exception as e:
        print("⚠️ No se pudo insertar el usuario de prueba:", e)

    cursor.close()

    # Cargar estilos si existe el archivo
    qss_path = "estilos/login.qss"
    if os.path.exists(qss_path):
        with open(qss_path, "r") as f:
            app.setStyleSheet(f.read())

    # Inicializar ventana
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)

    # Establecer tamaño fijo del login (igual al diseño)
    window.setFixedSize(590, 420)

    # Centrar la ventana en pantalla al inicio
    screen_geometry = app.primaryScreen().availableGeometry()
    x = int((screen_geometry.width() - window.width()) / 2)
    y = int((screen_geometry.height() - window.height()) / 2)
    window.move(x, y)

    window.show()
    sys.exit(app.exec())


# if __name__ == "__main__":
#     login()
