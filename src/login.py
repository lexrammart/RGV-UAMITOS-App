from PySide6 import QtCore, QtGui, QtWidgets
import sys
import os
from db_connection import login_validation


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.mainWidget = QtWidgets.QWidget(parent=Form)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 590, 420))
        self.mainWidget.setObjectName("mainWidget")

        self.backgroundFrame = QtWidgets.QLabel(parent=self.mainWidget)
        self.backgroundFrame.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.backgroundFrame.setObjectName("backgroundFrame")

        self.logoFrame = QtWidgets.QLabel(parent=self.mainWidget)
        self.logoFrame.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.logoFrame.setObjectName("logoFrame")
        sombra = QtWidgets.QGraphicsDropShadowEffect()
        sombra.setBlurRadius(20)
        sombra.setOffset(3, 0)
        sombra.setColor(QtGui.QColor(0, 0, 0, 140))
        self.logoFrame.setGraphicsEffect(sombra)

        self.titleLabel = QtWidgets.QLabel(parent=self.mainWidget)
        self.titleLabel.setGeometry(QtCore.QRect(350, 80, 161, 41))
        font = QtGui.QFont("Verdana", 15)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        self.usernameInput = QtWidgets.QLineEdit(parent=self.mainWidget)
        self.usernameInput.setGeometry(QtCore.QRect(335, 150, 190, 40))
        self.usernameInput.setObjectName("usernameInput")
        self.usernameInput.setPlaceholderText("Usuario")
        self.usernameInput.setFocus()

        self.passwordInput = QtWidgets.QLineEdit(parent=self.mainWidget)
        self.passwordInput.setGeometry(QtCore.QRect(335, 200, 190, 40))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.passwordInput.setPlaceholderText("Contraseña")

        self.togglePassword = QtWidgets.QPushButton(parent=self.passwordInput)
        self.togglePassword.setGeometry(QtCore.QRect(165, 5, 24, 30))
        self.togglePassword.setCheckable(True)
        self.togglePassword.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.togglePassword.setStyleSheet("border: none;")
        self.togglePassword.setIcon(QtGui.QIcon("recursos/ojo-cerrado.png"))

        self.loginButton = QtWidgets.QPushButton(parent=self.mainWidget)
        self.loginButton.setGeometry(QtCore.QRect(335, 280, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setEnabled(False)

        self.errorLabel = QtWidgets.QLabel(parent=self.mainWidget)
        self.errorLabel.setGeometry(QtCore.QRect(335, 250, 190, 20))
        self.errorLabel.setStyleSheet("color: red;")
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setText("")
        self.errorLabel.setVisible(False)

        self.brandingLabel = QtWidgets.QLabel(parent=self.mainWidget)
        self.brandingLabel.setGeometry(QtCore.QRect(120, 330, 111, 41))
        font = QtGui.QFont("Nirmala Text", 20)
        self.brandingLabel.setFont(font)
        self.brandingLabel.setObjectName("brandingLabel")

        self.minimizeButton = QtWidgets.QPushButton(parent=self.backgroundFrame)
        self.minimizeButton.setGeometry(QtCore.QRect(200, 10, 20, 20))
        self.minimizeButton.setObjectName("minimizeButton")
        self.minimizeButton.setText("–")

        self.closeButton = QtWidgets.QPushButton(parent=self.backgroundFrame)
        self.closeButton.setGeometry(QtCore.QRect(230, 10, 20, 20))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setText("X")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.titleLabel.setText(_translate("Form", "Inicio de sesión"))
        self.loginButton.setText(_translate("Form", "Iniciar sesión"))
        self.brandingLabel.setText(_translate("Form", "UAMISys"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    if os.path.exists("qss/login.qss"):
        with open("qss/login.qss", "r") as f:
            app.setStyleSheet(f.read())

    window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(window)

    # Mostrar / ocultar contraseña
    ui.togglePassword.clicked.connect(
        lambda: ui.passwordInput.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Normal
            if ui.togglePassword.isChecked()
            else QtWidgets.QLineEdit.EchoMode.Password
        )
    )

    def verificar_campos():
        lleno = ui.usernameInput.text().strip() and ui.passwordInput.text().strip()
        ui.loginButton.setEnabled(bool(lleno))

    def handle_login():
        email = ui.usernameInput.text().strip()
        password = ui.passwordInput.text().strip()

        result = login_validation(email, password)
        if result == "OK":
            ui.errorLabel.setVisible(False)
            print("Login exitoso desde la consola")
            # Aquí podrías cerrar esta ventana y abrir la ventana principal de tu aplicación
        else:
            ui.errorLabel.setText(result)
            ui.errorLabel.setVisible(True)

    ui.loginButton.clicked.connect(handle_login)
    ui.usernameInput.textChanged.connect(verificar_campos)
    ui.passwordInput.textChanged.connect(verificar_campos)
    ui.minimizeButton.clicked.connect(window.showMinimized)
    ui.closeButton.clicked.connect(window.close)
    ui.usernameInput.returnPressed.connect(ui.passwordInput.setFocus)
    ui.passwordInput.returnPressed.connect(ui.loginButton.click)

    # Mover ventana arrastrando
    def mousePressEvent(event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            window.drag_position = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            window.move(
                window.pos() + event.globalPosition().toPoint() - window.drag_position
            )
            window.drag_position = event.globalPosition().toPoint()
            event.accept()

    window.mousePressEvent = mousePressEvent
    window.mouseMoveEvent = mouseMoveEvent

    window.setFixedSize(590, 420)
    screen = app.primaryScreen().availableGeometry()
    window.move((screen.width() - 590) // 2, (screen.height() - 420) // 2)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
