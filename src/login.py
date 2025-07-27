import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from form_login import Ui_Form
from db_usuario import *


def login():
    app = QApplication(sys.argv)

    qss_path = "styles/login.qss"
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

    @Slot()
    def user_login():
        try:
            conexion = conectar_bd("usuarios.db")
            print("Conexxión a DB con SQLite")
            conexion.close()
        except Exception as e:
            print(f"Error de conexión")

    ui.loginButton.clicked.connect(user_login)

    window.show()
    sys.exit(app.exec())


# if __name__ == "__main__":
#     login()
