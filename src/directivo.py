from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QActionGroup
import sys
import datetime
import recursos_directivo
import subprocess
import bcrypt
from db_connection import connect_db
from data_access.insertar_datos_dao import *
from PySide6.QtWidgets import QComboBox


class ComboBoxRecargable(QComboBox):
    def __init__(self, cargar_funcion, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cargar_funcion = cargar_funcion

    def showPopup(self):
        self._cargar_funcion()
        super().showPopup()


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
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/casa.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/casa-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_inicio_texto.setIcon(icon)
        self.btn_inicio_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_inicio_texto.setCheckable(True)
        self.btn_inicio_texto.setAutoExclusive(True)
        self.btn_inicio_texto.setObjectName("btn_inicio_texto")
        self.verticalLayout_2.addWidget(self.btn_inicio_texto)
        self.btn_usuarios_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/usuario.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon1.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/usuario2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_usuarios_texto.setIcon(icon1)
        self.btn_usuarios_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_usuarios_texto.setCheckable(True)
        self.btn_usuarios_texto.setAutoExclusive(True)
        self.btn_usuarios_texto.setObjectName("btn_usuarios_texto")
        self.verticalLayout_2.addWidget(self.btn_usuarios_texto)
        self.btn_periodos_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/periodos.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon2.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/perdiodos-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_periodos_texto.setIcon(icon2)
        self.btn_periodos_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_periodos_texto.setCheckable(True)
        self.btn_periodos_texto.setAutoExclusive(True)
        self.btn_periodos_texto.setObjectName("btn_periodos_texto")
        self.verticalLayout_2.addWidget(self.btn_periodos_texto)
        self.btn_materias_horarios_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/libros-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon3.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/libros-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_materias_horarios_texto.setIcon(icon3)
        self.btn_materias_horarios_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_materias_horarios_texto.setCheckable(True)
        self.btn_materias_horarios_texto.setAutoExclusive(True)
        self.btn_materias_horarios_texto.setObjectName("btn_materias_horarios_texto")
        self.verticalLayout_2.addWidget(self.btn_materias_horarios_texto)
        self.btn_reportes_globales_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/reporte-global.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon4.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/reporte-global-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_reportes_globales_texto.setIcon(icon4)
        self.btn_reportes_globales_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_reportes_globales_texto.setCheckable(True)
        self.btn_reportes_globales_texto.setAutoExclusive(True)
        self.btn_reportes_globales_texto.setObjectName("btn_reportes_globales_texto")
        self.verticalLayout_2.addWidget(self.btn_reportes_globales_texto)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            611,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_acercade_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/acerca-de-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon5.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/acerca-de.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_acercade_texto.setIcon(icon5)
        self.btn_acercade_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_acercade_texto.setCheckable(True)
        self.btn_acercade_texto.setAutoExclusive(True)
        self.btn_acercade_texto.setObjectName("btn_acercade_texto")
        self.verticalLayout_5.addWidget(self.btn_acercade_texto)
        self.btn_logout_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/cerrar-sesion-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon6.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/cerrar-sesion.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_logout_texto.setIcon(icon6)
        self.btn_logout_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_logout_texto.setCheckable(True)
        self.btn_logout_texto.setAutoExclusive(True)
        self.btn_logout_texto.setObjectName("btn_logout_texto")
        self.verticalLayout_5.addWidget(self.btn_logout_texto)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.contenedor_menu_completo, 0, 1, 1, 1)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/lista.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_menu.setIcon(icon7)
        self.btn_menu.setIconSize(QtCore.QSize(20, 20))
        self.btn_menu.setCheckable(True)
        self.btn_menu.setAutoExclusive(False)
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_4.addWidget(self.btn_menu)
        spacerItem1 = QtWidgets.QSpacerItem(
            422,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_buscar = QtWidgets.QLineEdit(parent=self.widget)
        self.input_buscar.setObjectName("input_buscar")
        self.horizontalLayout.addWidget(self.input_buscar)
        self.btn_buscar = QtWidgets.QPushButton(parent=self.widget)
        self.btn_buscar.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/buscar.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_buscar.setIcon(icon8)
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout.addWidget(self.btn_buscar)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(
            422,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btn_user = QtWidgets.QPushButton(parent=self.widget)
        self.btn_user.setText("")
        self.btn_user.setIcon(icon1)
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
        # ===============================
        # 📌 Página de Usuarios
        # ===============================
        self.pagina_usuarios = QtWidgets.QWidget()
        self.pagina_usuarios.setObjectName("pagina_usuarios")
        self.layout_usuarios = QtWidgets.QVBoxLayout(self.pagina_usuarios)

        # === QToolBar de Usuarios ===
        self.toolbar_usuarios = QtWidgets.QToolBar()
        self.toolbar_usuarios.setMovable(False)
        self.layout_usuarios.addWidget(self.toolbar_usuarios)

        # 🔹 Acciones
        self.action_alta_usuario = QtGui.QAction("Alta Usuarios", MainWindow)
        self.action_baja_usuario = QtGui.QAction("Baja Usuarios", MainWindow)
        self.action_cambiar_roles = QtGui.QAction("Cambiar Roles", MainWindow)
        self.action_cambiar_password = QtGui.QAction(
            "Asignar/Cambiar Contraseña", MainWindow
        )

        self.action_alta_usuario.setCheckable(True)
        self.action_baja_usuario.setCheckable(True)
        self.action_cambiar_roles.setCheckable(True)
        self.action_cambiar_password.setCheckable(True)

        self.toolbar_usuarios.addAction(self.action_alta_usuario)
        self.toolbar_usuarios.addAction(self.action_baja_usuario)
        self.toolbar_usuarios.addAction(self.action_cambiar_roles)
        self.toolbar_usuarios.addAction(self.action_cambiar_password)

        # === Agrupar acciones para exclusividad ===
        self.action_group_usuarios = QtGui.QActionGroup(MainWindow)
        self.action_group_usuarios.setExclusive(True)
        self.action_group_usuarios.addAction(self.action_alta_usuario)
        self.action_group_usuarios.addAction(self.action_baja_usuario)
        self.action_group_usuarios.addAction(self.action_cambiar_roles)
        self.action_group_usuarios.addAction(self.action_cambiar_password)

        # === Stacked interno de usuarios ===
        self.stack_usuarios = QtWidgets.QStackedWidget()
        self.layout_usuarios.addWidget(self.stack_usuarios)

        # ===============================
        # 🚀 Alta de Usuario
        # ===============================
        self.page_alta_usuario = QtWidgets.QWidget()
        alta_u_layout = QtWidgets.QVBoxLayout(self.page_alta_usuario)

        group_datos_personales_u = QtWidgets.QGroupBox("Datos Personales")
        form_personales_u = QtWidgets.QFormLayout(group_datos_personales_u)
        self.input_nombre_u_alta = QtWidgets.QLineEdit()
        self.input_ap_paterno_u_alta = QtWidgets.QLineEdit()
        self.input_ap_materno_u_alta = QtWidgets.QLineEdit()
        self.input_fecha_nac_u_alta = QtWidgets.QDateEdit()
        self.input_fecha_nac_u_alta.setCalendarPopup(True)
        self.input_fecha_nac_u_alta.setDisplayFormat("dd/MM/yyyy")
        self.input_direccion_u_alta = QtWidgets.QLineEdit()
        self.input_telefono_u_alta = QtWidgets.QLineEdit()
        self.input_correo_u_alta = QtWidgets.QLineEdit()

        form_personales_u.addRow("Nombre(s):", self.input_nombre_u_alta)
        form_personales_u.addRow("Apellido Paterno:", self.input_ap_paterno_u_alta)
        form_personales_u.addRow("Apellido Materno:", self.input_ap_materno_u_alta)
        form_personales_u.addRow("Fecha de Nacimiento:", self.input_fecha_nac_u_alta)
        form_personales_u.addRow("Dirección:", self.input_direccion_u_alta)
        form_personales_u.addRow("Teléfono:", self.input_telefono_u_alta)
        form_personales_u.addRow("Correo:", self.input_correo_u_alta)

        group_datos_laborales_u = QtWidgets.QGroupBox("Datos Laborales")
        form_laborales_u = QtWidgets.QFormLayout(group_datos_laborales_u)
        self.input_numero_economico_u_alta = QtWidgets.QLineEdit()
        self.combo_rol_u_alta = QtWidgets.QComboBox()
        self.combo_rol_u_alta.addItems(["Maestro", "Administrativo", "Directivo"])
        self.input_password_u_alta = QtWidgets.QLineEdit()
        self.input_password_u_alta.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.check_activo_u_alta = QtWidgets.QCheckBox("Activo")

        form_laborales_u.addRow("Número Económico:", self.input_numero_economico_u_alta)
        form_laborales_u.addRow("Rol:", self.combo_rol_u_alta)
        form_laborales_u.addRow("Contraseña:", self.input_password_u_alta)
        form_laborales_u.addRow("", self.check_activo_u_alta)

        btn_layout_alta_u = QtWidgets.QHBoxLayout()
        btn_layout_alta_u.addStretch()
        self.btn_guardar_u_alta = QtWidgets.QPushButton("Dar de Alta Usuario")
        self.btn_cancelar_u_alta = QtWidgets.QPushButton("Cancelar")
        btn_layout_alta_u.addWidget(self.btn_guardar_u_alta)
        btn_layout_alta_u.addWidget(self.btn_cancelar_u_alta)

        alta_u_layout.addWidget(group_datos_personales_u)
        alta_u_layout.addWidget(group_datos_laborales_u)
        alta_u_layout.addLayout(btn_layout_alta_u)
        self.stack_usuarios.addWidget(self.page_alta_usuario)

        # ===============================
        # 🚀 Baja de Usuario
        # ===============================
        self.page_baja_usuario = QtWidgets.QWidget()
        baja_u_layout = QtWidgets.QVBoxLayout(self.page_baja_usuario)

        group_baja_u = QtWidgets.QGroupBox("Dar de Baja Usuario")
        group_baja_layout = QtWidgets.QFormLayout(group_baja_u)

        self.input_buscar_baja_u = QtWidgets.QLineEdit()
        self.input_buscar_baja_u.setPlaceholderText("Ingrese usuario o No. Económico")
        self.combo_resultado_baja_u = QtWidgets.QComboBox()

        group_baja_layout.addRow("Buscar:", self.input_buscar_baja_u)
        group_baja_layout.addRow("Resultados:", self.combo_resultado_baja_u)

        self.btn_dar_baja_u = QtWidgets.QPushButton("Dar de Baja Usuario")

        baja_u_layout.addWidget(group_baja_u)
        baja_u_layout.addWidget(self.btn_dar_baja_u)
        baja_u_layout.addStretch()

        # Labels para mostrar los datos del usuario
        self.label_nombre_baja_u = QtWidgets.QLabel("")
        self.label_rol_baja_u = QtWidgets.QLabel("")
        self.label_correo_baja_u = QtWidgets.QLabel("")
        self.label_activo_baja_u = QtWidgets.QLabel("")

        group_baja_layout.addRow("Nombre completo:", self.label_nombre_baja_u)
        group_baja_layout.addRow("Rol:", self.label_rol_baja_u)
        group_baja_layout.addRow("Correo:", self.label_correo_baja_u)
        group_baja_layout.addRow("Activo:", self.label_activo_baja_u)

        self.stack_usuarios.addWidget(self.page_baja_usuario)

        # ===============================
        # 🚀 Cambiar Roles
        # ===============================
        self.page_cambiar_roles = QtWidgets.QWidget()
        layout_cambiar_roles = QtWidgets.QVBoxLayout(self.page_cambiar_roles)

        group_buscar_roles = QtWidgets.QGroupBox("Buscar Usuario")
        layout_buscar_roles = QtWidgets.QFormLayout(group_buscar_roles)
        self.input_buscar_roles = QtWidgets.QLineEdit()
        self.input_buscar_roles.setPlaceholderText("Ingrese usuario o No. Económico")
        self.combo_resultado_roles = QtWidgets.QComboBox()

        layout_buscar_roles.addRow("Buscar:", self.input_buscar_roles)
        layout_buscar_roles.addRow("Resultados:", self.combo_resultado_roles)

        group_asignar_rol = QtWidgets.QGroupBox("Asignar Nuevo Rol")
        layout_asignar_rol = QtWidgets.QFormLayout(group_asignar_rol)
        self.combo_nuevo_rol = QtWidgets.QComboBox()
        self.combo_nuevo_rol.addItem("Maestro", "PROFESOR")
        self.combo_nuevo_rol.addItem("Administrativo", "ADMINISTRATIVO")
        self.combo_nuevo_rol.addItem("Directivo", "DIRECTIVO")
        self.btn_guardar_rol = QtWidgets.QPushButton("Guardar Cambios")

        layout_asignar_rol.addRow("Rol:", self.combo_nuevo_rol)

        layout_cambiar_roles.addWidget(group_buscar_roles)
        layout_cambiar_roles.addWidget(group_asignar_rol)
        layout_cambiar_roles.addWidget(self.btn_guardar_rol)
        layout_cambiar_roles.addStretch()
        self.label_nombre_rol_actual = QtWidgets.QLabel("")
        self.label_email_rol_actual = QtWidgets.QLabel("")
        self.label_rol_actual = QtWidgets.QLabel("")
        self.label_activo_rol_actual = QtWidgets.QLabel("")

        layout_asignar_rol.addRow("Nombre completo:", self.label_nombre_rol_actual)
        layout_asignar_rol.addRow("Correo:", self.label_email_rol_actual)
        layout_asignar_rol.addRow("Rol actual:", self.label_rol_actual)
        layout_asignar_rol.addRow("Activo:", self.label_activo_rol_actual)

        self.stack_usuarios.addWidget(self.page_cambiar_roles)

        # ===============================
        # 🚀 Asignar / Cambiar Contraseña
        # ===============================
        self.page_cambiar_password = QtWidgets.QWidget()
        layout_cambiar_pass = QtWidgets.QVBoxLayout(self.page_cambiar_password)

        titulo_pass = QtWidgets.QLabel("Asignar / Cambiar Contraseña")
        font_pass = QtGui.QFont()
        font_pass.setPointSize(18)
        font_pass.setBold(True)
        titulo_pass.setFont(font_pass)
        titulo_pass.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_cambiar_pass.addWidget(titulo_pass)

        form_pass = QtWidgets.QFormLayout()
        self.input_usuario_pass = QtWidgets.QLineEdit()
        self.input_usuario_pass.setPlaceholderText("Usuario o No. Económico")

        self.input_pass_nueva = QtWidgets.QLineEdit()
        self.input_pass_nueva.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input_pass_nueva.setPlaceholderText("Nueva Contraseña")

        self.input_pass_confirmar = QtWidgets.QLineEdit()
        self.input_pass_confirmar.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input_pass_confirmar.setPlaceholderText("Confirmar Nueva Contraseña")

        form_pass.addRow("Usuario:", self.input_usuario_pass)
        form_pass.addRow("Nueva Contraseña:", self.input_pass_nueva)
        form_pass.addRow("Confirmar Nueva:", self.input_pass_confirmar)

        layout_cambiar_pass.addLayout(form_pass)

        btn_layout_pass = QtWidgets.QHBoxLayout()
        btn_layout_pass.addStretch()
        self.btn_guardar_password = QtWidgets.QPushButton("Guardar")
        self.btn_cancelar_password = QtWidgets.QPushButton("Cancelar")
        btn_layout_pass.addWidget(self.btn_guardar_password)
        btn_layout_pass.addWidget(self.btn_cancelar_password)

        layout_cambiar_pass.addLayout(btn_layout_pass)

        self.stack_usuarios.addWidget(self.page_cambiar_password)

        # ✅ Agregar página completa al stacked principal
        self.contendor_contenido.addWidget(self.pagina_usuarios)

        ########## fin pagina usuarios ##########

        ########## pagina usuarios ###########

        ########## fin pagina usuarios ##########
        ########## pagina periodos ##########
        # ===============================
        # 📌 Bloque de Periodos
        # ===============================
        self.pagina_periodos = QtWidgets.QWidget()
        self.pagina_periodos.setObjectName("pagina_periodos")
        self.layout_periodos = QtWidgets.QVBoxLayout(self.pagina_periodos)

        # === QToolBar de Periodos ===
        self.toolbar_periodos = QtWidgets.QToolBar()
        self.toolbar_periodos.setMovable(False)
        self.layout_periodos.addWidget(self.toolbar_periodos)

        # === Grupo de acciones exclusivas ===
        self.grupo_acciones_periodos = QtGui.QActionGroup(MainWindow)
        self.grupo_acciones_periodos.setExclusive(True)

        # === Acciones ===
        self.action_crear_periodo = QtGui.QAction("Crear Periodo", MainWindow)
        self.action_activar_periodo = QtGui.QAction("Activar Periodo", MainWindow)
        self.action_marcar_vacaciones = QtGui.QAction("Marcar Vacaciones", MainWindow)

        # ✅ Hacerlas checkables y añadir al grupo
        for act in [
            self.action_crear_periodo,
            self.action_activar_periodo,
            self.action_marcar_vacaciones,
        ]:
            act.setCheckable(True)
            self.grupo_acciones_periodos.addAction(act)

        # ✅ Añadir acciones a la toolbar
        self.toolbar_periodos.addAction(self.action_crear_periodo)
        self.toolbar_periodos.addAction(self.action_activar_periodo)
        self.toolbar_periodos.addAction(self.action_marcar_vacaciones)

        # === Stacked interno para Periodos ===
        self.stack_periodos = QtWidgets.QStackedWidget()
        self.layout_periodos.addWidget(self.stack_periodos)

        # ===============================
        # 🚀 Crear Periodo
        # ===============================
        self.page_crear_periodo = QtWidgets.QWidget()
        crear_layout = QtWidgets.QVBoxLayout(self.page_crear_periodo)

        group_crear = QtWidgets.QGroupBox("Datos del Periodo")
        form_crear = QtWidgets.QFormLayout(group_crear)

        self.input_nombre_periodo = QtWidgets.QLineEdit()
        self.input_fecha_inicio = QtWidgets.QDateEdit()
        self.input_fecha_inicio.setCalendarPopup(True)
        self.input_fecha_inicio.setDisplayFormat("dd/MM/yyyy")
        self.input_fecha_fin = QtWidgets.QDateEdit()
        self.input_fecha_fin.setCalendarPopup(True)
        self.input_fecha_fin.setDisplayFormat("dd/MM/yyyy")

        form_crear.addRow("Nombre del Periodo:", self.input_nombre_periodo)
        form_crear.addRow("Fecha de Inicio:", self.input_fecha_inicio)
        form_crear.addRow("Fecha de Fin:", self.input_fecha_fin)

        btn_crear_layout = QtWidgets.QHBoxLayout()
        btn_crear_layout.addStretch()
        self.btn_guardar_periodo = QtWidgets.QPushButton("Crear Periodo")
        btn_crear_layout.addWidget(self.btn_guardar_periodo)

        crear_layout.addWidget(group_crear)
        crear_layout.addLayout(btn_crear_layout)
        self.stack_periodos.addWidget(self.page_crear_periodo)
        # ===============================
        # 🚀 Activar Periodo (Compacto arriba)
        # ===============================
        self.page_activar_periodo = QtWidgets.QWidget()
        activar_layout = QtWidgets.QVBoxLayout(self.page_activar_periodo)
        activar_layout.setContentsMargins(30, 10, 30, 10)
        activar_layout.setSpacing(10)

        # === Caja de Activar Periodo ===
        group_activar = QtWidgets.QGroupBox("Activar un Periodo")
        group_activar.setMinimumHeight(150)

        form_layout = QtWidgets.QFormLayout(group_activar)
        form_layout.setContentsMargins(20, 15, 20, 15)
        form_layout.setSpacing(15)

        # === ComboBox ===
        self.combo_periodos_disponibles = QtWidgets.QComboBox()
        self.combo_periodos_disponibles.setMinimumHeight(35)

        # === Botón Activar ===
        self.btn_activar_periodo = QtWidgets.QPushButton("Activar")
        self.btn_activar_periodo.setMinimumHeight(35)
        self.btn_activar_periodo.setStyleSheet("font-weight: bold;")

        # === Agregar elementos ===
        form_layout.addRow("Seleccionar Periodo:", self.combo_periodos_disponibles)
        form_layout.addRow("", self.btn_activar_periodo)

        activar_layout.addWidget(
            group_activar, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.stack_periodos.addWidget(self.page_activar_periodo)

        # ===============================
        # 🚀 Marcar Vacaciones
        # ===============================
        self.page_marcar_vacaciones = QtWidgets.QWidget()
        vacaciones_layout = QtWidgets.QVBoxLayout(self.page_marcar_vacaciones)

        group_vacaciones = QtWidgets.QGroupBox("Marcar Vacaciones")
        form_vacaciones = QtWidgets.QFormLayout(group_vacaciones)

        self.input_fecha_inicio_vac = QtWidgets.QDateEdit()
        self.input_fecha_inicio_vac.setCalendarPopup(True)
        self.input_fecha_inicio_vac.setDisplayFormat("dd/MM/yyyy")
        self.input_fecha_fin_vac = QtWidgets.QDateEdit()
        self.input_fecha_fin_vac.setCalendarPopup(True)
        self.input_fecha_fin_vac.setDisplayFormat("dd/MM/yyyy")

        form_vacaciones.addRow("Fecha de Inicio:", self.input_fecha_inicio_vac)
        form_vacaciones.addRow("Fecha de Fin:", self.input_fecha_fin_vac)

        btn_vacaciones_layout = QtWidgets.QHBoxLayout()
        btn_vacaciones_layout.addStretch()
        self.btn_guardar_vacaciones = QtWidgets.QPushButton("Marcar Vacaciones")
        btn_vacaciones_layout.addWidget(self.btn_guardar_vacaciones)

        vacaciones_layout.addWidget(group_vacaciones)
        vacaciones_layout.addLayout(btn_vacaciones_layout)
        self.stack_periodos.addWidget(self.page_marcar_vacaciones)

        # ✅ Añadir la página de periodos al stacked principal
        self.contendor_contenido.addWidget(self.pagina_periodos)

        ########## fin pagina periodos ##########
        ########### pagina materias y horarios ##########
        ########### pagina materias y horarios ##########
        # ===============================
        # 📌 Página Materias y Horarios
        # ===============================
        self.pagina_materias_horarios = QtWidgets.QWidget()
        self.layout_materias_horarios = QtWidgets.QVBoxLayout(
            self.pagina_materias_horarios
        )

        # === QToolBar ===
        self.toolbar_materias = QtWidgets.QToolBar()
        self.toolbar_materias.setMovable(False)
        self.layout_materias_horarios.addWidget(self.toolbar_materias)

        self.action_alta_materia = QtGui.QAction("Alta Materia", MainWindow)
        self.action_alta_materia.setCheckable(True)

        self.action_lista_materias = QtGui.QAction("Lista de Materias", MainWindow)
        self.action_lista_materias.setCheckable(True)

        self.action_editar_materia = QtGui.QAction("Editar Materia", MainWindow)
        self.action_editar_materia.setCheckable(True)

        self.action_asignar_horarios = QtGui.QAction("Asignar Horarios", MainWindow)
        self.action_asignar_horarios.setCheckable(True)

        self.action_salones = QtGui.QAction("Salones", MainWindow)
        self.action_salones.setCheckable(True)

        self.toolbar_materias.addAction(self.action_alta_materia)
        self.toolbar_materias.addAction(self.action_lista_materias)
        self.toolbar_materias.addAction(self.action_editar_materia)
        self.toolbar_materias.addAction(self.action_asignar_horarios)
        self.toolbar_materias.addAction(self.action_salones)

        # === Agrupar acciones para exclusividad ===
        self.group_materias = QtGui.QActionGroup(MainWindow)
        self.group_materias.setExclusive(True)
        self.group_materias.addAction(self.action_alta_materia)
        self.group_materias.addAction(self.action_lista_materias)
        self.group_materias.addAction(self.action_editar_materia)
        self.group_materias.addAction(self.action_asignar_horarios)
        self.group_materias.addAction(self.action_salones)

        # === Stacked interno ===
        self.stack_materias = QtWidgets.QStackedWidget()
        self.layout_materias_horarios.addWidget(self.stack_materias)

        # ===============================
        # 🚀 Alta de Materia
        # ===============================
        self.page_alta_materia = QtWidgets.QWidget()
        alta_layout = QtWidgets.QVBoxLayout(self.page_alta_materia)

        group_datos_materia = QtWidgets.QGroupBox("Datos de la Materia")
        form_materia = QtWidgets.QFormLayout(group_datos_materia)

        self.input_nombre_materia = QtWidgets.QLineEdit()
        self.input_clave_materia = QtWidgets.QLineEdit()
        self.spin_creditos_materia = QtWidgets.QSpinBox()
        self.spin_creditos_materia.setRange(1, 20)
        self.spin_cupo_materia = QtWidgets.QSpinBox()
        self.spin_cupo_materia.setRange(1, 100)

        form_materia.addRow("Nombre de la Materia:", self.input_nombre_materia)
        form_materia.addRow("Clave:", self.input_clave_materia)
        form_materia.addRow("Créditos:", self.spin_creditos_materia)
        form_materia.addRow("Cupo Máximo:", self.spin_cupo_materia)

        # === Sección para Asignar Profesor ===
        group_profesor = QtWidgets.QGroupBox("Asignar Profesor")
        form_profesor = QtWidgets.QFormLayout(group_profesor)

        self.input_buscar_profesor = QtWidgets.QLineEdit()
        self.input_buscar_profesor.setPlaceholderText("Ingrese nombre o No. Económico")
        self.btn_buscar_profesor = QtWidgets.QPushButton("Buscar")
        self.combo_profesor = QtWidgets.QComboBox()

        form_profesor.addRow("Buscar Profesor:", self.input_buscar_profesor)
        form_profesor.addRow("", self.btn_buscar_profesor)
        form_profesor.addRow("Seleccionar:", self.combo_profesor)

        # === Botones ===
        btn_layout_alta = QtWidgets.QHBoxLayout()
        self.btn_guardar_materia = QtWidgets.QPushButton("Guardar Materia")
        self.btn_cancelar_materia = QtWidgets.QPushButton("Cancelar")
        btn_layout_alta.addStretch()
        btn_layout_alta.addWidget(self.btn_guardar_materia)
        btn_layout_alta.addWidget(self.btn_cancelar_materia)

        alta_layout.addWidget(group_datos_materia)
        alta_layout.addWidget(group_profesor)
        alta_layout.addLayout(btn_layout_alta)
        self.stack_materias.addWidget(self.page_alta_materia)

        # ===============================
        # 🚀 Lista de Materias
        # ===============================
        self.page_lista_materias = QtWidgets.QWidget()
        lista_layout = QtWidgets.QVBoxLayout(self.page_lista_materias)

        self.input_buscar_lista_materias = QtWidgets.QLineEdit()
        self.input_buscar_lista_materias.setPlaceholderText(
            "Buscar materia por nombre o clave"
        )
        self.tabla_materias = QtWidgets.QTableWidget()
        self.tabla_materias.setColumnCount(4)
        self.tabla_materias.setHorizontalHeaderLabels(
            ["Clave", "Nombre", "Profesor", "Cupo"]
        )
        self.tabla_materias.horizontalHeader().setStretchLastSection(True)

        lista_layout.addWidget(QtWidgets.QLabel("Listado de Materias"))
        lista_layout.addWidget(self.input_buscar_lista_materias)
        lista_layout.addWidget(self.tabla_materias)
        self.stack_materias.addWidget(self.page_lista_materias)

        # ===============================
        # 🚀 Editar Materias
        # ===============================
        self.page_editar_materia = QtWidgets.QWidget()
        editar_layout = QtWidgets.QVBoxLayout(self.page_editar_materia)

        group_buscar_editar = QtWidgets.QGroupBox("Buscar Materia")
        form_buscar_editar = QtWidgets.QFormLayout(group_buscar_editar)

        self.input_buscar_editar = QtWidgets.QLineEdit()
        self.input_buscar_editar.setPlaceholderText("Ingrese nombre o clave de materia")
        self.btn_buscar_editar = QtWidgets.QPushButton("Buscar")
        self.combo_editar_materia = QtWidgets.QComboBox()

        form_buscar_editar.addRow("Buscar:", self.input_buscar_editar)
        form_buscar_editar.addRow("", self.btn_buscar_editar)
        form_buscar_editar.addRow("Seleccionar:", self.combo_editar_materia)

        group_datos_editar = QtWidgets.QGroupBox("Editar Datos de la Materia")
        form_datos_editar = QtWidgets.QFormLayout(group_datos_editar)

        self.input_nombre_editar = QtWidgets.QLineEdit()
        self.input_clave_editar = QtWidgets.QLineEdit()
        self.spin_creditos_editar = QtWidgets.QSpinBox()
        self.spin_creditos_editar.setRange(1, 20)
        self.spin_cupo_editar = QtWidgets.QSpinBox()
        self.spin_cupo_editar.setRange(1, 100)

        form_datos_editar.addRow("Nombre:", self.input_nombre_editar)
        form_datos_editar.addRow("Clave:", self.input_clave_editar)
        form_datos_editar.addRow("Créditos:", self.spin_creditos_editar)
        form_datos_editar.addRow("Cupo:", self.spin_cupo_editar)

        # === Sección para editar Profesor asignado ===
        group_profesor_editar = QtWidgets.QGroupBox("Editar Profesor Asignado")
        form_profesor_editar = QtWidgets.QFormLayout(group_profesor_editar)

        self.input_buscar_profesor_editar = QtWidgets.QLineEdit()
        self.input_buscar_profesor_editar.setPlaceholderText(
            "Ingrese nombre o No. Económico"
        )
        self.btn_buscar_profesor_editar = QtWidgets.QPushButton("Buscar")
        self.combo_profesor_editar = QtWidgets.QComboBox()

        form_profesor_editar.addRow(
            "Buscar Profesor:", self.input_buscar_profesor_editar
        )
        form_profesor_editar.addRow("", self.btn_buscar_profesor_editar)
        form_profesor_editar.addRow("Seleccionar:", self.combo_profesor_editar)

        btn_layout_editar = QtWidgets.QHBoxLayout()
        self.btn_guardar_cambios_materia = QtWidgets.QPushButton("Guardar Cambios")
        self.btn_cancelar_editar_materia = QtWidgets.QPushButton("Cancelar")
        btn_layout_editar.addStretch()
        btn_layout_editar.addWidget(self.btn_guardar_cambios_materia)
        btn_layout_editar.addWidget(self.btn_cancelar_editar_materia)

        editar_layout.addWidget(group_buscar_editar)
        editar_layout.addWidget(group_datos_editar)
        editar_layout.addWidget(group_profesor_editar)
        editar_layout.addLayout(btn_layout_editar)
        self.stack_materias.addWidget(self.page_editar_materia)

        # ===============================
        # 🚀 Asignar Horarios
        # ===============================
        self.page_asignar_horarios = QtWidgets.QWidget()
        horarios_layout = QtWidgets.QVBoxLayout(self.page_asignar_horarios)

        group_horario = QtWidgets.QGroupBox("Asignar Horario")
        form_horario = QtWidgets.QFormLayout(group_horario)

        self.combo_materia_horario = QtWidgets.QComboBox()
        self.combo_dia_semana = QtWidgets.QComboBox()
        self.combo_dia_semana.addItems(
            ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        )
        self.time_inicio = QtWidgets.QTimeEdit()
        self.time_fin = QtWidgets.QTimeEdit()

        form_horario.addRow("Materia:", self.combo_materia_horario)
        form_horario.addRow("Día de la Semana:", self.combo_dia_semana)
        form_horario.addRow("Hora Inicio:", self.time_inicio)
        form_horario.addRow("Hora Fin:", self.time_fin)

        btn_layout_horarios = QtWidgets.QHBoxLayout()
        self.btn_guardar_horario = QtWidgets.QPushButton("Asignar Horario")
        btn_layout_horarios.addStretch()
        btn_layout_horarios.addWidget(self.btn_guardar_horario)

        horarios_layout.addWidget(group_horario)
        horarios_layout.addLayout(btn_layout_horarios)
        self.stack_materias.addWidget(self.page_asignar_horarios)

        # ===============================
        # 🚀 Salones (Crear y Asignar)
        # ===============================
        self.page_salones = QtWidgets.QWidget()
        salones_layout = QtWidgets.QVBoxLayout(self.page_salones)

        # === Grupo para CREAR Salón ===
        group_crear_salon = QtWidgets.QGroupBox("Crear Nuevo Salón")
        form_crear_salon = QtWidgets.QFormLayout(group_crear_salon)

        self.input_numero_salon_nuevo = QtWidgets.QLineEdit()
        self.input_capacidad_salon_nuevo = QtWidgets.QSpinBox()
        self.input_capacidad_salon_nuevo.setRange(1, 120)

        form_crear_salon.addRow("Número de Salón:", self.input_numero_salon_nuevo)
        form_crear_salon.addRow("Capacidad:", self.input_capacidad_salon_nuevo)

        btn_layout_crear = QtWidgets.QHBoxLayout()
        self.btn_guardar_nuevo_salon = QtWidgets.QPushButton("Guardar Salón")
        self.btn_cancelar_nuevo_salon = QtWidgets.QPushButton("Cancelar")
        btn_layout_crear.addStretch()
        btn_layout_crear.addWidget(self.btn_guardar_nuevo_salon)
        btn_layout_crear.addWidget(self.btn_cancelar_nuevo_salon)

        # === Grupo para ASIGNAR Salón ===
        group_asignar_salon = QtWidgets.QGroupBox("Asignar Salón")
        form_asignar_salon = QtWidgets.QFormLayout(group_asignar_salon)

        # 🔍 Buscar Materia
        self.input_buscar_materia_salon = QtWidgets.QLineEdit()
        self.input_buscar_materia_salon.setPlaceholderText(
            "Buscar materia por nombre o clave"
        )
        self.btn_buscar_materia_salon = QtWidgets.QPushButton("Buscar")
        self.combo_materia_salon = QtWidgets.QComboBox()

        form_asignar_salon.addRow("Buscar Materia:", self.input_buscar_materia_salon)
        form_asignar_salon.addRow("", self.btn_buscar_materia_salon)
        form_asignar_salon.addRow("Seleccionar Materia:", self.combo_materia_salon)

        # 🔍 Buscar Salón
        self.input_buscar_salon = QtWidgets.QLineEdit()
        self.input_buscar_salon.setPlaceholderText("Buscar salón por número o nombre")
        self.btn_buscar_salon = QtWidgets.QPushButton("Buscar")
        self.combo_salon = QtWidgets.QComboBox()

        form_asignar_salon.addRow("Buscar Salón:", self.input_buscar_salon)
        form_asignar_salon.addRow("", self.btn_buscar_salon)
        form_asignar_salon.addRow("Seleccionar Salón:", self.combo_salon)

        btn_layout_asignar = QtWidgets.QHBoxLayout()
        self.btn_guardar_asignacion_salon = QtWidgets.QPushButton("Asignar Salón")
        self.btn_cancelar_asignacion_salon = QtWidgets.QPushButton("Cancelar")
        btn_layout_asignar.addStretch()
        btn_layout_asignar.addWidget(self.btn_guardar_asignacion_salon)
        btn_layout_asignar.addWidget(self.btn_cancelar_asignacion_salon)

        # === Añadir todo al layout principal ===
        salones_layout.addWidget(group_crear_salon)
        salones_layout.addLayout(btn_layout_crear)
        salones_layout.addWidget(group_asignar_salon)
        salones_layout.addLayout(btn_layout_asignar)

        self.stack_materias.addWidget(self.page_salones)

        # ✅ Agregar la página al Stacked principal
        self.contendor_contenido.addWidget(self.pagina_materias_horarios)

        ########### fin pagina materias y horarios ##########
        ########### pagina reportes globales ##########
        # ===============================
        # 📌 Página Reportes Globales
        # ===============================
        self.pagina_reportes_globales = QtWidgets.QWidget()
        self.layout_reportes = QtWidgets.QVBoxLayout(self.pagina_reportes_globales)

        # === QToolBar ===
        self.toolbar_reportes = QtWidgets.QToolBar()
        self.toolbar_reportes.setMovable(False)
        self.layout_reportes.addWidget(self.toolbar_reportes)

        self.action_alumnos_periodo = QtGui.QAction("Alumnos por Periodo", MainWindow)
        self.action_alumnos_periodo.setCheckable(True)

        self.action_maestros_periodo = QtGui.QAction("Maestros y Materias", MainWindow)
        self.action_maestros_periodo.setCheckable(True)

        self.action_materias_periodo = QtGui.QAction("Materias por Periodo", MainWindow)
        self.action_materias_periodo.setCheckable(True)

        self.action_reporte_usuarios = QtGui.QAction("Reporte de Usuarios", MainWindow)
        self.action_reporte_usuarios.setCheckable(True)

        self.toolbar_reportes.addAction(self.action_alumnos_periodo)
        self.toolbar_reportes.addAction(self.action_maestros_periodo)
        self.toolbar_reportes.addAction(self.action_materias_periodo)
        self.toolbar_reportes.addAction(self.action_reporte_usuarios)

        # === Agrupar acciones ===
        self.group_reportes = QtGui.QActionGroup(MainWindow)
        self.group_reportes.setExclusive(True)
        self.group_reportes.addAction(self.action_alumnos_periodo)
        self.group_reportes.addAction(self.action_maestros_periodo)
        self.group_reportes.addAction(self.action_materias_periodo)
        self.group_reportes.addAction(self.action_reporte_usuarios)

        # === Stacked interno ===
        self.stack_reportes = QtWidgets.QStackedWidget()
        self.layout_reportes.addWidget(self.stack_reportes)

        # ===============================
        # 🚀 Alumnos por Periodo
        # ===============================
        self.page_alumnos_periodo = QtWidgets.QWidget()
        alumnos_layout = QtWidgets.QVBoxLayout(self.page_alumnos_periodo)

        group_alumnos_periodo = QtWidgets.QGroupBox(
            "Generar Reporte de Alumnos por Periodo"
        )
        form_alumnos = QtWidgets.QFormLayout(group_alumnos_periodo)

        self.combo_periodo_alumnos = QtWidgets.QComboBox()
        self.combo_periodo_alumnos.addItems(["2025-A", "2025-B", "2026-A"])  # ejemplo

        self.btn_generar_alumnos_periodo = QtWidgets.QPushButton("Generar Reporte")

        form_alumnos.addRow("Periodo:", self.combo_periodo_alumnos)
        form_alumnos.addRow("", self.btn_generar_alumnos_periodo)

        self.tabla_alumnos_periodo = QtWidgets.QTableWidget()
        self.tabla_alumnos_periodo.setColumnCount(4)
        self.tabla_alumnos_periodo.setHorizontalHeaderLabels(
            ["Matrícula", "Nombre", "Apellido", "Carrera"]
        )
        self.tabla_alumnos_periodo.horizontalHeader().setStretchLastSection(True)

        alumnos_layout.addWidget(group_alumnos_periodo)
        alumnos_layout.addWidget(self.tabla_alumnos_periodo)
        self.stack_reportes.addWidget(self.page_alumnos_periodo)

        # ===============================
        # 🚀 Maestros por Periodo con Materias
        # ===============================
        self.page_maestros_periodo = QtWidgets.QWidget()
        maestros_layout = QtWidgets.QVBoxLayout(self.page_maestros_periodo)

        group_maestros_periodo = QtWidgets.QGroupBox(
            "Generar Reporte de Maestros y Materias por Periodo"
        )
        form_maestros = QtWidgets.QFormLayout(group_maestros_periodo)

        self.combo_periodo_maestros = QtWidgets.QComboBox()
        self.combo_periodo_maestros.addItems(["2025-A", "2025-B", "2026-A"])

        self.btn_generar_maestros_periodo = QtWidgets.QPushButton("Generar Reporte")

        form_maestros.addRow("Periodo:", self.combo_periodo_maestros)
        form_maestros.addRow("", self.btn_generar_maestros_periodo)

        self.tabla_maestros_periodo = QtWidgets.QTableWidget()
        self.tabla_maestros_periodo.setColumnCount(3)
        self.tabla_maestros_periodo.setHorizontalHeaderLabels(
            ["No. Económico", "Nombre Maestro", "Materias Asignadas"]
        )
        self.tabla_maestros_periodo.horizontalHeader().setStretchLastSection(True)

        maestros_layout.addWidget(group_maestros_periodo)
        maestros_layout.addWidget(self.tabla_maestros_periodo)
        self.stack_reportes.addWidget(self.page_maestros_periodo)

        # ===============================
        # 🚀 Materias por Periodo
        # ===============================
        self.page_materias_periodo = QtWidgets.QWidget()
        materias_layout = QtWidgets.QVBoxLayout(self.page_materias_periodo)

        group_materias_periodo = QtWidgets.QGroupBox(
            "Generar Reporte de Materias por Periodo"
        )
        form_materias = QtWidgets.QFormLayout(group_materias_periodo)

        self.combo_periodo_materias = QtWidgets.QComboBox()
        self.combo_periodo_materias.addItems(["2025-A", "2025-B", "2026-A"])

        self.btn_generar_materias_periodo = QtWidgets.QPushButton("Generar Reporte")

        form_materias.addRow("Periodo:", self.combo_periodo_materias)
        form_materias.addRow("", self.btn_generar_materias_periodo)

        self.tabla_materias_periodo = QtWidgets.QTableWidget()
        self.tabla_materias_periodo.setColumnCount(4)
        self.tabla_materias_periodo.setHorizontalHeaderLabels(
            ["Clave", "Materia", "Profesor", "Cupo"]
        )
        self.tabla_materias_periodo.horizontalHeader().setStretchLastSection(True)

        materias_layout.addWidget(group_materias_periodo)
        materias_layout.addWidget(self.tabla_materias_periodo)
        self.stack_reportes.addWidget(self.page_materias_periodo)

        # 🚀 Reporte de Usuarios
        self.page_reporte_usuarios = QtWidgets.QWidget()
        layout_reporte_usuarios = QtWidgets.QVBoxLayout(self.page_reporte_usuarios)

        # === Tabla ===
        self.tabla_reporte_usuarios = QtWidgets.QTableWidget()
        self.tabla_reporte_usuarios.setColumnCount(5)
        self.tabla_reporte_usuarios.setHorizontalHeaderLabels(
            ["No. Económico", "Nombre", "Apellido Paterno", "Apellido Materno", "Rol"]
        )

        # ✅ Ajuste dinámico de columnas (Opción 2)
        header = self.tabla_reporte_usuarios.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        # === Botón para generar reporte ===
        btn_layout_usuarios = QtWidgets.QHBoxLayout()
        self.btn_generar_reporte_usuarios = QtWidgets.QPushButton("Generar Reporte")
        btn_layout_usuarios.addStretch()
        btn_layout_usuarios.addWidget(self.btn_generar_reporte_usuarios)

        # === Añadir widgets al layout ===
        layout_reporte_usuarios.addWidget(self.tabla_reporte_usuarios)
        layout_reporte_usuarios.addLayout(btn_layout_usuarios)

        self.stack_reportes.addWidget(self.page_reporte_usuarios)

        # ✅ Agregar la página al Stacked principal
        self.contendor_contenido.addWidget(self.pagina_reportes_globales)

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
        ######### inicio perfil ###########
        ########## Página Perfil ##########
        # === Página Perfil ===
        self.pagina_perfil = QtWidgets.QWidget()
        self.pagina_perfil.setObjectName("pagina_perfil")
        self.layout_perfil = QtWidgets.QVBoxLayout(self.pagina_perfil)

        # === Título ===
        self.label_titulo_perfil = QtWidgets.QLabel("Perfil del Directivo")
        font_perfil = QtGui.QFont()
        font_perfil.setPointSize(22)
        font_perfil.setBold(True)
        self.label_titulo_perfil.setFont(font_perfil)
        self.label_titulo_perfil.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_perfil.addWidget(self.label_titulo_perfil)

        # === Contenedor de datos con tarjeta ===
        perfil_card = QtWidgets.QGroupBox("Información Personal")
        perfil_layout = QtWidgets.QFormLayout(perfil_card)
        perfil_layout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        # Campos de perfil
        self.input_correo = QtWidgets.QLineEdit()
        self.input_correo.setPlaceholderText("Correo electrónico")

        self.input_direccion = QtWidgets.QLineEdit()
        self.input_direccion.setPlaceholderText("Dirección")

        self.input_telefono = QtWidgets.QLineEdit()
        self.input_telefono.setPlaceholderText("Teléfono")

        self.input_password = QtWidgets.QLineEdit()
        self.input_password.setPlaceholderText("Contraseña")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Agregar campos al formulario
        perfil_layout.addRow("Correo:", self.input_correo)
        perfil_layout.addRow("Dirección:", self.input_direccion)
        perfil_layout.addRow("Teléfono:", self.input_telefono)
        perfil_layout.addRow("Contraseña:", self.input_password)

        # === Botones de acción ===
        btn_layout_perfil = QtWidgets.QHBoxLayout()
        btn_layout_perfil.addStretch()
        self.btn_guardar_perfil = QtWidgets.QPushButton("Guardar Cambios")
        self.btn_cancelar_perfil = QtWidgets.QPushButton("Cancelar")
        btn_layout_perfil.addWidget(self.btn_guardar_perfil)
        btn_layout_perfil.addWidget(self.btn_cancelar_perfil)

        # === Añadir todo al layout principal ===
        self.layout_perfil.addWidget(perfil_card)
        self.layout_perfil.addLayout(btn_layout_perfil)

        # ✅ Agregar al QStacked principal
        self.contendor_contenido.addWidget(self.pagina_perfil)
        ########## Fin Página Perfil ##########

        ######### fin perfil ###########
        self.verticalLayout_7.addWidget(self.contendor_contenido)
        self.gridLayout.addWidget(self.contenedor_secundario, 0, 2, 1, 1)
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
        self.btn_inicio.setIcon(icon)
        self.btn_inicio.setIconSize(QtCore.QSize(26, 26))
        self.btn_inicio.setCheckable(True)
        self.btn_inicio.setAutoExclusive(True)
        self.btn_inicio.setObjectName("btn_inicio")
        self.verticalLayout.addWidget(self.btn_inicio)
        self.btn_usuarios = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_usuarios.setText("")
        self.btn_usuarios.setIcon(icon1)
        self.btn_usuarios.setIconSize(QtCore.QSize(26, 26))
        self.btn_usuarios.setCheckable(True)
        self.btn_usuarios.setAutoExclusive(True)
        self.btn_usuarios.setObjectName("btn_usuarios")
        self.verticalLayout.addWidget(self.btn_usuarios)
        self.btn_periodos = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_periodos.setText("")
        self.btn_periodos.setIcon(icon2)
        self.btn_periodos.setIconSize(QtCore.QSize(26, 26))
        self.btn_periodos.setCheckable(True)
        self.btn_periodos.setAutoExclusive(True)
        self.btn_periodos.setObjectName("btn_periodos")
        self.verticalLayout.addWidget(self.btn_periodos)
        self.btn_materias_horarios = QtWidgets.QPushButton(
            parent=self.contenedor_menu_iconos
        )
        self.btn_materias_horarios.setText("")
        self.btn_materias_horarios.setIcon(icon3)
        self.btn_materias_horarios.setIconSize(QtCore.QSize(26, 26))
        self.btn_materias_horarios.setCheckable(True)
        self.btn_materias_horarios.setAutoExclusive(True)
        self.btn_materias_horarios.setObjectName("btn_materias_horarios")
        self.verticalLayout.addWidget(self.btn_materias_horarios)
        self.btn_reportes_globales = QtWidgets.QPushButton(
            parent=self.contenedor_menu_iconos
        )
        self.btn_reportes_globales.setText("")
        self.btn_reportes_globales.setIcon(icon4)
        self.btn_reportes_globales.setIconSize(QtCore.QSize(26, 26))
        self.btn_reportes_globales.setCheckable(True)
        self.btn_reportes_globales.setAutoExclusive(True)
        self.btn_reportes_globales.setObjectName("btn_reportes_globales")
        self.verticalLayout.addWidget(self.btn_reportes_globales)
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
        self.btn_acercade.setIcon(icon5)
        self.btn_acercade.setIconSize(QtCore.QSize(26, 26))
        self.btn_acercade.setCheckable(True)
        self.btn_acercade.setAutoExclusive(True)
        self.btn_acercade.setObjectName("btn_acercade")
        self.verticalLayout_3.addWidget(self.btn_acercade)
        self.btn_logout = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_logout.setText("")
        self.btn_logout.setIcon(icon6)
        self.btn_logout.setIconSize(QtCore.QSize(26, 26))
        self.btn_logout.setCheckable(True)
        self.btn_logout.setAutoExclusive(True)
        self.btn_logout.setObjectName("btn_logout")
        self.verticalLayout_3.addWidget(self.btn_logout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.contenedor_menu_iconos, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.contenedo_principal)

        # ==============================
        # ✅ Función genérica para estilo activo
        # ==============================
        def aplicar_estilo_toolbar(toolbar, acciones):
            for action in acciones:
                widget = toolbar.widgetForAction(action)
                if action.isChecked():
                    widget.setStyleSheet(
                        "background-color: #b71c1c; color: white; border-radius: 6px;"
                    )
                else:
                    widget.setStyleSheet("")

        # ==============================
        # 📌 Sidebar Inicio
        # ==============================
        self.btn_inicio.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_bienvenida)
        )
        self.btn_inicio_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_bienvenida)
        )

        # ==============================
        # 📌 Usuarios
        # ==============================
        self.action_alta_usuario.triggered.connect(
            lambda: self.stack_usuarios.setCurrentWidget(self.page_alta_usuario)
        )
        self.action_baja_usuario.triggered.connect(
            lambda: self.stack_usuarios.setCurrentWidget(self.page_baja_usuario)
        )
        self.action_cambiar_roles.triggered.connect(
            lambda: self.stack_usuarios.setCurrentWidget(self.page_cambiar_roles)
        )
        self.action_cambiar_password.triggered.connect(
            lambda: self.stack_usuarios.setCurrentWidget(self.page_cambiar_password)
        )

        self.btn_usuarios.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_usuarios)
        )
        self.btn_usuarios_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_usuarios)
        )

        acciones_usuarios = [
            self.action_alta_usuario,
            self.action_baja_usuario,
            self.action_cambiar_roles,
            self.action_cambiar_password,
        ]

        for a in acciones_usuarios:
            a.triggered.connect(
                lambda checked, a=a: aplicar_estilo_toolbar(
                    self.toolbar_usuarios, acciones_usuarios
                )
            )

        # ✅ Al abrir la sección de Usuarios, por defecto mostrar "Alta Usuarios"
        self.btn_usuarios.clicked.connect(lambda: self.action_alta_usuario.trigger())
        self.btn_usuarios_texto.clicked.connect(
            lambda: self.action_alta_usuario.trigger()
        )

        # ==============================
        # 📌 Periodos
        # ==============================
        self.action_crear_periodo.triggered.connect(
            lambda: self.stack_periodos.setCurrentWidget(self.page_crear_periodo)
        )
        self.action_activar_periodo.triggered.connect(
            lambda: self.stack_periodos.setCurrentWidget(self.page_activar_periodo)
        )
        self.action_marcar_vacaciones.triggered.connect(
            lambda: self.stack_periodos.setCurrentWidget(self.page_marcar_vacaciones)
        )

        self.btn_periodos.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_periodos)
        )
        self.btn_periodos_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_periodos)
        )

        acciones_periodos = [
            self.action_crear_periodo,
            self.action_activar_periodo,
            self.action_marcar_vacaciones,
        ]
        for a in acciones_periodos:
            a.triggered.connect(
                lambda checked, a=a: aplicar_estilo_toolbar(
                    self.toolbar_periodos, acciones_periodos
                )
            )

        self.btn_periodos.clicked.connect(lambda: self.action_crear_periodo.trigger())
        self.btn_periodos_texto.clicked.connect(
            lambda: self.action_crear_periodo.trigger()
        )

        # ==============================
        # 📌 Materias y Horarios
        # ==============================
        self.action_alta_materia.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_alta_materia)
        )
        self.action_lista_materias.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_lista_materias)
        )
        self.action_editar_materia.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_editar_materia)
        )
        self.action_asignar_horarios.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_asignar_horarios)
        )
        self.action_salones.triggered.connect(
            lambda: self.stack_materias.setCurrentWidget(self.page_salones)
        )

        self.btn_materias_horarios.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(
                self.pagina_materias_horarios
            )
        )
        self.btn_materias_horarios_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(
                self.pagina_materias_horarios
            )
        )

        acciones_materias = [
            self.action_alta_materia,
            self.action_lista_materias,
            self.action_editar_materia,
            self.action_asignar_horarios,
            self.action_salones,
        ]
        for a in acciones_materias:
            a.triggered.connect(
                lambda checked, a=a: aplicar_estilo_toolbar(
                    self.toolbar_materias, acciones_materias
                )
            )

        self.btn_materias_horarios.clicked.connect(
            lambda: self.action_alta_materia.trigger()
        )
        self.btn_materias_horarios_texto.clicked.connect(
            lambda: self.action_alta_materia.trigger()
        )

        # ==============================
        # 📌 Reportes Globales
        # ==============================
        self.action_alumnos_periodo.triggered.connect(
            lambda: self.stack_reportes.setCurrentWidget(self.page_alumnos_periodo)
        )
        self.action_maestros_periodo.triggered.connect(
            lambda: self.stack_reportes.setCurrentWidget(self.page_maestros_periodo)
        )
        self.action_materias_periodo.triggered.connect(
            lambda: self.stack_reportes.setCurrentWidget(self.page_materias_periodo)
        )
        self.action_reporte_usuarios.triggered.connect(
            lambda: self.stack_reportes.setCurrentWidget(self.page_reporte_usuarios)
        )

        self.btn_reportes_globales.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(
                self.pagina_reportes_globales
            )
        )
        self.btn_reportes_globales_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(
                self.pagina_reportes_globales
            )
        )

        acciones_reportes = [
            self.action_alumnos_periodo,
            self.action_maestros_periodo,
            self.action_materias_periodo,
            self.action_reporte_usuarios,
        ]
        for a in acciones_reportes:
            a.triggered.connect(
                lambda checked, a=a: aplicar_estilo_toolbar(
                    self.toolbar_reportes, acciones_reportes
                )
            )

        self.btn_reportes_globales.clicked.connect(
            lambda: self.action_alumnos_periodo.trigger()
        )
        self.btn_reportes_globales_texto.clicked.connect(
            lambda: self.action_alumnos_periodo.trigger()
        )
        # ✅ Conexiones Sidebar - Página Acerca de
        self.btn_acercade.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_acercade)
        )
        self.btn_acercade_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_acercade)
        )

        # ✅ Mantener sincronizados icono y texto (checked)
        self.btn_acercade.toggled["bool"].connect(self.btn_acercade_texto.setChecked)
        self.btn_acercade_texto.toggled["bool"].connect(self.btn_acercade.setChecked)
        # === Conexiones de la Página Perfil ===
        self.btn_user.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_perfil)
        )

        # ✅ Cancelar (volver a la página de bienvenida)
        self.btn_cancelar_perfil.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_bienvenida)
        )

        self.retranslateUi(MainWindow)
        self.contendor_contenido.setCurrentIndex(0)
        self.btn_menu.toggled["bool"].connect(self.contenedor_menu_iconos.setVisible)  # type: ignore
        self.btn_menu.toggled["bool"].connect(self.contenedor_menu_completo.setHidden)  # type: ignore
        self.btn_inicio.toggled["bool"].connect(self.btn_inicio_texto.setChecked)  # type: ignore
        self.btn_usuarios.toggled["bool"].connect(self.btn_usuarios_texto.setChecked)  # type: ignore
        self.btn_periodos.toggled["bool"].connect(self.btn_periodos_texto.setChecked)  # type: ignore
        self.btn_materias_horarios.toggled["bool"].connect(self.btn_materias_horarios_texto.setChecked)  # type: ignore
        self.btn_reportes_globales.toggled["bool"].connect(self.btn_reportes_globales_texto.setChecked)  # type: ignore
        self.btn_inicio_texto.toggled["bool"].connect(self.btn_inicio.setChecked)  # type: ignore
        self.btn_usuarios_texto.toggled["bool"].connect(self.btn_usuarios.setChecked)  # type: ignore
        self.btn_periodos_texto.toggled["bool"].connect(self.btn_periodos.setChecked)  # type: ignore
        self.btn_materias_horarios_texto.toggled["bool"].connect(self.btn_materias_horarios.setChecked)  # type: ignore
        self.btn_reportes_globales_texto.toggled["bool"].connect(self.btn_reportes_globales.setChecked)  # type: ignore
        self.btn_acercade.toggled["bool"].connect(self.btn_acercade_texto.setChecked)  # type: ignore
        self.btn_acercade_texto.toggled["bool"].connect(self.btn_acercade.setChecked)  # type: ignore
        self.btn_logout_texto.toggled["bool"].connect(self.btn_logout.setChecked)  # type: ignore
        self.btn_logout.toggled["bool"].connect(self.btn_logout_texto.setChecked)  # type: ignore
        self.btn_logout_texto.clicked.connect(MainWindow.close)  # type: ignore
        self.btn_logout.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UAMISys"))
        self.titulo.setText(_translate("MainWindow", "UAMISys"))
        self.btn_inicio_texto.setText(_translate("MainWindow", "Inicio"))
        self.btn_usuarios_texto.setText(_translate("MainWindow", "Usuarios"))
        self.btn_periodos_texto.setText(_translate("MainWindow", "Periodos"))
        self.btn_materias_horarios_texto.setText(
            _translate("MainWindow", "Materias y horarios")
        )
        self.btn_reportes_globales_texto.setText(
            _translate("MainWindow", "Reportes globales")
        )
        self.btn_acercade_texto.setText(_translate("MainWindow", "Acerca dé"))
        self.btn_logout_texto.setText(_translate("MainWindow", "Cerrar sesión"))
        self.input_buscar.setPlaceholderText(_translate("MainWindow", "Buscar"))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cargar_periodos_en_combo()
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
        # ✅ Conexión para el perfil
        self.ui.btn_guardar_perfil.clicked.connect(self.guardar_cambios_perfil)
        self.ui.btn_cancelar_perfil.clicked.connect(
            lambda: self.ui.contendor_contenido.setCurrentWidget(
                self.ui.pagina_bienvenida
            )
        )

        # conexión alta usuario
        self.ui.btn_guardar_u_alta.clicked.connect(self.guardar_usuario_alta)
        self.ui.btn_cancelar_u_alta.clicked.connect(self.limpiar_campos_alta_usuario)

        # conexión baja usuario
        self.ui.input_buscar_baja_u.textChanged.connect(
            self.actualizar_combo_baja_usuarios
        )
        self.ui.combo_resultado_baja_u.currentIndexChanged.connect(
            self.mostrar_datos_usuario_combo
        )
        self.ui.btn_dar_baja_u.clicked.connect(self.dar_baja_usuario)

        # conexión cambiar rolee
        self.ui.input_buscar_roles.textChanged.connect(
            lambda: self.buscar_usuarios_y_llenar_combo(
                self.ui.input_buscar_roles, self.ui.combo_resultado_roles
            )
        )
        self.ui.combo_resultado_roles.currentIndexChanged.connect(
            self.mostrar_datos_usuario_roles
        )
        self.ui.btn_guardar_rol.clicked.connect(self.guardar_nuevo_rol_usuario)

        # coexión asignación contraseña
        self.ui.btn_guardar_password.clicked.connect(self.asignar_cambiar_contrasena)
        self.ui.btn_cancelar_password.clicked.connect(self.limpiar_campos_password)

        # conexión período
        self.ui.btn_guardar_periodo.clicked.connect(self.guardar_periodo)
        self.ui.btn_activar_periodo.clicked.connect(
            self.activar_periodo
        )  # activar período
        self.combo_periodos_disponibles = ComboBoxRecargable(
            self.cargar_periodos_en_combo
        )
        self.ui.btn_guardar_vacaciones.clicked.connect(
            self.marcar_vacaciones
        )  # conexxión vacaciones

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

    def guardar_cambios_perfil(self):
        correo = self.ui.input_correo.text()
        direccion = self.ui.input_direccion.text()
        telefono = self.ui.input_telefono.text()
        password = self.ui.input_password.text()

        # Aquí iría la lógica para guardar los datos en base de datos
        print("✅ Guardado perfil:")
        print("Correo:", correo)
        print("Dirección:", direccion)
        print("Teléfono:", telefono)
        print("Contraseña:", password)

        # Opcional: volver a bienvenida
        self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_bienvenida)

    def cerrar_sesion(self):
        import subprocess
        import sys
        import os

        ruta_login = os.path.join(os.path.dirname(__file__), "login.py")
        print("⚠️ Cerrando sesión y lanzando login.py...")
        subprocess.Popen([sys.executable, ruta_login])
        self.close()

    # guardar usuario / alta de usuario
    def guardar_usuario_alta(self):
        nombre = self.ui.input_nombre_u_alta.text().strip().upper()
        ap_paterno = self.ui.input_ap_paterno_u_alta.text().strip().upper()
        ap_materno = self.ui.input_ap_materno_u_alta.text().strip().upper()
        fecha_nac = self.ui.input_fecha_nac_u_alta.date().toString("yyyy-MM-dd")
        direccion = self.ui.input_direccion_u_alta.text().strip().upper()
        telefono = self.ui.input_telefono_u_alta.text().strip().upper()
        correo = self.ui.input_correo_u_alta.text().strip()  # se queda en minúsculas

        numero_economico = self.ui.input_numero_economico_u_alta.text().strip().upper()
        rol = self.ui.combo_rol_u_alta.currentText().strip().upper()
        rol = self.ui.combo_rol_u_alta.currentText()
        password = self.ui.input_password_u_alta.text().strip()
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        activo = self.ui.check_activo_u_alta.isChecked()

        # Validación rápida
        if not all(
            [
                nombre,
                ap_paterno,
                ap_materno,
                fecha_nac,
                direccion,
                telefono,
                correo,
                numero_economico,
                password,
            ]
        ):
            QtWidgets.QMessageBox.warning(
                self,
                "Campos vacíos",
                "Por favor, completa todos los campos obligatorios.",
            )
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            query = """
            INSERT INTO usuarios (
                numero_economico, nombre, apellido_paterno, apellido_materno,
                sexo, fecha_nacimiento, telefono, email, direccion,
                rol, contrasena, activo
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(
                query,
                (
                    numero_economico,
                    nombre,
                    ap_paterno,
                    ap_materno,
                    "X",  # ⚠️ No hay campo para sexo en el form
                    fecha_nac,
                    telefono,
                    correo,
                    direccion,
                    rol,
                    hashed_password,
                    activo,
                ),
            )

            conexion.commit()
            cursor.close()
            conexion.close()

            QtWidgets.QMessageBox.information(
                self, "Éxito", "Usuario dado de alta correctamente."
            )
            self.limpiar_campos_alta_usuario()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo dar de alta el usuario.\n{e}"
            )

    # limpiar formulario
    def limpiar_campos_alta_usuario(self):
        self.ui.input_nombre_u_alta.clear()
        self.ui.input_ap_paterno_u_alta.clear()
        self.ui.input_ap_materno_u_alta.clear()
        self.ui.input_fecha_nac_u_alta.setDate(QtCore.QDate(2000, 1, 1))
        self.ui.input_direccion_u_alta.clear()
        self.ui.input_telefono_u_alta.clear()
        self.ui.input_correo_u_alta.clear()
        self.ui.input_numero_economico_u_alta.clear()
        self.ui.combo_rol_u_alta.setCurrentIndex(0)
        self.ui.input_password_u_alta.clear()
        self.ui.check_activo_u_alta.setChecked(False)

    # buscar y actualizar combo
    def actualizar_combo_baja_usuarios(self):
        texto = self.ui.input_buscar_baja_u.text().strip().upper()
        self.ui.combo_resultado_baja_u.clear()

        if not texto:
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            query = """
                SELECT id, numero_economico, nombre, apellido_paterno, apellido_materno
                FROM usuarios
                WHERE activo = TRUE AND (
                    UPPER(nombre) LIKE %s OR
                    UPPER(apellido_paterno) LIKE %s OR
                    UPPER(apellido_materno) LIKE %s OR
                    UPPER(numero_economico) LIKE %s
                )
            """
            like_text = f"%{texto}%"
            cursor.execute(query, (like_text, like_text, like_text, like_text))
            resultados = cursor.fetchall()

            for usuario in resultados:
                id_, num_econ, nombre, ap_pat, ap_mat = usuario
                etiqueta = f"{num_econ} - {nombre} {ap_pat} {ap_mat}"
                self.ui.combo_resultado_baja_u.addItem(etiqueta, id_)

            cursor.close()
            conexion.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo buscar usuarios.\n{e}"
            )

    # mostar datos
    def mostrar_datos_usuario_combo(self):
        index = self.ui.combo_resultado_baja_u.currentIndex()
        if index == -1:
            return

        id_usuario = self.ui.combo_resultado_baja_u.currentData()

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            query = """
                SELECT nombre, apellido_paterno, apellido_materno,
                    rol, email, activo
                FROM usuarios
                WHERE id = %s
            """
            cursor.execute(query, (id_usuario,))
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()

            if resultado:
                nombre, ap_pat, ap_mat, rol, correo, activo = resultado
                self.ui.label_nombre_baja_u.setText(f"{nombre} {ap_pat} {ap_mat}")
                self.ui.label_rol_baja_u.setText(rol)
                self.ui.label_correo_baja_u.setText(correo)
                self.ui.label_activo_baja_u.setText("Sí" if activo else "No")
            else:
                self.ui.label_nombre_baja_u.setText("No encontrado")
                self.ui.label_rol_baja_u.setText("")
                self.ui.label_correo_baja_u.setText("")
                self.ui.label_activo_baja_u.setText("")

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo obtener los datos del usuario.\n{e}"
            )

    # dar de baja usuario
    def dar_baja_usuario(self):
        index = self.ui.combo_resultado_baja_u.currentIndex()
        if index == -1:
            QtWidgets.QMessageBox.warning(
                self, "Sin selección", "Selecciona un usuario para dar de baja."
            )
            return

        id_usuario = self.ui.combo_resultado_baja_u.currentData()

        confirmacion = QtWidgets.QMessageBox.question(
            self,
            "Confirmar baja",
            "¿Estás seguro que deseas dar de baja al usuario seleccionado?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )

        if confirmacion == QtWidgets.QMessageBox.No:
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            query = "UPDATE usuarios SET activo = FALSE WHERE id = %s"
            cursor.execute(query, (id_usuario,))
            conexion.commit()
            cursor.close()
            conexion.close()

            QtWidgets.QMessageBox.information(
                self, "Listo", "Usuario dado de baja correctamente."
            )
            self.ui.input_buscar_baja_u.clear()
            self.ui.combo_resultado_baja_u.clear()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo dar de baja.\n{e}"
            )

        self.ui.label_nombre_baja_u.clear()
        self.ui.label_rol_baja_u.clear()
        self.ui.label_correo_baja_u.clear()
        self.ui.label_activo_baja_u.clear()

    # mostrar selección cambio de roles
    def mostrar_datos_usuario_roles(self):
        index = self.ui.combo_resultado_roles.currentIndex()
        if index == -1:
            return

        id_usuario = self.ui.combo_resultado_roles.currentData()

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            query = """
                SELECT nombre, apellido_paterno, apellido_materno,
                    rol, email, activo
                FROM usuarios
                WHERE id = %s
            """
            cursor.execute(query, (id_usuario,))
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()

            if resultado:
                nombre, ap_pat, ap_mat, rol, correo, activo = resultado
                self.ui.label_nombre_rol_actual.setText(f"{nombre} {ap_pat} {ap_mat}")
                self.ui.label_email_rol_actual.setText(correo)
                self.ui.label_rol_actual.setText(rol)
                self.ui.label_activo_rol_actual.setText("Sí" if activo else "No")
            else:
                self.limpiar_labels_roles()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo obtener los datos del usuario.\n{e}"
            )

    # limpiar roles
    def limpiar_labels_roles(self):
        self.ui.label_nombre_rol_actual.clear()
        self.ui.label_email_rol_actual.clear()
        self.ui.label_rol_actual.clear()
        self.ui.label_activo_rol_actual.clear()

    # combo cambiar roles
    def buscar_usuarios_y_llenar_combo(self, input_lineedit, combo_box):
        texto = input_lineedit.text().strip().upper()
        combo_box.clear()

        if not texto:
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            query = """
                SELECT id, numero_economico, nombre, apellido_paterno, apellido_materno
                FROM usuarios
                WHERE activo = TRUE AND (
                    UPPER(nombre) LIKE %s OR
                    UPPER(apellido_paterno) LIKE %s OR
                    UPPER(apellido_materno) LIKE %s OR
                    UPPER(numero_economico) LIKE %s
                )
            """
            like_text = f"%{texto}%"
            cursor.execute(query, (like_text, like_text, like_text, like_text))
            resultados = cursor.fetchall()

            for usuario in resultados:
                id_, num_econ, nombre, ap_pat, ap_mat = usuario
                etiqueta = f"{num_econ} - {nombre} {ap_pat} {ap_mat}"
                combo_box.addItem(etiqueta, id_)

            cursor.close()
            conexion.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo buscar usuarios.\n{e}"
            )

    # guardar nuevo rol
    def guardar_nuevo_rol_usuario(self):
        index = self.ui.combo_resultado_roles.currentIndex()
        if index == -1:
            QtWidgets.QMessageBox.warning(
                self, "Sin selección", "Selecciona un usuario para actualizar su rol."
            )
            return

        nuevo_rol = self.ui.combo_nuevo_rol.currentText().strip().upper()
        id_usuario = self.ui.combo_resultado_roles.currentData()

        confirm = QtWidgets.QMessageBox.question(
            self,
            "Confirmar cambio de rol",
            f"¿Estás seguro que deseas asignar el rol '{nuevo_rol}' al usuario seleccionado?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )

        if confirm == QtWidgets.QMessageBox.No:
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            query = "UPDATE usuarios SET rol = %s WHERE id = %s"
            cursor.execute(query, (nuevo_rol, id_usuario))
            conexion.commit()
            cursor.close()
            conexion.close()

            QtWidgets.QMessageBox.information(
                self, "Éxito", "Rol actualizado correctamente."
            )
            self.ui.input_buscar_roles.clear()
            self.ui.combo_resultado_roles.clear()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo cambiar el rol.\n{e}"
            )

        self.limpiar_labels_roles()

    # cabmiar contraseña
    def asignar_cambiar_contrasena(self):
        numero_economico = self.ui.input_usuario_pass.text().strip().upper()
        nueva_pass = self.ui.input_pass_nueva.text().strip()
        confirmar_pass = self.ui.input_pass_confirmar.text().strip()

        if not numero_economico or not nueva_pass or not confirmar_pass:
            QtWidgets.QMessageBox.warning(
                self, "Campos vacíos", "Completa todos los campos."
            )
            return

        if nueva_pass != confirmar_pass:
            QtWidgets.QMessageBox.warning(
                self, "Error", "Las contraseñas no coinciden."
            )
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            # Buscar usuario solo por número económico
            query_buscar = "SELECT id FROM usuarios WHERE UPPER(numero_economico) = %s"
            cursor.execute(query_buscar, (numero_economico,))
            resultado = cursor.fetchone()

            if not resultado:
                QtWidgets.QMessageBox.warning(
                    self, "No encontrado", "No se encontró el usuario."
                )
                cursor.close()
                conexion.close()
                return

            id_usuario = resultado[0]

            # Hashear la nueva contraseña
            hashed = bcrypt.hashpw(nueva_pass.encode("utf-8"), bcrypt.gensalt()).decode(
                "utf-8"
            )

            # Actualizar contraseña
            query_update = "UPDATE usuarios SET contrasena = %s WHERE id = %s"
            cursor.execute(query_update, (hashed, id_usuario))
            conexion.commit()
            cursor.close()
            conexion.close()

            QtWidgets.QMessageBox.information(
                self, "Éxito", "Contraseña actualizada correctamente."
            )
            self.limpiar_campos_password()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"Ocurrió un error al actualizar.\n{e}"
            )

    # limpiar campos contrasña asignación
    def limpiar_campos_password(self):
        self.ui.input_usuario_pass.clear()
        self.ui.input_pass_nueva.clear()
        self.ui.input_pass_confirmar.clear()

    # crear período
    def guardar_periodo(self):
        nombre = self.ui.input_nombre_periodo.text().strip().upper()
        fecha_inicio = self.ui.input_fecha_inicio.date().toString("yyyy-MM-dd")
        fecha_fin = self.ui.input_fecha_fin.date().toString("yyyy-MM-dd")

        if not nombre:
            QtWidgets.QMessageBox.warning(
                self, "Campo vacío", "El nombre del periodo no puede estar vacío."
            )
            return

        if fecha_inicio > fecha_fin:
            QtWidgets.QMessageBox.warning(
                self,
                "Fechas inválidas",
                "La fecha de inicio no puede ser posterior a la fecha de fin.",
            )
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            # Verificar si el nombre del periodo ya existe
            cursor.execute("SELECT id FROM periodos WHERE nombre = %s", (nombre,))
            if cursor.fetchone():
                QtWidgets.QMessageBox.warning(
                    self, "Ya existe", f"El periodo '{nombre}' ya existe."
                )
                cursor.close()
                conexion.close()
                return

            # Insertar nuevo periodo
            cursor.execute(
                """
                INSERT INTO periodos (nombre, fecha_inicio, fecha_fin)
                VALUES (%s, %s, %s)
            """,
                (nombre, fecha_inicio, fecha_fin),
            )

            conexion.commit()
            cursor.close()
            conexion.close()

            QtWidgets.QMessageBox.information(
                self, "Éxito", "Periodo creado correctamente."
            )
            self.limpiar_formulario_periodo()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo guardar el periodo.\n{e}"
            )

    # auxiliar para limpiar
    def limpiar_formulario_periodo(self):
        self.ui.input_nombre_periodo.clear()
        self.ui.input_fecha_inicio.setDate(QtCore.QDate.currentDate())
        self.ui.input_fecha_fin.setDate(QtCore.QDate.currentDate())

    # cargar períodos
    def cargar_periodos_en_combo(self):
        self.ui.combo_periodos_disponibles.clear()

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            cursor.execute("SELECT id, nombre FROM periodos ORDER BY fecha_inicio DESC")
            periodos = cursor.fetchall()

            for pid, nombre in periodos:
                self.ui.combo_periodos_disponibles.addItem(nombre, pid)

            cursor.close()
            conexion.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudieron cargar los períodos.\n{e}"
            )

    # activar período
    def activar_periodo(self):
        index = self.ui.combo_periodos_disponibles.currentIndex()
        if index == -1:
            QtWidgets.QMessageBox.warning(
                self, "Sin selección", "Selecciona un período para activarlo."
            )
            return

        id_periodo = self.ui.combo_periodos_disponibles.currentData()

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            # Primero desactivamos todos
            cursor.execute("UPDATE periodos SET activo = FALSE")

            # Luego activamos el seleccionado
            cursor.execute(
                "UPDATE periodos SET activo = TRUE WHERE id = %s", (id_periodo,)
            )

            conexion.commit()
            cursor.close()
            conexion.close()

            QtWidgets.QMessageBox.information(
                self, "Éxito", "El período fue activado correctamente."
            )

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo activar el período.\n{e}"
            )

    # cargar período
    def cargar_periodos_en_combo(self):
        self.ui.combo_periodos_disponibles.clear()

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            query = "SELECT id, nombre FROM periodos ORDER BY fecha_inicio DESC"
            cursor.execute(query)
            resultados = cursor.fetchall()

            for id_periodo, nombre in resultados:
                self.ui.combo_periodos_disponibles.addItem(nombre, id_periodo)

            cursor.close()
            conexion.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudieron cargar los períodos.\n{e}"
            )

    # marcar vacaciones
    def marcar_vacaciones(self):
        fecha_inicio = self.ui.input_fecha_inicio_vac.date().toString("yyyy-MM-dd")
        fecha_fin = self.ui.input_fecha_fin_vac.date().toString("yyyy-MM-dd")

        if fecha_inicio > fecha_fin:
            QtWidgets.QMessageBox.warning(
                self,
                "Fechas inválidas",
                "La fecha de inicio no puede ser posterior a la fecha de fin.",
            )
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()

            # Verificar cruce de fechas con periodos ya registrados
            query_check = """
                SELECT COUNT(*) FROM vacaciones
                WHERE NOT (%s > fecha_fin OR %s < fecha_inicio)
            """
            cursor.execute(query_check, (fecha_inicio, fecha_fin))
            resultado = cursor.fetchone()[0]

            if resultado > 0:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Cruce de Fechas",
                    "Ya existe un periodo de vacaciones que se cruza con las fechas seleccionadas.",
                )
                cursor.close()
                conexion.close()
                return

            # Insertar nuevo periodo si no hay cruce
            query_insert = (
                "INSERT INTO vacaciones (fecha_inicio, fecha_fin) VALUES (%s, %s)"
            )
            cursor.execute(query_insert, (fecha_inicio, fecha_fin))
            conexion.commit()

            cursor.close()
            conexion.close()

            QtWidgets.QMessageBox.information(
                self, "Éxito", "Las vacaciones fueron marcadas correctamente."
            )

            # Limpiar campos
            hoy = QtCore.QDate.currentDate()
            self.ui.input_fecha_inicio_vac.setDate(hoy)
            self.ui.input_fecha_fin_vac.setDate(hoy)

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error", f"No se pudo guardar el periodo de vacaciones.\n{e}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("./qss/estilos.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
