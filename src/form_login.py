from PySide6 import QtCore, QtGui, QtWidgets
import sys
import os


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.mainWidget = QtWidgets.QWidget(parent=Form)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 590, 420))
        self.mainWidget.setObjectName("mainWidget")

        # Marco derecho (formulario blanco)
        self.backgroundFrame = QtWidgets.QLabel(parent=self.mainWidget)
        self.backgroundFrame.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.backgroundFrame.setObjectName("backgroundFrame")

        # Marco izquierdo con logo
        self.logoFrame = QtWidgets.QLabel(parent=self.mainWidget)
        self.logoFrame.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.logoFrame.setObjectName("logoFrame")

        # Título
        self.titleLabel = QtWidgets.QLabel(parent=self.mainWidget)
        self.titleLabel.setGeometry(QtCore.QRect(350, 80, 161, 41))
        font = QtGui.QFont("Verdana", 15)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        # Inputs
        self.usernameInput = QtWidgets.QLineEdit(parent=self.mainWidget)
        self.usernameInput.setGeometry(QtCore.QRect(335, 150, 190, 40))
        self.usernameInput.setObjectName("usernameInput")

        self.passwordInput = QtWidgets.QLineEdit(parent=self.mainWidget)
        self.passwordInput.setGeometry(QtCore.QRect(335, 200, 190, 40))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordInput.setObjectName("passwordInput")

        # Botón login
        self.loginButton = QtWidgets.QPushButton(parent=self.mainWidget)
        self.loginButton.setGeometry(QtCore.QRect(335, 280, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")

        # Branding
        self.brandingLabel = QtWidgets.QLabel(parent=self.mainWidget)
        self.brandingLabel.setGeometry(QtCore.QRect(120, 330, 111, 41))
        font = QtGui.QFont("Nirmala Text", 20)
        self.brandingLabel.setFont(font)
        self.brandingLabel.setObjectName("brandingLabel")

        # Botón minimizar (dentro del formulario blanco)
        self.minimizeButton = QtWidgets.QPushButton(parent=self.backgroundFrame)
        self.minimizeButton.setGeometry(QtCore.QRect(200, 10, 20, 20))
        self.minimizeButton.setObjectName("minimizeButton")
        self.minimizeButton.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.minimizeButton.setText("–")
        self.minimizeButton.clicked.connect(Form.showMinimized)

        # Botón cerrar (dentro del formulario blanco)
        self.closeButton = QtWidgets.QPushButton(parent=self.backgroundFrame)
        self.closeButton.setGeometry(QtCore.QRect(230, 10, 20, 20))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.closeButton.setText("X")
        self.closeButton.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.titleLabel.setText(_translate("Form", "Inicio de sesión"))
        self.usernameInput.setPlaceholderText(_translate("Form", "Usuario"))
        self.passwordInput.setPlaceholderText(_translate("Form", "Contraseña"))
        self.loginButton.setText(_translate("Form", "Iniciar sesión"))
        self.brandingLabel.setText(_translate("Form", "UAMISys"))
