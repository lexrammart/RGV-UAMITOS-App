from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QActionGroup
import sys
import datetime
import subprocess
import recursos_maestros
from db_connection import connect_db
from data_access.insertar_datos_dao import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1580, 904)
        MainWindow.setMinimumSize(QtCore.QSize(1580, 904))
        MainWindow.setMaximumSize(QtCore.QSize(1580, 904))
        self.contenedo_principal = QtWidgets.QWidget(parent=MainWindow)
        self.contenedo_principal.setObjectName("contenedo_principal")
        self.gridLayout = QtWidgets.QGridLayout(self.contenedo_principal)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.contenedor_secundario = QtWidgets.QWidget(parent=self.contenedo_principal)
        self.contenedor_secundario.setObjectName("contenedor_secundario")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.contenedor_secundario)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtWidgets.QWidget(parent=self.contenedor_secundario)
        self.widget.setMinimumSize(QtCore.QSize(0, 45))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 6, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_menu = QtWidgets.QPushButton(parent=self.widget)
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/lista.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(20, 20))
        self.btn_menu.setCheckable(True)
        self.btn_menu.setAutoExclusive(False)
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_4.addWidget(self.btn_menu)
        spacerItem = QtWidgets.QSpacerItem(
            422,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_buscar = QtWidgets.QLineEdit(parent=self.widget)
        self.input_buscar.setObjectName("input_buscar")
        self.horizontalLayout.addWidget(self.input_buscar)
        self.btn_buscar = QtWidgets.QPushButton(parent=self.widget)
        self.btn_buscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/buscar.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_buscar.setIcon(icon1)
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout.addWidget(self.btn_buscar)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(
            422,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btn_user = QtWidgets.QPushButton(parent=self.widget)
        self.btn_user.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/usuario.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon2.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/usuario2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_user.setIcon(icon2)
        self.btn_user.setIconSize(QtCore.QSize(20, 20))
        self.btn_user.setCheckable(True)
        self.btn_user.setAutoExclusive(True)
        self.btn_user.setObjectName("btn_user")
        self.horizontalLayout_4.addWidget(self.btn_user)
        self.verticalLayout_7.addWidget(self.widget)
        self.contendor_contenido = QtWidgets.QStackedWidget(
            parent=self.contenedor_secundario
        )
        self.contendor_contenido.setMinimumSize(QtCore.QSize(0, 0))
        self.contendor_contenido.setObjectName("contendor_contenido")
        ########## pagina bienvenida ##########
        # === Página de Bienvenida ===
        self.pagina_bienvenida = QtWidgets.QWidget()
        self.pagina_bienvenida.setObjectName("pagina_bienvenida")

        # Layout central
        self.layout_bienvenida = QtWidgets.QVBoxLayout(self.pagina_bienvenida)
        self.layout_bienvenida.setContentsMargins(0, 50, 0, 0)
        self.layout_bienvenida.setSpacing(20)
        self.layout_bienvenida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # === Label de saludo dinámico ===
        self.label_bienvenida = QtWidgets.QLabel()
        font_b = QtGui.QFont()
        font_b.setFamily("Verdana")
        font_b.setPointSize(24)
        font_b.setBold(True)
        self.label_bienvenida.setFont(font_b)
        self.label_bienvenida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_bienvenida.addWidget(self.label_bienvenida)

        # === Label de la hora ===
        self.label_hora = QtWidgets.QLabel()
        font_hora = QtGui.QFont()
        font_hora.setFamily("Consolas")
        font_hora.setPointSize(22)
        self.label_hora.setFont(font_hora)
        self.label_hora.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_bienvenida.addWidget(self.label_hora)

        # === Imagen central ===
        self.label_imagen = QtWidgets.QLabel()
        self.label_imagen.setPixmap(QtGui.QPixmap("./recursos/imagen1.png"))
        self.label_imagen.setScaledContents(True)
        self.label_imagen.setFixedSize(450, 300)
        self.label_imagen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_bienvenida.addWidget(self.label_imagen)

        # ✅ Agregar al QStacked principal
        self.contendor_contenido.addWidget(self.pagina_bienvenida)

        ########## fin pagina bienvenida ##########
        ########## pagina materias ##########
        # === Página Mis Materias ===
        self.pagina_materias = QtWidgets.QWidget()
        self.pagina_materias.setObjectName("pagina_materias")
        self.layout_materias = QtWidgets.QVBoxLayout(self.pagina_materias)

        # === QToolBar ===
        self.toolbar_materias = QtWidgets.QToolBar()
        self.toolbar_materias.setMovable(False)
        self.layout_materias.addWidget(self.toolbar_materias)

        # === Acciones de QToolBar ===
        self.action_ver_materias = QtGui.QAction("Ver Materias", MainWindow)
        self.action_lista_alumnos = QtGui.QAction("Lista de Alumnos", MainWindow)
        self.action_imprimir_asistencia = QtGui.QAction(
            "Imprimir Asistencia", MainWindow
        )

        self.toolbar_materias.addAction(self.action_ver_materias)
        self.toolbar_materias.addAction(self.action_lista_alumnos)
        self.toolbar_materias.addAction(self.action_imprimir_asistencia)

        # === Stacked interno ===
        self.stack_materias = QtWidgets.QStackedWidget()
        self.layout_materias.addWidget(self.stack_materias)

        # Páginas internas
        self.page_ver_materias = QtWidgets.QWidget()
        self.page_lista_alumnos = QtWidgets.QWidget()
        self.page_imprimir_asistencia = QtWidgets.QWidget()

        self.stack_materias.addWidget(self.page_ver_materias)
        self.stack_materias.addWidget(self.page_lista_alumnos)
        self.stack_materias.addWidget(self.page_imprimir_asistencia)

        # === Conexión de acciones ===
        self.action_ver_materias.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_ver_materias)
        )
        self.action_lista_alumnos.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_lista_alumnos)
        )
        self.action_imprimir_asistencia.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_imprimir_asistencia)
        )

        # ✅ Hacer acciones checkables y exclusivas
        from PySide6.QtGui import QActionGroup

        self.action_group_materias = QActionGroup(MainWindow)
        self.action_group_materias.setExclusive(True)
        for action in [
            self.action_ver_materias,
            self.action_lista_alumnos,
            self.action_imprimir_asistencia,
        ]:
            action.setCheckable(True)
            self.action_group_materias.addAction(action)

        # ✅ Agregar la página al Stacked principal
        self.contendor_contenido.addWidget(self.pagina_materias)

        ########## fin pagina materias ##########
        ########## pagina horario ##########
        # === Página Mi Horario ===
        self.pagina_horario = QtWidgets.QWidget()
        self.pagina_horario.setObjectName("pagina_horario")
        self.layout_horario = QtWidgets.QVBoxLayout(self.pagina_horario)

        self.label_horario = QtWidgets.QLabel("Aquí se mostrará el horario del maestro")
        self.label_horario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_horario.addWidget(self.label_horario)

        self.btn_imprimir_horario = QtWidgets.QPushButton("Imprimir Horario en PDF")
        self.layout_horario.addWidget(self.btn_imprimir_horario)

        # ✅ Agregar al QStacked principal
        self.contendor_contenido.addWidget(self.pagina_horario)

        ########## fin pagina horario ##########
        ########## pagina mensajes ##########
        # === Página Mensajes ===
        self.pagina_mensajes = QtWidgets.QWidget()
        self.pagina_mensajes.setObjectName("pagina_mensajes")
        self.layout_mensajes = QtWidgets.QVBoxLayout(self.pagina_mensajes)

        self.lista_mensajes = QtWidgets.QListWidget()
        self.lista_mensajes.addItems(["Aviso 1", "Aviso 2", "Aviso 3"])
        self.layout_mensajes.addWidget(self.lista_mensajes)

        # ✅ Agregar al QStacked principal
        self.contendor_contenido.addWidget(self.pagina_mensajes)

        ########## Página Mensajes ##########
        ########## pagina perfil ##########
        # === Página Perfil ===
        self.pagina_perfil = QtWidgets.QWidget()
        self.pagina_perfil.setObjectName("pagina_perfil")
        self.layout_perfil = QtWidgets.QVBoxLayout(self.pagina_perfil)

        self.label_titulo_perfil = QtWidgets.QLabel("Perfil del Maestro")
        font_perfil = QtGui.QFont()
        font_perfil.setPointSize(20)
        font_perfil.setBold(True)
        self.label_titulo_perfil.setFont(font_perfil)
        self.label_titulo_perfil.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_perfil.addWidget(self.label_titulo_perfil)

        self.input_correo = QtWidgets.QLineEdit()
        self.input_correo.setPlaceholderText("Correo electrónico")
        self.input_direccion = QtWidgets.QLineEdit()
        self.input_direccion.setPlaceholderText("Dirección")
        self.input_password = QtWidgets.QLineEdit()
        self.input_password.setPlaceholderText("Contraseña")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.layout_perfil.addWidget(self.input_correo)
        self.layout_perfil.addWidget(self.input_direccion)
        self.layout_perfil.addWidget(self.input_password)

        self.btn_guardar_perfil = QtWidgets.QPushButton("Guardar Cambios")
        self.layout_perfil.addWidget(self.btn_guardar_perfil)

        # ✅ Agregar al QStacked principal
        self.contendor_contenido.addWidget(self.pagina_perfil)

        ######### fin pagina perfil ##########
        ######### pagina acerca de ##########
        ######### pagina acerca de ##########
        # === Página Acerca de ===
        self.pagina_acercade = QtWidgets.QWidget()
        self.pagina_acercade.setObjectName("pagina_acercade")
        layout_acercade = QtWidgets.QVBoxLayout(self.pagina_acercade)
        layout_acercade.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Logo o imagen de la institución
        self.logo_rgv = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("./recursos/RGV_Innovations.png")
        pixmap = pixmap.scaled(
            400,
            400,
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation,
        )
        self.logo_rgv.setPixmap(pixmap)
        self.logo_rgv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Título principal
        self.label_titulo_rgv = QtWidgets.QLabel("UAMISys")
        font_titulo = QtGui.QFont()
        font_titulo.setPointSize(26)
        font_titulo.setBold(True)
        self.label_titulo_rgv.setFont(font_titulo)
        self.label_titulo_rgv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Subtítulo
        self.label_subtitulo_rgv = QtWidgets.QLabel(
            "Sistema Integral de Gestión Académica"
        )
        font_sub = QtGui.QFont()
        font_sub.setPointSize(14)
        self.label_subtitulo_rgv.setFont(font_sub)
        self.label_subtitulo_rgv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Créditos
        self.label_creditos = QtWidgets.QLabel(
            "Este programa fue desarrollado por <b>RGV Innovations</b><br>"
            "Con el objetivo de optimizar la gestión académica y<br>"
            "ofrecer una experiencia moderna y eficiente.<br><br>"
            "Repositorio disponible en:"
        )
        font_creditos = QtGui.QFont()
        font_creditos.setPointSize(12)
        self.label_creditos.setFont(font_creditos)
        self.label_creditos.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_creditos.setWordWrap(True)

        # Link de GitHub
        self.link_github = QtWidgets.QLabel()
        self.link_github.setText(
            '<a href="https://github.com/lexrammart/RGV-UAMITOS-App" style="color: #1565c0;">'
            "https://github.com/lexrammart/RGV-UAMITOS-App</a>"
        )
        self.link_github.setFont(font_creditos)
        self.link_github.setOpenExternalLinks(True)
        self.link_github.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # === Añadir al layout ===
        layout_acercade.addStretch()
        layout_acercade.addWidget(self.logo_rgv)
        layout_acercade.addSpacing(10)
        layout_acercade.addWidget(self.label_titulo_rgv)
        layout_acercade.addWidget(self.label_subtitulo_rgv)
        layout_acercade.addSpacing(20)
        layout_acercade.addWidget(self.label_creditos)
        layout_acercade.addWidget(self.link_github)
        layout_acercade.addStretch()

        # ✅ Agregar al QStacked principal
        self.contendor_contenido.addWidget(self.pagina_acercade)
        ######### fin pagina acerca de ##########

        self.verticalLayout_7.addWidget(self.contendor_contenido)
        self.gridLayout.addWidget(self.contenedor_secundario, 0, 2, 1, 1)
        self.contenedor_menu_completo = QtWidgets.QWidget(
            parent=self.contenedo_principal
        )
        self.contenedor_menu_completo.setObjectName("contenedor_menu_completo")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.contenedor_menu_completo)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.logo_titulo = QtWidgets.QHBoxLayout()
        self.logo_titulo.setSpacing(0)
        self.logo_titulo.setObjectName("logo_titulo")
        self.logo_1 = QtWidgets.QLabel(parent=self.contenedor_menu_completo)
        self.logo_1.setMinimumSize(QtCore.QSize(50, 40))
        self.logo_1.setMaximumSize(QtCore.QSize(50, 40))
        self.logo_1.setText("")
        self.logo_1.setPixmap(QtGui.QPixmap(":/recursos/recursos/logoUamitos.png"))
        self.logo_1.setScaledContents(True)
        self.logo_1.setObjectName("logo_1")
        self.logo_titulo.addWidget(self.logo_1)
        self.titulo = QtWidgets.QLabel(parent=self.contenedor_menu_completo)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.logo_titulo.addWidget(self.titulo)
        self.verticalLayout_6.addLayout(self.logo_titulo)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_inicio_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/casa.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon3.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/casa-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_inicio_texto.setIcon(icon3)
        self.btn_inicio_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_inicio_texto.setCheckable(True)
        self.btn_inicio_texto.setAutoExclusive(True)
        self.btn_inicio_texto.setObjectName("btn_inicio_texto")
        self.verticalLayout_2.addWidget(self.btn_inicio_texto)
        self.btn_materias_texto_2 = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/libros-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon4.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/libros-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_materias_texto_2.setIcon(icon4)
        self.btn_materias_texto_2.setIconSize(QtCore.QSize(20, 20))
        self.btn_materias_texto_2.setCheckable(True)
        self.btn_materias_texto_2.setAutoExclusive(True)
        self.btn_materias_texto_2.setObjectName("btn_materias_texto_2")
        self.verticalLayout_2.addWidget(self.btn_materias_texto_2)
        self.btn_horario_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/calendario.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon5.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/calendario-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_horario_texto.setIcon(icon5)
        self.btn_horario_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_horario_texto.setCheckable(True)
        self.btn_horario_texto.setAutoExclusive(True)
        self.btn_horario_texto.setObjectName("btn_horario_texto")
        self.verticalLayout_2.addWidget(self.btn_horario_texto)
        self.btn_mensajes_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/mensajes.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon6.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/mensajes-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_mensajes_texto.setIcon(icon6)
        self.btn_mensajes_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_mensajes_texto.setCheckable(True)
        self.btn_mensajes_texto.setAutoExclusive(True)
        self.btn_mensajes_texto.setObjectName("btn_mensajes_texto")
        self.verticalLayout_2.addWidget(self.btn_mensajes_texto)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            611,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_6.addItem(spacerItem2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_acercade_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/acerca-de-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon7.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/acerca-de.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_acercade_texto.setIcon(icon7)
        self.btn_acercade_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_acercade_texto.setCheckable(True)
        self.btn_acercade_texto.setAutoExclusive(True)
        self.btn_acercade_texto.setObjectName("btn_acercade_texto")
        self.verticalLayout_5.addWidget(self.btn_acercade_texto)
        self.btn_logout_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/cerrar-sesion-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon8.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/cerrar-sesion-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_logout_texto.setIcon(icon8)
        self.btn_logout_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_logout_texto.setCheckable(True)
        self.btn_logout_texto.setAutoExclusive(True)
        self.btn_logout_texto.setObjectName("btn_logout_texto")
        self.verticalLayout_5.addWidget(self.btn_logout_texto)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.contenedor_menu_completo, 0, 1, 1, 1)
        self.contenedor_menu_iconos = QtWidgets.QWidget(parent=self.contenedo_principal)
        self.contenedor_menu_iconos.setMaximumSize(QtCore.QSize(75, 16777215))
        self.contenedor_menu_iconos.setObjectName("contenedor_menu_iconos")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.contenedor_menu_iconos)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo_layout = QtWidgets.QHBoxLayout()
        self.logo_layout.setObjectName("logo_layout")
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.logo_layout.addItem(spacerItem3)
        self.logo = QtWidgets.QLabel(parent=self.contenedor_menu_iconos)
        self.logo.setMinimumSize(QtCore.QSize(60, 50))
        self.logo.setMaximumSize(QtCore.QSize(70, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/recursos/recursos/logoUamitos.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.logo_layout.addWidget(self.logo)
        spacerItem4 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.logo_layout.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.logo_layout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_inicio = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_inicio.setText("")
        self.btn_inicio.setIcon(icon3)
        self.btn_inicio.setIconSize(QtCore.QSize(26, 26))
        self.btn_inicio.setCheckable(True)
        self.btn_inicio.setAutoExclusive(True)
        self.btn_inicio.setObjectName("btn_inicio")
        self.verticalLayout.addWidget(self.btn_inicio)
        self.btn_materias = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_materias.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/libros-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon9.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/libros-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon9.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/libros-1.png"),
            QtGui.QIcon.Mode.Disabled,
            QtGui.QIcon.State.On,
        )
        self.btn_materias.setIcon(icon9)
        self.btn_materias.setIconSize(QtCore.QSize(26, 26))
        self.btn_materias.setCheckable(True)
        self.btn_materias.setAutoExclusive(True)
        self.btn_materias.setObjectName("btn_materias")
        self.verticalLayout.addWidget(self.btn_materias)
        self.btn_horario = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_horario.setText("")
        self.btn_horario.setIcon(icon5)
        self.btn_horario.setIconSize(QtCore.QSize(26, 26))
        self.btn_horario.setCheckable(True)
        self.btn_horario.setAutoExclusive(True)
        self.btn_horario.setObjectName("btn_horario")
        self.verticalLayout.addWidget(self.btn_horario)
        self.btn_mensajes = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_mensajes.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/mensajes.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon10.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/mensajes-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon10.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/libros-1.png"),
            QtGui.QIcon.Mode.Disabled,
            QtGui.QIcon.State.On,
        )
        self.btn_mensajes.setIcon(icon10)
        self.btn_mensajes.setIconSize(QtCore.QSize(26, 26))
        self.btn_mensajes.setCheckable(True)
        self.btn_mensajes.setAutoExclusive(True)
        self.btn_mensajes.setObjectName("btn_mensajes")
        self.verticalLayout.addWidget(self.btn_mensajes)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(
            20,
            589,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_4.addItem(spacerItem5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_acercade = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_acercade.setText("")
        self.btn_acercade.setIcon(icon7)
        self.btn_acercade.setIconSize(QtCore.QSize(26, 26))
        self.btn_acercade.setCheckable(True)
        self.btn_acercade.setAutoExclusive(True)
        self.btn_acercade.setObjectName("btn_acercade")
        self.verticalLayout_3.addWidget(self.btn_acercade)
        self.btn_logout = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_logout.setText("")
        self.btn_logout.setIcon(icon8)
        self.btn_logout.setIconSize(QtCore.QSize(26, 26))
        self.btn_logout.setCheckable(True)
        self.btn_logout.setAutoExclusive(True)
        self.btn_logout.setObjectName("btn_logout")
        self.verticalLayout_3.addWidget(self.btn_logout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.contenedor_menu_iconos, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.contenedo_principal)

        self.retranslateUi(MainWindow)
        self.contendor_contenido.setCurrentIndex(5)
        self.btn_menu.toggled["bool"].connect(self.contenedor_menu_iconos.setVisible)  # type: ignore
        self.btn_menu.toggled["bool"].connect(self.contenedor_menu_completo.setHidden)  # type: ignore
        self.btn_inicio.toggled["bool"].connect(self.btn_inicio_texto.setChecked)  # type: ignore
        self.btn_materias.toggled["bool"].connect(self.btn_materias_texto_2.setChecked)  # type: ignore
        self.btn_horario.toggled["bool"].connect(self.btn_horario_texto.setChecked)  # type: ignore
        self.btn_mensajes.toggled["bool"].connect(self.btn_mensajes_texto.setChecked)  # type: ignore
        self.btn_inicio_texto.toggled["bool"].connect(self.btn_inicio.setChecked)  # type: ignore
        self.btn_materias_texto_2.toggled["bool"].connect(self.btn_materias.setChecked)  # type: ignore
        self.btn_horario_texto.toggled["bool"].connect(self.btn_horario.setChecked)  # type: ignore
        self.btn_mensajes_texto.toggled["bool"].connect(self.btn_mensajes.setChecked)  # type: ignore
        self.btn_acercade_texto.toggled["bool"].connect(self.btn_acercade.setChecked)  # type: ignore
        self.btn_logout_texto.toggled["bool"].connect(self.btn_logout.setChecked)  # type: ignore
        self.btn_logout.toggled["bool"].connect(self.btn_logout_texto.setChecked)  # type: ignore
        self.btn_logout_texto.clicked.connect(MainWindow.close)  # type: ignore
        self.btn_logout.clicked.connect(MainWindow.close)  # type: ignore
        self.btn_logout.toggled["bool"].connect(self.btn_logout_texto.setChecked)  # type: ignore
        self.btn_acercade.toggled["bool"].connect(self.btn_acercade_texto.setChecked)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # === Conexiones Sidebar ===
        self.btn_inicio.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_bienvenida)
        )
        self.btn_inicio_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_bienvenida)
        )

        self.btn_materias.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_materias)
        )
        self.btn_materias_texto_2.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_materias)
        )

        self.btn_horario.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_horario)
        )
        self.btn_horario_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_horario)
        )

        self.btn_mensajes.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_mensajes)
        )
        self.btn_mensajes_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_mensajes)
        )

        self.btn_user.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_perfil)
        )
        # === Conexiones Acerca de ===
        self.btn_acercade.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_acercade)
        )
        self.btn_acercade_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_acercade)
        )

        # === Conexiones QToolBar (Mis Materias) ===
        self.action_ver_materias.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_ver_materias)
        )
        self.action_lista_alumnos.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_lista_alumnos)
        )
        self.action_imprimir_asistencia.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_imprimir_asistencia)
        )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UamiSys"))
        self.input_buscar.setPlaceholderText(_translate("MainWindow", "Buscar"))
        self.titulo.setText(_translate("MainWindow", "UAMISys"))
        self.btn_inicio_texto.setText(_translate("MainWindow", "Inicio"))
        self.btn_materias_texto_2.setText(_translate("MainWindow", "Mis materias"))
        self.btn_horario_texto.setText(_translate("MainWindow", "Mi horario"))
        self.btn_mensajes_texto.setText(_translate("MainWindow", "Mensajes"))
        self.btn_acercade_texto.setText(_translate("MainWindow", "Acerca dé"))
        self.btn_logout_texto.setText(_translate("MainWindow", "Cerrar sesión"))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # conexión cerrar sesión
        self.ui.btn_logout.clicked.connect(self.cerrar_sesion)
        self.ui.btn_logout_texto.clicked.connect(self.cerrar_sesion)

        # ✅ Ocultar menú de iconos al iniciar y mostrar página de bienvenida
        self.ui.contenedor_menu_iconos.hide()
        self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_bienvenida)
        self.ui.btn_inicio.setChecked(True)

        # ✅ Configurar saludo inicial
        self.actualizar_bienvenida()

        # ✅ Actualizar cada minuto la hora y el saludo
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizar_bienvenida)
        self.timer.start(60000)  # 60 segundos

        # ✅ Mostrar página de bienvenida al inicio
        self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_bienvenida)
        self.ui.btn_inicio_texto.setChecked(True)  # 🔹 Activa el botón de texto
        self.ui.btn_inicio.setChecked(
            False
        )  # 🔹 Asegura que el de icono NO esté activo

    # === Función para actualizar saludo dinámico ===
    def actualizar_bienvenida(self):
        import datetime

        ahora = datetime.datetime.now()
        hora = ahora.strftime("%I:%M %p")

        if ahora.hour < 12:
            saludo = "Buenos días"
        elif ahora.hour < 19:
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"

        self.ui.label_bienvenida.setText(f"{saludo} Uammito")
        self.ui.label_hora.setText(hora)

    def cerrar_sesion(self):
        import subprocess
        import sys
        import os

        ruta_login = os.path.join(os.path.dirname(__file__), "login.py")
        print("⚠️ Cerrando sesión y lanzando login.py...")
        subprocess.Popen([sys.executable, ruta_login])
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("./qss/estilos.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
