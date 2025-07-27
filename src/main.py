# main.py
# Aplicación principal – Secundaria UAMITO – RGV Innovations

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación UAMITOS")
        self.setGeometry(100, 100, 1100, 700)
        # Aquí se agregarán los elementos visuales (menús, botones, etc.)

        self.cargar_estilos()

    def cargar_estilos(self):
        file = QFile("estilos/estilos.qss")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            style = stream.readAll()
            self.setStyleSheet(style)
            file.close()

            """ jkladsflkjalñdfjañfj
            """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
