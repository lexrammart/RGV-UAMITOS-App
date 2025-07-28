import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

import os

current_dir = os.path.dirname(os.path.abspath(__file__))


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prueba de Ícono Duotone")
        self.setFixedSize(600, 600)

        # Crear botón con ícono
        boton = QToolButton(self)
        boton.setIcon(QIcon(os.path.join(current_dir, "spinner.svg")))
        boton.setIconSize(QSize(500, 500))  # Tamaño del ícono
        boton.setToolTip("Botón de prueba")
        boton.setObjectName("botonDuotone")  # Para aplicarle estilo desde QSS
        boton.move(100, 60)  # Posición del botón en la ventana


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Aplicar QSS
    current_path = os.path.dirname(os.path.abspath(__file__))
    qss_path = os.path.join(current_path, "duotone.qss")
    with open(qss_path, "r") as f:
        app.setStyleSheet(f.read())

    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
