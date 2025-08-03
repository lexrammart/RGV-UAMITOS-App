from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QActionGroup
import sys
import datetime
from data_access.insertar_datos_dao import *
from db_connection import connect_db  # <-- Importar conectar
import subprocess
import os
import recursos


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
        self.logo_1.setPixmap(QtGui.QPixmap(":/prefijoNuevo/recursos/logoUamitos.png"))
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
            QtGui.QPixmap(":/prefijoNuevo/iconos/casa.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/casa-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_inicio_texto.setIcon(icon)
        self.btn_inicio_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_inicio_texto.setCheckable(True)
        self.btn_inicio_texto.setAutoExclusive(True)
        self.btn_inicio_texto.setObjectName("btn_inicio_texto")
        self.verticalLayout_2.addWidget(self.btn_inicio_texto)
        self.btn_alumnos_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/alumno-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon1.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/alumno.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_alumnos_texto.setIcon(icon1)
        self.btn_alumnos_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_alumnos_texto.setCheckable(True)
        self.btn_alumnos_texto.setAutoExclusive(True)
        self.btn_alumnos_texto.setObjectName("btn_alumnos_texto")
        self.verticalLayout_2.addWidget(self.btn_alumnos_texto)
        self.btn_maestros_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/maestro-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon2.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/maestro.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_maestros_texto.setIcon(icon2)
        self.btn_maestros_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_maestros_texto.setCheckable(True)
        self.btn_maestros_texto.setAutoExclusive(True)
        self.btn_maestros_texto.setObjectName("btn_maestros_texto")
        self.verticalLayout_2.addWidget(self.btn_maestros_texto)
        self.btn_materias_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/libros.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon3.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/libros-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_materias_texto.setIcon(icon3)
        self.btn_materias_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_materias_texto.setCheckable(True)
        self.btn_materias_texto.setAutoExclusive(True)
        self.btn_materias_texto.setObjectName("btn_materias_texto")
        self.verticalLayout_2.addWidget(self.btn_materias_texto)
        self.btndocumentos_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/abrir-documento-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon4.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/abrir-documento.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btndocumentos_texto.setIcon(icon4)
        self.btndocumentos_texto.setIconSize(QtCore.QSize(20, 20))
        self.btndocumentos_texto.setCheckable(True)
        self.btndocumentos_texto.setAutoExclusive(True)
        self.btndocumentos_texto.setObjectName("btndocumentos_texto")
        self.verticalLayout_2.addWidget(self.btndocumentos_texto)
        self.btn_reportes_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/analitica.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon5.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/analitica-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_reportes_texto.setIcon(icon5)
        self.btn_reportes_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_reportes_texto.setCheckable(True)
        self.btn_reportes_texto.setAutoExclusive(True)
        self.btn_reportes_texto.setObjectName("btn_reportes_texto")
        self.verticalLayout_2.addWidget(self.btn_reportes_texto)
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
        self.btn_logout_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/acerca-de-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon6.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/acerca-de.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_logout_texto.setIcon(icon6)
        self.btn_logout_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_logout_texto.setCheckable(True)
        self.btn_logout_texto.setAutoExclusive(True)
        self.btn_logout_texto.setObjectName("btn_logout_texto")
        self.verticalLayout_5.addWidget(self.btn_logout_texto)
        self.btn_acercade_texto = QtWidgets.QPushButton(
            parent=self.contenedor_menu_completo
        )
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/cerrar-sesion-2.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon7.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/cerrar-sesion.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_acercade_texto.setIcon(icon7)
        self.btn_acercade_texto.setIconSize(QtCore.QSize(20, 20))
        self.btn_acercade_texto.setCheckable(True)
        self.btn_acercade_texto.setAutoExclusive(True)
        self.btn_acercade_texto.setObjectName("btn_acercade_texto")
        self.verticalLayout_5.addWidget(self.btn_acercade_texto)
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/lista.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon8.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/lista.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_menu.setIcon(icon8)
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/buscar.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_buscar.setIcon(icon9)
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/usuario.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btn_user.setIcon(icon10)
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
        self.pagina_bienvenida = QtWidgets.QWidget()
        self.pagina_bienvenida.setObjectName("pagina_bienvenida")
        ##########pagina bienvenida##################
        # === Layout de la página de bienvenida ===
        self.layout_bienvenida = QtWidgets.QVBoxLayout(self.pagina_bienvenida)
        self.layout_bienvenida.setContentsMargins(0, 50, 0, 0)
        self.layout_bienvenida.setSpacing(20)
        self.layout_bienvenida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.contendor_contenido.addWidget(self.pagina_bienvenida)

        # === Label para mensaje dinámico ===
        self.label_bienvenida = QtWidgets.QLabel()
        font_b = QtGui.QFont()
        font_b.setFamily("Verdana")
        font_b.setPointSize(24)
        font_b.setBold(True)
        self.label_bienvenida.setFont(font_b)
        self.label_bienvenida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_bienvenida.addWidget(self.label_bienvenida)

        # === Label para la hora ===
        self.label_hora = QtWidgets.QLabel()
        font_hora = QtGui.QFont()
        font_hora.setFamily("Consolas")
        font_hora.setPointSize(22)
        self.label_hora.setFont(font_hora)
        self.label_hora.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_bienvenida.addWidget(self.label_hora)

        # === Imagen bienvenida ===
        self.label_imagen = QtWidgets.QLabel()
        self.label_imagen.setPixmap(QtGui.QPixmap("./recursos/imagen1.png"))
        self.label_imagen.setScaledContents(True)
        self.label_imagen.setFixedSize(450, 300)
        self.label_imagen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_bienvenida.addWidget(self.label_imagen)

        ##########fin de pagina bienvenida##########
        self.pagina_maestros = QtWidgets.QWidget()
        self.pagina_maestros.setObjectName("pagina_maestros")
        ######### Inicio de página maestros ##############
        # ===============================
        # 📌 Página de Maestros (completa)
        # ===============================
        self.pagina_maestros = QtWidgets.QWidget()
        self.pagina_maestros.setObjectName("pagina_maestros")
        self.layout_maestros = QtWidgets.QVBoxLayout(self.pagina_maestros)

        # === QToolBar de Maestros ===
        self.toolbar_maestros = QtWidgets.QToolBar()
        self.toolbar_maestros.setMovable(False)
        self.layout_maestros.addWidget(self.toolbar_maestros)

        self.action_alta_maestro = QtGui.QAction("Alta", MainWindow)
        self.action_baja_maestro = QtGui.QAction("Baja", MainWindow)
        self.action_actualizar_maestro = QtGui.QAction("Actualizar", MainWindow)
        self.action_imprimir_horario_m = QtGui.QAction("Imprimir Horario", MainWindow)

        self.toolbar_maestros.addAction(self.action_alta_maestro)
        self.toolbar_maestros.addAction(self.action_baja_maestro)
        self.toolbar_maestros.addAction(self.action_actualizar_maestro)
        self.toolbar_maestros.addAction(self.action_imprimir_horario_m)

        # === Stacked interno para Maestros ===
        self.stack_maestros = QtWidgets.QStackedWidget()
        self.layout_maestros.addWidget(self.stack_maestros)

        # ===============================
        # 🚀 Alta de Maestros
        # ===============================
        self.page_alta_maestro = QtWidgets.QWidget()
        alta_m_layout = QtWidgets.QVBoxLayout(self.page_alta_maestro)

        group_datos_personales_m = QtWidgets.QGroupBox("Datos Personales")
        form_personales_m = QtWidgets.QFormLayout(group_datos_personales_m)
        self.input_nombre_m_alta = QtWidgets.QLineEdit()
        self.input_ap_paterno_m_alta = QtWidgets.QLineEdit()
        self.input_ap_materno_m_alta = QtWidgets.QLineEdit()
        self.input_fecha_nac_m_alta = QtWidgets.QDateEdit()
        self.input_fecha_nac_m_alta.setCalendarPopup(True)
        self.input_fecha_nac_m_alta.setDisplayFormat("dd/MM/yyyy")
        self.input_direccion_m_alta = QtWidgets.QLineEdit()
        self.input_correo_m_alta = QtWidgets.QLineEdit()

        form_personales_m.addRow("Nombre(s):", self.input_nombre_m_alta)
        form_personales_m.addRow("Apellido Paterno:", self.input_ap_paterno_m_alta)
        form_personales_m.addRow("Apellido Materno:", self.input_ap_materno_m_alta)
        form_personales_m.addRow("Fecha Nacimiento:", self.input_fecha_nac_m_alta)
        form_personales_m.addRow("Dirección:", self.input_direccion_m_alta)
        form_personales_m.addRow("Correo:", self.input_correo_m_alta)

        group_datos_escolares_m = QtWidgets.QGroupBox("Datos Laborales")
        form_escolares_m = QtWidgets.QFormLayout(group_datos_escolares_m)
        self.input_numero_economico_m_alta = QtWidgets.QLineEdit()
        self.check_activo_m_alta = QtWidgets.QCheckBox("Activo")
        form_escolares_m.addRow("Número Económico:", self.input_numero_economico_m_alta)
        form_escolares_m.addRow("", self.check_activo_m_alta)

        btn_layout_alta_m = QtWidgets.QHBoxLayout()
        btn_layout_alta_m.addStretch()
        self.btn_guardar_m_alta = QtWidgets.QPushButton("Dar de Alta Maestro")
        self.btn_cancelar_m_alta = QtWidgets.QPushButton("Cancelar")
        btn_layout_alta_m.addWidget(self.btn_guardar_m_alta)
        btn_layout_alta_m.addWidget(self.btn_cancelar_m_alta)

        alta_m_layout.addWidget(group_datos_personales_m)
        alta_m_layout.addWidget(group_datos_escolares_m)
        alta_m_layout.addLayout(btn_layout_alta_m)
        self.stack_maestros.addWidget(self.page_alta_maestro)

        # ===============================
        # 🚀 Baja de Maestros
        # ===============================
        self.page_baja_maestro = QtWidgets.QWidget()
        baja_m_layout = QtWidgets.QVBoxLayout(self.page_baja_maestro)
        self.input_buscar_baja_m = QtWidgets.QLineEdit()
        self.input_buscar_baja_m.setPlaceholderText(
            "Buscar por nombre o número económico"
        )
        self.combo_baja_maestro = QtWidgets.QComboBox()
        self.btn_baja_maestro = QtWidgets.QPushButton("Dar de Baja")
        baja_m_layout.addWidget(QtWidgets.QLabel("Buscar Maestro:"))
        baja_m_layout.addWidget(self.input_buscar_baja_m)
        baja_m_layout.addWidget(self.combo_baja_maestro)
        baja_m_layout.addStretch()
        baja_m_layout.addWidget(self.btn_baja_maestro)
        self.stack_maestros.addWidget(self.page_baja_maestro)

        # ===============================
        # 🚀 Actualizar Datos de Maestros
        # ===============================
        self.page_actualizar_maestro = QtWidgets.QWidget()
        update_m_layout = QtWidgets.QVBoxLayout(self.page_actualizar_maestro)

        group_buscar_m = QtWidgets.QGroupBox("Buscar Maestro")
        buscar_form_m = QtWidgets.QFormLayout(group_buscar_m)
        self.input_buscar_update_m = QtWidgets.QLineEdit()
        self.input_buscar_update_m.setPlaceholderText(
            "Buscar por nombre o número económico"
        )
        self.combo_update_maestro = QtWidgets.QComboBox()
        buscar_form_m.addRow("Buscar:", self.input_buscar_update_m)
        buscar_form_m.addRow("Seleccionar:", self.combo_update_maestro)

        group_update_m = QtWidgets.QGroupBox("Actualizar Datos")
        form_update_m = QtWidgets.QFormLayout(group_update_m)
        self.input_nombre_update_m = QtWidgets.QLineEdit()
        self.input_ap_paterno_update_m = QtWidgets.QLineEdit()
        self.input_ap_materno_update_m = QtWidgets.QLineEdit()
        self.input_direccion_update_m = QtWidgets.QLineEdit()
        self.input_correo_update_m = QtWidgets.QLineEdit()
        self.input_numero_economico_update_m = QtWidgets.QLineEdit()
        self.check_activo_update_m = QtWidgets.QCheckBox("Activo")

        form_update_m.addRow("Nombre(s):", self.input_nombre_update_m)
        form_update_m.addRow("Apellido Paterno:", self.input_ap_paterno_update_m)
        form_update_m.addRow("Apellido Materno:", self.input_ap_materno_update_m)
        form_update_m.addRow("Dirección:", self.input_direccion_update_m)
        form_update_m.addRow("Correo:", self.input_correo_update_m)
        form_update_m.addRow("Número Económico:", self.input_numero_economico_update_m)
        form_update_m.addRow("", self.check_activo_update_m)

        btn_layout_update_m = QtWidgets.QHBoxLayout()
        btn_layout_update_m.addStretch()
        self.btn_guardar_update_m = QtWidgets.QPushButton("Actualizar")
        self.btn_cancelar_update_m = QtWidgets.QPushButton("Cancelar")
        btn_layout_update_m.addWidget(self.btn_guardar_update_m)
        btn_layout_update_m.addWidget(self.btn_cancelar_update_m)

        update_m_layout.addWidget(group_buscar_m)
        update_m_layout.addWidget(group_update_m)
        update_m_layout.addLayout(btn_layout_update_m)
        self.stack_maestros.addWidget(self.page_actualizar_maestro)

        # ===============================
        # 🚀 Imprimir Horario de Maestros
        # ===============================
        self.page_imprimir_horario_m = QtWidgets.QWidget()
        horario_m_layout = QtWidgets.QVBoxLayout(self.page_imprimir_horario_m)
        self.input_buscar_horario_m = QtWidgets.QLineEdit()
        self.input_buscar_horario_m.setPlaceholderText(
            "Buscar por nombre o número económico"
        )
        self.btn_generar_pdf_m = QtWidgets.QPushButton("Generar Horario en PDF")
        horario_m_layout.addWidget(QtWidgets.QLabel("Generar horario del maestro"))
        horario_m_layout.addWidget(self.input_buscar_horario_m)
        horario_m_layout.addStretch()
        horario_m_layout.addWidget(self.btn_generar_pdf_m)
        self.stack_maestros.addWidget(self.page_imprimir_horario_m)

        # === Conexión de acciones de Toolbar ===
        self.action_alta_maestro.triggered.connect(
            lambda checked: self.stack_maestros.setCurrentWidget(self.page_alta_maestro)
        )
        self.action_baja_maestro.triggered.connect(
            lambda checked: self.stack_maestros.setCurrentWidget(self.page_baja_maestro)
        )
        self.action_actualizar_maestro.triggered.connect(
            lambda checked: self.stack_maestros.setCurrentWidget(
                self.page_actualizar_maestro
            )
        )
        self.action_imprimir_horario_m.triggered.connect(
            lambda checked: self.stack_maestros.setCurrentWidget(
                self.page_imprimir_horario_m
            )
        )

        ######### Fin página maestros ##############
        self.contendor_contenido.addWidget(self.pagina_maestros)

        ######### Inicio de página materias ##############
        # ===============================
        # 📌 Página de Materias (completa)
        # ===============================
        self.pagina_materias = QtWidgets.QWidget()
        self.pagina_materias.setObjectName("pagina_materias")
        self.layout_materias = QtWidgets.QVBoxLayout(self.pagina_materias)

        # === QToolBar de Materias ===
        self.toolbar_materias = QtWidgets.QToolBar()
        self.toolbar_materias.setMovable(False)
        self.layout_materias.addWidget(self.toolbar_materias)

        self.action_alta_materia = QtGui.QAction("Alta", MainWindow)
        self.action_baja_materia = QtGui.QAction("Baja", MainWindow)
        self.action_actualizar_materia = QtGui.QAction("Actualizar", MainWindow)

        self.toolbar_materias.addAction(self.action_alta_materia)
        self.toolbar_materias.addAction(self.action_baja_materia)
        self.toolbar_materias.addAction(self.action_actualizar_materia)

        # === Stacked interno para Materias ===
        self.stack_materias = QtWidgets.QStackedWidget()
        self.layout_materias.addWidget(self.stack_materias)

        # ===============================
        # 🚀 Alta de Materias
        # ===============================
        self.page_alta_materia = QtWidgets.QWidget()
        alta_mat_layout = QtWidgets.QVBoxLayout(self.page_alta_materia)

        group_datos_materia = QtWidgets.QGroupBox("Datos de la Materia")
        form_materia = QtWidgets.QFormLayout(group_datos_materia)
        self.input_nombre_materia_alta = QtWidgets.QLineEdit()
        self.input_clave_materia_alta = QtWidgets.QLineEdit()
        self.spin_creditos_materia_alta = QtWidgets.QSpinBox()
        self.spin_creditos_materia_alta.setRange(1, 20)
        self.spin_cupo_materia_alta = QtWidgets.QSpinBox()
        self.spin_cupo_materia_alta.setRange(1, 100)

        form_materia.addRow("Nombre:", self.input_nombre_materia_alta)
        form_materia.addRow("Clave:", self.input_clave_materia_alta)
        form_materia.addRow("Créditos:", self.spin_creditos_materia_alta)
        form_materia.addRow("Cupo Máximo:", self.spin_cupo_materia_alta)

        alta_mat_layout.addWidget(group_datos_materia)
        self.stack_materias.addWidget(self.page_alta_materia)

        # ===============================
        # 🚀 Baja de Materias (corregida)
        # ===============================
        self.page_baja_materia_m = (
            QtWidgets.QWidget()
        )  # 🔹 Nombre único para evitar conflicto
        baja_mat_layout = QtWidgets.QVBoxLayout(self.page_baja_materia_m)
        self.input_buscar_baja_materia = QtWidgets.QLineEdit()
        self.input_buscar_baja_materia.setPlaceholderText("Buscar por nombre o clave")
        self.combo_baja_materia = QtWidgets.QComboBox()
        self.btn_baja_materia = QtWidgets.QPushButton("Dar de Baja")
        baja_mat_layout.addWidget(QtWidgets.QLabel("Buscar Materia:"))
        baja_mat_layout.addWidget(self.input_buscar_baja_materia)
        baja_mat_layout.addWidget(self.combo_baja_materia)
        baja_mat_layout.addStretch()
        baja_mat_layout.addWidget(self.btn_baja_materia)
        self.stack_materias.addWidget(self.page_baja_materia_m)

        # ===============================
        # 🚀 Actualizar Materias
        # ===============================
        self.page_actualizar_materia = QtWidgets.QWidget()
        update_mat_layout = QtWidgets.QVBoxLayout(self.page_actualizar_materia)

        group_buscar_materia = QtWidgets.QGroupBox("Buscar Materia")
        buscar_form_mat = QtWidgets.QFormLayout(group_buscar_materia)
        self.input_buscar_update_materia = QtWidgets.QLineEdit()
        self.input_buscar_update_materia.setPlaceholderText("Buscar por nombre o clave")
        self.combo_update_materia = QtWidgets.QComboBox()
        buscar_form_mat.addRow("Buscar:", self.input_buscar_update_materia)
        buscar_form_mat.addRow("Seleccionar:", self.combo_update_materia)

        group_update_materia = QtWidgets.QGroupBox("Actualizar Datos")
        form_update_materia = QtWidgets.QFormLayout(group_update_materia)
        self.input_nombre_update_materia = QtWidgets.QLineEdit()
        self.input_clave_update_materia = QtWidgets.QLineEdit()
        self.spin_creditos_update_materia = QtWidgets.QSpinBox()
        self.spin_creditos_update_materia.setRange(1, 20)
        self.spin_cupo_update_materia = QtWidgets.QSpinBox()
        self.spin_cupo_update_materia.setRange(1, 100)

        form_update_materia.addRow("Nombre:", self.input_nombre_update_materia)
        form_update_materia.addRow("Clave:", self.input_clave_update_materia)
        form_update_materia.addRow("Créditos:", self.spin_creditos_update_materia)
        form_update_materia.addRow("Cupo Máximo:", self.spin_cupo_update_materia)

        btn_layout_update_mat = QtWidgets.QHBoxLayout()
        btn_layout_update_mat.addStretch()
        self.btn_guardar_update_materia = QtWidgets.QPushButton("Actualizar")
        self.btn_cancelar_update_materia = QtWidgets.QPushButton("Cancelar")
        btn_layout_update_mat.addWidget(self.btn_guardar_update_materia)
        btn_layout_update_mat.addWidget(self.btn_cancelar_update_materia)

        update_mat_layout.addWidget(group_buscar_materia)
        update_mat_layout.addWidget(group_update_materia)
        update_mat_layout.addLayout(btn_layout_update_mat)
        self.stack_materias.addWidget(self.page_actualizar_materia)

        # === Conexión de Toolbar ===
        self.action_alta_materia.triggered.connect(
            lambda checked: self.stack_materias.setCurrentWidget(self.page_alta_materia)
        )
        self.action_baja_materia.triggered.connect(
            lambda checked: self.stack_materias.setCurrentWidget(
                self.page_baja_materia_m
            )
        )
        self.action_actualizar_materia.triggered.connect(
            lambda checked: self.stack_materias.setCurrentWidget(
                self.page_actualizar_materia
            )
        )

        # ✅ Agregar la página al Stacked principal
        self.contendor_contenido.addWidget(self.pagina_materias)
        ############# Fin de página materias ##############

        # ===============================
        # 📌 Página de Documentos
        # ===============================
        self.pagina_documentos = QtWidgets.QWidget()
        self.pagina_documentos.setObjectName("pagina_documentos")
        self.layout_documentos = QtWidgets.QVBoxLayout(self.pagina_documentos)

        # === QToolBar de Documentos ===
        self.toolbar_documentos = QtWidgets.QToolBar()
        self.toolbar_documentos.setMovable(False)
        self.layout_documentos.addWidget(self.toolbar_documentos)

        self.action_alta_documento = QtGui.QAction("Subir Documento", MainWindow)
        self.action_validar_documento = QtGui.QAction("Validar Documentos", MainWindow)
        self.action_consultar_documento = QtGui.QAction("Consultar", MainWindow)

        self.toolbar_documentos.addAction(self.action_alta_documento)
        self.toolbar_documentos.addAction(self.action_validar_documento)
        self.toolbar_documentos.addAction(self.action_consultar_documento)

        # === Stacked interno de Documentos ===
        self.stack_documentos = QtWidgets.QStackedWidget()
        self.layout_documentos.addWidget(self.stack_documentos)

        # ===============================
        # 🚀 Subir Documento
        # ===============================
        self.page_alta_documento = QtWidgets.QWidget()
        alta_doc_layout = QtWidgets.QVBoxLayout(self.page_alta_documento)

        group_datos_doc = QtWidgets.QGroupBox("Datos del Documento")
        form_doc = QtWidgets.QFormLayout(group_datos_doc)
        self.input_buscar_alumno_doc = QtWidgets.QLineEdit()
        self.input_buscar_alumno_doc.setPlaceholderText("Buscar por nombre o matrícula")
        self.combo_alumno_doc = QtWidgets.QComboBox()
        self.combo_tipo_documento = QtWidgets.QComboBox()
        self.combo_tipo_documento.addItems(
            [
                "Acta de nacimiento",
                "CURP",
                "Comprobante de domicilio",
                "Certificado de estudios",
            ]
        )
        self.btn_seleccionar_archivo = QtWidgets.QPushButton("Seleccionar Archivo")
        form_doc.addRow("Buscar Alumno:", self.input_buscar_alumno_doc)
        form_doc.addRow("Seleccionar Alumno:", self.combo_alumno_doc)
        form_doc.addRow("Tipo Documento:", self.combo_tipo_documento)
        form_doc.addRow("Archivo:", self.btn_seleccionar_archivo)

        btn_layout_alta_doc = QtWidgets.QHBoxLayout()
        btn_layout_alta_doc.addStretch()
        self.btn_subir_documento = QtWidgets.QPushButton("Subir Documento")
        btn_layout_alta_doc.addWidget(self.btn_subir_documento)

        alta_doc_layout.addWidget(group_datos_doc)
        alta_doc_layout.addLayout(btn_layout_alta_doc)
        self.stack_documentos.addWidget(self.page_alta_documento)

        # ===============================
        # 🚀 Validar Documentos
        # ===============================
        self.page_validar_documento = QtWidgets.QWidget()
        validar_doc_layout = QtWidgets.QVBoxLayout(self.page_validar_documento)
        self.lista_documentos_pendientes = QtWidgets.QListWidget()
        self.btn_validar_seleccionado = QtWidgets.QPushButton("Marcar como Validado")
        validar_doc_layout.addWidget(
            QtWidgets.QLabel("Documentos Pendientes de Validación")
        )
        validar_doc_layout.addWidget(self.lista_documentos_pendientes)
        validar_doc_layout.addWidget(self.btn_validar_seleccionado)
        self.stack_documentos.addWidget(self.page_validar_documento)

        # ===============================
        # 🚀 Consultar Documentos
        # ===============================
        self.page_consultar_documento = QtWidgets.QWidget()
        consultar_doc_layout = QtWidgets.QVBoxLayout(self.page_consultar_documento)
        self.input_buscar_consulta_doc = QtWidgets.QLineEdit()
        self.input_buscar_consulta_doc.setPlaceholderText(
            "Buscar por nombre o matrícula"
        )
        self.lista_documentos_alumno = QtWidgets.QListWidget()
        consultar_doc_layout.addWidget(QtWidgets.QLabel("Consultar Documentos"))
        consultar_doc_layout.addWidget(self.input_buscar_consulta_doc)
        consultar_doc_layout.addWidget(self.lista_documentos_alumno)
        self.stack_documentos.addWidget(self.page_consultar_documento)

        # === Conexión de Toolbar ===
        self.action_alta_documento.triggered.connect(
            lambda checked: self.stack_documentos.setCurrentWidget(
                self.page_alta_documento
            )
        )
        self.action_validar_documento.triggered.connect(
            lambda checked: self.stack_documentos.setCurrentWidget(
                self.page_validar_documento
            )
        )
        self.action_consultar_documento.triggered.connect(
            lambda checked: self.stack_documentos.setCurrentWidget(
                self.page_consultar_documento
            )
        )

        # ✅ Agregar al QStacked principal
        self.contendor_contenido.addWidget(self.pagina_documentos)
        ############# Fin de página documentos ##############

        # ===============================
        # 📌 Página de Reportes (TXT)
        # ===============================
        self.pagina_reportes = QtWidgets.QWidget()
        self.pagina_reportes.setObjectName("pagina_reportes")
        self.layout_reportes = QtWidgets.QVBoxLayout(self.pagina_reportes)

        # === QToolBar ===
        self.toolbar_reportes = QtWidgets.QToolBar()
        self.toolbar_reportes.setMovable(False)
        self.layout_reportes.addWidget(self.toolbar_reportes)

        self.action_generar_reporte = QtGui.QAction("Generar", MainWindow)
        self.action_cargar_reporte = QtGui.QAction("Cargar", MainWindow)
        self.action_exportar_reporte = QtGui.QAction("Exportar", MainWindow)

        self.toolbar_reportes.addAction(self.action_generar_reporte)
        self.toolbar_reportes.addAction(self.action_cargar_reporte)
        self.toolbar_reportes.addAction(self.action_exportar_reporte)

        # === Stacked interno ===
        self.stack_reportes = QtWidgets.QStackedWidget()
        self.layout_reportes.addWidget(self.stack_reportes)

        # ===============================
        # 🚀 Generar Reporte
        # ===============================
        self.page_generar_reporte = QtWidgets.QWidget()
        generar_layout = QtWidgets.QVBoxLayout(self.page_generar_reporte)

        self.combo_tipo_reporte = QtWidgets.QComboBox()
        self.combo_tipo_reporte.addItems(
            [
                "Alumnos Activos",
                "Maestros y Materias",
                "Inscripciones",
                "Documentos Validados",
            ]
        )
        self.btn_generar_txt = QtWidgets.QPushButton("Generar TXT")

        generar_layout.addWidget(QtWidgets.QLabel("Seleccionar Tipo de Reporte:"))
        generar_layout.addWidget(self.combo_tipo_reporte)
        generar_layout.addStretch()
        generar_layout.addWidget(self.btn_generar_txt)
        self.stack_reportes.addWidget(self.page_generar_reporte)

        # ===============================
        # 🚀 Cargar Reporte
        # ===============================
        self.page_cargar_reporte = QtWidgets.QWidget()
        cargar_layout = QtWidgets.QVBoxLayout(self.page_cargar_reporte)

        self.btn_cargar_txt = QtWidgets.QPushButton("Seleccionar Archivo TXT")
        self.texto_reporte = QtWidgets.QPlainTextEdit()
        self.texto_reporte.setReadOnly(True)

        cargar_layout.addWidget(self.btn_cargar_txt)
        cargar_layout.addWidget(self.texto_reporte)
        self.stack_reportes.addWidget(self.page_cargar_reporte)

        # ===============================
        # 🚀 Exportar Reporte
        # ===============================
        self.page_exportar_reporte = QtWidgets.QWidget()
        exportar_layout = QtWidgets.QVBoxLayout(self.page_exportar_reporte)

        self.input_texto_exportar = QtWidgets.QPlainTextEdit()
        self.btn_exportar_txt = QtWidgets.QPushButton("Guardar como TXT")
        exportar_layout.addWidget(QtWidgets.QLabel("Escribe datos para exportar"))
        exportar_layout.addWidget(self.input_texto_exportar)
        exportar_layout.addWidget(self.btn_exportar_txt)
        self.stack_reportes.addWidget(self.page_exportar_reporte)

        # === Conexión de Toolbar ===
        self.action_generar_reporte.triggered.connect(
            lambda checked: self.stack_reportes.setCurrentWidget(
                self.page_generar_reporte
            )
        )
        self.action_cargar_reporte.triggered.connect(
            lambda checked: self.stack_reportes.setCurrentWidget(
                self.page_cargar_reporte
            )
        )
        self.action_exportar_reporte.triggered.connect(
            lambda checked: self.stack_reportes.setCurrentWidget(
                self.page_exportar_reporte
            )
        )

        # ✅ Agregar al QStacked principal
        self.contendor_contenido.addWidget(self.pagina_reportes)

        ############### Fin pagina reportes ##############
        self.pagina_alumnos = QtWidgets.QWidget()
        self.pagina_alumnos.setObjectName("pagina_alumnos")
        # ===============================
        # 📌 Página de Alumnos (completa)
        # ===============================
        self.pagina_alumnos = QtWidgets.QWidget()
        self.pagina_alumnos.setObjectName("pagina_alumnos")
        self.layout_alumnos = QtWidgets.QVBoxLayout(self.pagina_alumnos)

        # === QToolBar para opciones de alumnos ===
        self.toolbar_alumnos = QtWidgets.QToolBar()
        self.toolbar_alumnos.setMovable(False)
        self.layout_alumnos.addWidget(self.toolbar_alumnos)

        self.action_alta_alumno = QtGui.QAction("Alta", MainWindow)
        self.action_baja_alumno = QtGui.QAction("Baja", MainWindow)
        self.action_actualizar_alumno = QtGui.QAction("Actualizar", MainWindow)
        self.action_inscribir_materia = QtGui.QAction("Inscribir Materias", MainWindow)
        self.action_baja_materia_alumno = QtGui.QAction("Baja Materias", MainWindow)
        self.action_imprimir_horario = QtGui.QAction("Imprimir Horario", MainWindow)

        self.toolbar_alumnos.addAction(self.action_alta_alumno)
        self.toolbar_alumnos.addAction(self.action_baja_alumno)
        self.toolbar_alumnos.addAction(self.action_actualizar_alumno)
        self.toolbar_alumnos.addAction(self.action_inscribir_materia)
        self.toolbar_alumnos.addAction(self.action_baja_materia_alumno)
        self.toolbar_alumnos.addAction(self.action_imprimir_horario)

        # === Stacked interno de Alumnos ===
        self.stack_alumnos = QtWidgets.QStackedWidget()
        self.layout_alumnos.addWidget(self.stack_alumnos)

        # ===============================
        # 🚀 Alta de Alumnos
        # ===============================
        self.page_alta_alumno = QtWidgets.QWidget()
        alta_layout = QtWidgets.QVBoxLayout(self.page_alta_alumno)

        group_datos_personales = QtWidgets.QGroupBox("Datos Personales")
        form_personales = QtWidgets.QFormLayout(group_datos_personales)
        self.input_nombre_alta = QtWidgets.QLineEdit()
        self.input_ap_paterno_alta = QtWidgets.QLineEdit()
        self.input_ap_materno_alta = QtWidgets.QLineEdit()
        self.input_fecha_nacimiento_alta = QtWidgets.QDateEdit()
        self.input_fecha_nacimiento_alta.setCalendarPopup(True)
        self.input_fecha_nacimiento_alta.setDisplayFormat("dd/MM/yyyy")
        self.input_direccion_alta = QtWidgets.QLineEdit()
        self.input_correo_alta = QtWidgets.QLineEdit()

        form_personales.addRow("Nombre(s):", self.input_nombre_alta)
        form_personales.addRow("Apellido Paterno:", self.input_ap_paterno_alta)
        form_personales.addRow("Apellido Materno:", self.input_ap_materno_alta)
        form_personales.addRow("Fecha Nacimiento:", self.input_fecha_nacimiento_alta)
        form_personales.addRow("Dirección:", self.input_direccion_alta)
        form_personales.addRow("Correo:", self.input_correo_alta)

        group_datos_escolares = QtWidgets.QGroupBox("Datos Escolares")
        form_escolares = QtWidgets.QFormLayout(group_datos_escolares)
        self.input_matricula_alta = QtWidgets.QLineEdit()
        self.combo_periodo_ingreso = QtWidgets.QComboBox()
        self.combo_periodo_ingreso.addItems(["2025-01", "2025-02"])
        self.check_activo_alta = QtWidgets.QCheckBox("Activo")
        form_escolares.addRow("Matrícula:", self.input_matricula_alta)
        form_escolares.addRow("Periodo de Ingreso:", self.combo_periodo_ingreso)
        form_escolares.addRow("", self.check_activo_alta)

        btn_layout_alta = QtWidgets.QHBoxLayout()
        btn_layout_alta.addStretch()
        self.btn_guardar_alta = QtWidgets.QPushButton("Dar de Alta Alumno")

        # self.btn_guardar_alta.clicked.connect(
        #     self.dar_alta_alumno
        # )  # ============================================================= Guardar alta connection
        self.btn_cancelar_alta = QtWidgets.QPushButton("Cancelar")
        btn_layout_alta.addWidget(self.btn_guardar_alta)
        btn_layout_alta.addWidget(self.btn_cancelar_alta)

        alta_layout.addWidget(group_datos_personales)
        alta_layout.addWidget(group_datos_escolares)
        alta_layout.addLayout(btn_layout_alta)
        self.stack_alumnos.addWidget(self.page_alta_alumno)

        # ===============================
        # 🚀 Baja de Alumnos
        # ===============================
        self.page_baja_alumno = QtWidgets.QWidget()
        baja_layout = QtWidgets.QVBoxLayout(self.page_baja_alumno)
        self.input_buscar_baja = QtWidgets.QLineEdit()
        self.input_buscar_baja.setPlaceholderText("Buscar por nombre o matrícula")
        self.combo_baja_alumno = QtWidgets.QComboBox()
        self.btn_baja_alumno = QtWidgets.QPushButton("Dar de Baja")
        baja_layout.addWidget(QtWidgets.QLabel("Buscar Alumno:"))
        baja_layout.addWidget(self.input_buscar_baja)
        baja_layout.addWidget(self.combo_baja_alumno)

        # Info del alumno seleccionado
        self.group_info_alumno = QtWidgets.QGroupBox("Información del Alumno")
        self.group_info_alumno.hide()
        info_layout = QtWidgets.QVBoxLayout(self.group_info_alumno)
        self.label_info_matricula = QtWidgets.QLabel("Matrícula: -")
        self.label_info_nombre = QtWidgets.QLabel("Nombre: -")
        self.label_info_direccion = QtWidgets.QLabel("Dirección: -")
        self.label_info_correo = QtWidgets.QLabel("Correo: -")
        info_layout.addWidget(self.label_info_matricula)
        info_layout.addWidget(self.label_info_nombre)
        info_layout.addWidget(self.label_info_direccion)
        info_layout.addWidget(self.label_info_correo)
        baja_layout.addWidget(self.group_info_alumno)  # 💡 debajo del combo

        baja_layout.addStretch()
        baja_layout.addWidget(self.btn_baja_alumno)
        self.stack_alumnos.addWidget(self.page_baja_alumno)

        # ===============================
        # 🚀 Actualizar Datos
        # ===============================
        self.page_actualizar_alumno = QtWidgets.QWidget()
        update_layout = QtWidgets.QVBoxLayout(self.page_actualizar_alumno)

        group_buscar = QtWidgets.QGroupBox("Buscar Alumno")
        buscar_form = QtWidgets.QFormLayout(group_buscar)
        self.input_buscar_update = QtWidgets.QLineEdit()
        self.input_buscar_update.setPlaceholderText("Buscar por nombre o matrícula")
        self.combo_update_alumno = QtWidgets.QComboBox()
        buscar_form.addRow("Buscar:", self.input_buscar_update)
        buscar_form.addRow("Seleccionar:", self.combo_update_alumno)

        group_update = QtWidgets.QGroupBox("Actualizar Datos")
        form_update = QtWidgets.QFormLayout(group_update)
        self.input_nombre_update = QtWidgets.QLineEdit()
        self.input_ap_paterno_update = QtWidgets.QLineEdit()
        self.input_ap_materno_update = QtWidgets.QLineEdit()
        self.input_direccion_update = QtWidgets.QLineEdit()
        self.input_correo_update = QtWidgets.QLineEdit()
        self.combo_periodo_update = QtWidgets.QComboBox()
        self.combo_periodo_update.addItems(["2025-01", "2025-02"])
        self.check_activo_update = QtWidgets.QCheckBox("Activo")

        form_update.addRow("Nombre(s):", self.input_nombre_update)
        form_update.addRow("Apellido Paterno:", self.input_ap_paterno_update)
        form_update.addRow("Apellido Materno:", self.input_ap_materno_update)
        form_update.addRow("Dirección:", self.input_direccion_update)
        form_update.addRow("Correo:", self.input_correo_update)
        form_update.addRow("Periodo de Ingreso:", self.combo_periodo_update)
        form_update.addRow("", self.check_activo_update)

        btn_layout_update = QtWidgets.QHBoxLayout()
        btn_layout_update.addStretch()
        self.btn_guardar_update = QtWidgets.QPushButton("Actualizar")
        self.btn_cancelar_update = QtWidgets.QPushButton("Cancelar")
        btn_layout_update.addWidget(self.btn_guardar_update)
        btn_layout_update.addWidget(self.btn_cancelar_update)

        update_layout.addWidget(group_buscar)
        update_layout.addWidget(group_update)
        update_layout.addLayout(btn_layout_update)
        self.stack_alumnos.addWidget(self.page_actualizar_alumno)

        # ===============================
        # 🚀 Inscribir Materias
        # ===============================
        self.page_inscribir_materia = QtWidgets.QWidget()
        inscribir_layout = QtWidgets.QVBoxLayout(self.page_inscribir_materia)
        self.input_buscar_inscribir = QtWidgets.QLineEdit()
        self.input_buscar_inscribir.setPlaceholderText("Buscar por nombre o matrícula")
        self.combo_inscribir_alumno = QtWidgets.QComboBox()
        self.lista_materias_inscribir = QtWidgets.QListWidget()
        self.lista_materias_inscribir.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.MultiSelection
        )
        self.btn_inscribir_materias = QtWidgets.QPushButton("Inscribir Seleccionadas")
        inscribir_layout.addWidget(QtWidgets.QLabel("Buscar Alumno:"))
        inscribir_layout.addWidget(self.input_buscar_inscribir)
        inscribir_layout.addWidget(self.combo_inscribir_alumno)
        inscribir_layout.addWidget(QtWidgets.QLabel("Materias Disponibles:"))
        inscribir_layout.addWidget(self.lista_materias_inscribir)
        inscribir_layout.addWidget(self.btn_inscribir_materias)
        self.stack_alumnos.addWidget(self.page_inscribir_materia)

        # ===============================
        # 🚀 Baja de Materias
        # ===============================
        self.page_baja_materia = QtWidgets.QWidget()
        baja_materia_layout = QtWidgets.QVBoxLayout(self.page_baja_materia)
        self.input_buscar_baja_materia = QtWidgets.QLineEdit()
        self.input_buscar_baja_materia.setPlaceholderText(
            "Buscar por nombre o matrícula"
        )
        self.combo_baja_materia_alumno = QtWidgets.QComboBox()
        self.lista_materias_baja = QtWidgets.QListWidget()
        self.lista_materias_baja.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.MultiSelection
        )
        self.btn_baja_materias = QtWidgets.QPushButton("Dar de Baja Seleccionadas")
        baja_materia_layout.addWidget(QtWidgets.QLabel("Buscar Alumno:"))
        baja_materia_layout.addWidget(self.input_buscar_baja_materia)
        baja_materia_layout.addWidget(self.combo_baja_materia_alumno)
        baja_materia_layout.addWidget(QtWidgets.QLabel("Materias Inscritas:"))
        baja_materia_layout.addWidget(self.lista_materias_baja)
        baja_materia_layout.addWidget(self.btn_baja_materias)
        self.stack_alumnos.addWidget(self.page_baja_materia)

        # ===============================
        # 🚀 Imprimir Horario
        # ===============================
        self.page_imprimir_horario = QtWidgets.QWidget()
        horario_layout = QtWidgets.QVBoxLayout(self.page_imprimir_horario)
        self.input_buscar_horario = QtWidgets.QLineEdit()
        self.input_buscar_horario.setPlaceholderText("Buscar por nombre o matrícula")
        self.btn_generar_pdf = QtWidgets.QPushButton("Generar Horario en PDF")
        horario_layout.addWidget(QtWidgets.QLabel("Generar horario del alumno"))
        horario_layout.addWidget(self.input_buscar_horario)
        horario_layout.addStretch()
        horario_layout.addWidget(self.btn_generar_pdf)
        self.stack_alumnos.addWidget(self.page_imprimir_horario)

        # === Conexión de Toolbar con Stacked ===
        self.action_alta_alumno.triggered.connect(
            lambda checked: self.stack_alumnos.setCurrentWidget(self.page_alta_alumno)
        )
        self.action_baja_alumno.triggered.connect(
            lambda checked: self.stack_alumnos.setCurrentWidget(self.page_baja_alumno)
        )
        self.action_actualizar_alumno.triggered.connect(
            lambda checked: self.stack_alumnos.setCurrentWidget(
                self.page_actualizar_alumno
            )
        )
        self.action_inscribir_materia.triggered.connect(
            lambda checked: self.stack_alumnos.setCurrentWidget(
                self.page_inscribir_materia
            )
        )
        self.action_baja_materia_alumno.triggered.connect(
            lambda checked: self.stack_alumnos.setCurrentWidget(self.page_baja_materia)
        )

        self.action_imprimir_horario.triggered.connect(
            lambda checked: self.stack_alumnos.setCurrentWidget(
                self.page_imprimir_horario
            )
        )
        self.contendor_contenido.addWidget(self.pagina_alumnos)

        ############# fin pagina alumnos ##############
        # ===============================
        # 📌 Página Acerca de (actualizada)
        # ===============================
        self.pagina_acercade = QtWidgets.QWidget()
        self.pagina_acercade.setObjectName("pagina_acercade")
        layout_acercade = QtWidgets.QVBoxLayout(self.pagina_acercade)
        layout_acercade.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # === Imagen de la empresa (con suavizado y proporción) ===
        self.logo_rgv = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("./recursos/RGV_Innovations.png")
        pixmap = pixmap.scaled(
            500,
            300,
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation,
        )
        self.logo_rgv.setPixmap(pixmap)
        self.logo_rgv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # === Texto elegante ===
        self.label_titulo_rgv = QtWidgets.QLabel("UAMISys")
        font_titulo = QtGui.QFont()
        font_titulo.setPointSize(28)
        font_titulo.setBold(True)
        self.label_titulo_rgv.setFont(font_titulo)
        self.label_titulo_rgv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.label_subtitulo_rgv = QtWidgets.QLabel(
            "Sistema Integral de Gestión Académica"
        )
        font_sub = QtGui.QFont()
        font_sub.setPointSize(14)
        self.label_subtitulo_rgv.setFont(font_sub)
        self.label_subtitulo_rgv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # === Créditos y enlace ===
        self.label_creditos = QtWidgets.QLabel(
            "Este programa fue desarrollado por <b>RGV Innovations</b><br>"
            "Con el objetivo de optimizar la gestión académica y ofrecer una experiencia moderna y eficiente.<br><br>"
            "Repositorio disponible en:"
        )
        font_creditos = QtGui.QFont()
        font_creditos.setPointSize(12)
        self.label_creditos.setFont(font_creditos)
        self.label_creditos.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_creditos.setWordWrap(True)

        self.link_github = QtWidgets.QLabel()
        self.link_github.setText(
            '<a href="https://github.com/lexrammart/RGV-UAMITOS-App" style="color: #1565c0;">'
            "https://github.com/lexrammart/RGV-UAMITOS-App</a>"
        )
        self.link_github.setFont(font_creditos)
        self.link_github.setOpenExternalLinks(True)
        self.link_github.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

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

        ############# fin pagina acerca de ##############
        ######### botones stacked ##############
        from PySide6.QtGui import QActionGroup

        self.action_group_alumnos = QActionGroup(MainWindow)
        self.action_group_alumnos.setExclusive(True)
        self.action_alta_alumno.setCheckable(True)
        self.action_group_alumnos.addAction(self.action_alta_alumno)
        self.action_baja_alumno.setCheckable(True)
        self.action_group_alumnos.addAction(self.action_baja_alumno)
        self.action_actualizar_alumno.setCheckable(True)
        self.action_group_alumnos.addAction(self.action_actualizar_alumno)
        self.action_inscribir_materia.setCheckable(True)
        self.action_group_alumnos.addAction(self.action_inscribir_materia)
        self.action_baja_materia_alumno.setCheckable(True)
        self.action_group_alumnos.addAction(self.action_baja_materia_alumno)
        self.action_imprimir_horario.setCheckable(True)
        self.action_group_alumnos.addAction(self.action_imprimir_horario)

        self.action_group_maestros = QActionGroup(MainWindow)
        self.action_group_maestros.setExclusive(True)
        self.action_alta_maestro.setCheckable(True)
        self.action_group_maestros.addAction(self.action_alta_maestro)
        self.action_baja_maestro.setCheckable(True)
        self.action_group_maestros.addAction(self.action_baja_maestro)
        self.action_actualizar_maestro.setCheckable(True)
        self.action_group_maestros.addAction(self.action_actualizar_maestro)
        self.action_imprimir_horario_m.setCheckable(True)
        self.action_group_maestros.addAction(self.action_imprimir_horario_m)

        self.action_group_materias = QActionGroup(MainWindow)
        self.action_group_materias.setExclusive(True)
        self.action_alta_materia.setCheckable(True)
        self.action_group_materias.addAction(self.action_alta_materia)
        self.action_baja_materia.setCheckable(True)
        self.action_group_materias.addAction(self.action_baja_materia)
        self.action_actualizar_materia.setCheckable(True)
        self.action_group_materias.addAction(self.action_actualizar_materia)

        self.action_group_documentos = QActionGroup(MainWindow)
        self.action_group_documentos.setExclusive(True)
        self.action_alta_documento.setCheckable(True)
        self.action_group_documentos.addAction(self.action_alta_documento)
        self.action_validar_documento.setCheckable(True)
        self.action_group_documentos.addAction(self.action_validar_documento)
        self.action_consultar_documento.setCheckable(True)
        self.action_group_documentos.addAction(self.action_consultar_documento)

        self.action_group_reportes = QActionGroup(MainWindow)
        self.action_group_reportes.setExclusive(True)
        self.action_generar_reporte.setCheckable(True)
        self.action_group_reportes.addAction(self.action_generar_reporte)
        self.action_cargar_reporte.setCheckable(True)
        self.action_group_reportes.addAction(self.action_cargar_reporte)
        self.action_exportar_reporte.setCheckable(True)
        self.action_group_reportes.addAction(self.action_exportar_reporte)

        ######### fin botones stacked ##############
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/casa.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon11.addPixmap(
            QtGui.QPixmap(":/recursos/iconos/casa-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.btn_inicio.setIcon(icon11)
        self.btn_inicio.setIconSize(QtCore.QSize(26, 26))
        self.btn_inicio.setCheckable(True)
        self.btn_inicio.setAutoExclusive(True)
        self.btn_inicio.setObjectName("btn_inicio")
        self.verticalLayout.addWidget(self.btn_inicio)
        self.btn_alumnos = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_alumnos.setText("")
        self.btn_alumnos.setIcon(icon1)
        self.btn_alumnos.setIconSize(QtCore.QSize(26, 26))
        self.btn_alumnos.setCheckable(True)
        self.btn_alumnos.setAutoExclusive(True)
        self.btn_alumnos.setObjectName("btn_alumnos")
        self.verticalLayout.addWidget(self.btn_alumnos)
        self.btn_maestros = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_maestros.setText("")
        self.btn_maestros.setIcon(icon2)
        self.btn_maestros.setIconSize(QtCore.QSize(26, 26))
        self.btn_maestros.setCheckable(True)
        self.btn_maestros.setAutoExclusive(True)
        self.btn_maestros.setObjectName("btn_maestros")
        self.verticalLayout.addWidget(self.btn_maestros)
        self.btn_materias = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_materias.setText("")
        self.btn_materias.setIcon(icon3)
        self.btn_materias.setIconSize(QtCore.QSize(26, 26))
        self.btn_materias.setCheckable(True)
        self.btn_materias.setAutoExclusive(True)
        self.btn_materias.setObjectName("btn_materias")
        self.verticalLayout.addWidget(self.btn_materias)
        self.btn_documentos = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_documentos.setText("")
        self.btn_documentos.setIcon(icon4)
        self.btn_documentos.setIconSize(QtCore.QSize(26, 26))
        self.btn_documentos.setCheckable(True)
        self.btn_documentos.setAutoExclusive(True)
        self.btn_documentos.setObjectName("btn_documentos")
        self.verticalLayout.addWidget(self.btn_documentos)
        self.btn_reportes = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_reportes.setText("")
        self.btn_reportes.setIcon(icon5)
        self.btn_reportes.setIconSize(QtCore.QSize(26, 26))
        self.btn_reportes.setCheckable(True)
        self.btn_reportes.setAutoExclusive(True)
        self.btn_reportes.setObjectName("btn_reportes")
        self.verticalLayout.addWidget(self.btn_reportes)
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
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/acerca-de-1.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon12.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/acerca-de.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon12.addPixmap(
            QtGui.QPixmap(":/prefijoNuevo/iconos/acerca-de.png"),
            QtGui.QIcon.Mode.Disabled,
            QtGui.QIcon.State.On,
        )
        self.btn_acercade.setIcon(icon12)
        self.btn_acercade.setIconSize(QtCore.QSize(26, 26))
        self.btn_acercade.setCheckable(True)
        self.btn_acercade.setAutoExclusive(True)
        self.btn_acercade.setObjectName("btn_acercade")
        self.verticalLayout_3.addWidget(self.btn_acercade)
        self.btn_logout = QtWidgets.QPushButton(parent=self.contenedor_menu_iconos)
        self.btn_logout.setText("")
        self.btn_logout.setIcon(icon7)
        self.btn_logout.setIconSize(QtCore.QSize(26, 26))
        self.btn_logout.setCheckable(True)
        self.btn_logout.setAutoExclusive(True)
        self.btn_logout.setObjectName("btn_logout")
        self.verticalLayout_3.addWidget(self.btn_logout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.contenedor_menu_iconos, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.contenedo_principal)

        self.retranslateUi(MainWindow)
        self.contendor_contenido.setCurrentIndex(0)
        self.btn_menu.toggled["bool"].connect(self.contenedor_menu_iconos.setVisible)  # type: ignore
        self.btn_menu.toggled["bool"].connect(self.contenedor_menu_completo.setHidden)  # type: ignore
        self.btn_inicio.toggled["bool"].connect(self.btn_inicio_texto.setChecked)  # type: ignore
        self.btn_alumnos.toggled["bool"].connect(self.btn_alumnos_texto.setChecked)  # type: ignore
        self.btn_maestros.toggled["bool"].connect(self.btn_maestros_texto.setChecked)  # type: ignore
        self.btn_materias.toggled["bool"].connect(self.btn_materias_texto.setChecked)  # type: ignore
        self.btn_documentos.toggled["bool"].connect(self.btndocumentos_texto.setChecked)  # type: ignore
        self.btn_reportes.toggled["bool"].connect(self.btn_reportes_texto.setChecked)  # type: ignore
        self.btn_inicio_texto.toggled["bool"].connect(self.btn_inicio.setChecked)  # type: ignore
        self.btn_alumnos_texto.toggled["bool"].connect(self.btn_alumnos.setChecked)  # type: ignore
        self.btn_maestros_texto.toggled["bool"].connect(self.btn_maestros.setChecked)  # type: ignore
        self.btn_materias_texto.toggled["bool"].connect(self.btn_materias.setChecked)  # type: ignore
        self.btndocumentos_texto.toggled["bool"].connect(self.btn_documentos.setChecked)  # type: ignore
        self.btn_reportes_texto.toggled["bool"].connect(self.btn_reportes.setChecked)  # type: ignore
        self.btn_acercade.toggled["bool"].connect(self.btn_logout_texto.setChecked)  # type: ignore
        self.btn_logout_texto.toggled["bool"].connect(self.btn_acercade.setChecked)  # type: ignore
        self.btn_acercade_texto.toggled["bool"].connect(self.btn_logout.setChecked)  # type: ignore
        self.btn_logout.toggled["bool"].connect(self.btn_acercade_texto.setChecked)  # type: ignore
        self.btn_acercade_texto.clicked.connect(MainWindow.close)  # type: ignore
        self.btn_logout.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ####### Conectar señales de los botones a las páginas correspondientes ###
        # ✅ Cuando se haga click en Inicio, actualiza mensaje
        def _update_welcome():
            try:
                MainWindow.actualizar_bienvenida()
            except:
                pass

        self.btn_inicio.clicked.connect(_update_welcome)
        self.btn_inicio_texto.clicked.connect(_update_welcome)
        self.btn_inicio.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_bienvenida)
        )
        self.btn_inicio_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_bienvenida)
        )

        # ✅ Conectar botón de Alumnos con la página correspondiente
        self.btn_alumnos.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_alumnos)
        )
        self.btn_alumnos_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_alumnos)
        )
        self.btn_maestros.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_maestros)
        )
        self.btn_maestros_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_maestros)
        )
        self.btn_materias.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_materias)
        )
        self.btn_materias_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_materias)
        )
        self.btn_documentos.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_documentos)
        )
        self.btndocumentos_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_documentos)
        )
        self.btn_reportes.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_reportes)
        )
        self.btn_reportes_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_reportes)
        )
        self.btn_acercade.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_acercade)
        )
        self.btn_logout_texto.clicked.connect(
            lambda: self.contendor_contenido.setCurrentWidget(self.pagina_acercade)
        )

        ######## fin de conexión de señales ########

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UAMISys"))
        self.titulo.setText(_translate("MainWindow", "UAMISys"))
        self.btn_inicio_texto.setText(_translate("MainWindow", "Inicio"))
        self.btn_alumnos_texto.setText(_translate("MainWindow", "Alumnos"))
        self.btn_maestros_texto.setText(_translate("MainWindow", "Maestros"))
        self.btn_materias_texto.setText(_translate("MainWindow", "Materias"))
        self.btndocumentos_texto.setText(_translate("MainWindow", "Documentos"))
        self.btn_reportes_texto.setText(_translate("MainWindow", "Reportes"))
        self.btn_logout_texto.setText(_translate("MainWindow", "Acerca dé"))
        self.btn_acercade_texto.setText(_translate("MainWindow", "Cerrar sesión"))
        self.input_buscar.setPlaceholderText(_translate("MainWindow", "Buscar"))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # conexión cerrar sesión
        self.ui.btn_logout.clicked.connect(self.cerrar_sesion)
        self.ui.btn_acercade_texto.clicked.connect(self.cerrar_sesion)

        # ✅ Conexión de botón para seleccionar archivo de documento
        self.ui.btn_seleccionar_archivo.clicked.connect(
            self.seleccionar_archivo_documento
        )

        # ✅ Conexión de búsqueda
        self.ui.btn_buscar.clicked.connect(self.buscar_opcion)
        self.ui.input_buscar.returnPressed.connect(
            self.buscar_opcion
        )  # 🔥 Enter también busca

        # ✅ Configurar saludo inicial
        self.actualizar_bienvenida()

        # ✅ Actualizar cada minuto
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizar_bienvenida)
        self.timer.start(60000)

        # Ocultar menú de iconos al iniciar
        self.ui.contenedor_menu_iconos.hide()
        self.ui.contendor_contenido.setCurrentIndex(0)
        self.ui.btn_inicio.setChecked(True)

        # Variable para guardar ruta de documento seleccionado
        self.ruta_documento_seleccionado = None

        # conexión para alumno
        self.ui.btn_guardar_alta.clicked.connect(self.dar_alta_alumno)
        self.ui.btn_cancelar_alta.clicked.connect(self.limpiar_campos_alta_alumno)
        self.ui.btn_baja_alumno.clicked.connect(self.dar_baja_alumno)
        self.ui.input_buscar_baja.textChanged.connect(self.actualizar_combo_baja)
        self.ui.combo_baja_alumno.currentIndexChanged.connect(self.mostrar_info_baja)

    def cerrar_sesion(self):
        import subprocess
        import sys
        import os

        ruta_login = os.path.join(os.path.dirname(__file__), "login.py")
        print("⚠️ Cerrando sesión y lanzando login.py...")
        subprocess.Popen([sys.executable, ruta_login])
        self.close()

    def seleccionar_archivo_documento(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Documento",
            "",
            "Archivos PDF (*.pdf);;Imágenes (*.png *.jpg *.jpeg);;Todos los archivos (*.*)",
        )
        if ruta_archivo:
            self.ruta_documento_seleccionado = ruta_archivo
            nombre = ruta_archivo.split("/")[-1]
            self.ui.btn_seleccionar_archivo.setText(f"Seleccionado: {nombre}")
        else:
            self.ruta_documento_seleccionado = None
            self.ui.btn_seleccionar_archivo.setText("Seleccionar Archivo")

    def actualizar_bienvenida(self):
        ahora = datetime.datetime.now()
        hora = ahora.strftime("%I:%M %p")  # Formato 12h

        if ahora.hour < 12:
            saludo = "Buenos días"
        elif ahora.hour < 19:
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"

        self.ui.label_bienvenida.setText(f"{saludo} Uamito")
        self.ui.label_hora.setText(hora)

    def buscar_opcion(self):
        texto = self.ui.input_buscar.text().strip().lower()

        # 🔍 Alumnos
        if "alta alumno" in texto or texto == "alta":
            self.ui.btn_alumnos.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_alumnos)
            self.ui.stack_alumnos.setCurrentWidget(self.ui.page_alta_alumno)
        elif "baja alumno" in texto or texto == "baja":
            self.ui.btn_alumnos.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_alumnos)
            self.ui.stack_alumnos.setCurrentWidget(self.ui.page_baja_alumno)
        elif "actualizar alumno" in texto or "update alumno" in texto:
            self.ui.btn_alumnos.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_alumnos)
            self.ui.stack_alumnos.setCurrentWidget(self.ui.page_actualizar_alumno)

        # 🔍 Maestros
        elif "alta maestro" in texto:
            self.ui.btn_maestros.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_maestros)
            self.ui.stack_maestros.setCurrentWidget(self.ui.page_alta_maestro)
        elif "baja maestro" in texto:
            self.ui.btn_maestros.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_maestros)
            self.ui.stack_maestros.setCurrentWidget(self.ui.page_baja_maestro)
        elif "actualizar maestro" in texto:
            self.ui.btn_maestros.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_maestros)
            self.ui.stack_maestros.setCurrentWidget(self.ui.page_actualizar_maestro)

        # 🔍 Materias
        elif "alta materia" in texto:
            self.ui.btn_materias.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_materias)
            self.ui.stack_materias.setCurrentWidget(self.ui.page_alta_materia)
        elif "baja materia" in texto:
            self.ui.btn_materias.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_materias)
            self.ui.stack_materias.setCurrentWidget(self.ui.page_baja_materia_m)
        elif "actualizar materia" in texto:
            self.ui.btn_materias.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_materias)
            self.ui.stack_materias.setCurrentWidget(self.ui.page_actualizar_materia)

        # 🔍 Documentos
        elif "subir documento" in texto or "documento" in texto:
            self.ui.btn_documentos.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_documentos)
            self.ui.stack_documentos.setCurrentWidget(self.ui.page_alta_documento)
        elif "validar documento" in texto:
            self.ui.btn_documentos.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_documentos)
            self.ui.stack_documentos.setCurrentWidget(self.ui.page_validar_documento)
        elif "consultar documento" in texto:
            self.ui.btn_documentos.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_documentos)
            self.ui.stack_documentos.setCurrentWidget(self.ui.page_consultar_documento)

        # 🔍 Reportes
        elif "generar reporte" in texto or "reporte" in texto:
            self.ui.btn_reportes.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_reportes)
            self.ui.stack_reportes.setCurrentWidget(self.ui.page_generar_reporte)

        # 🔍 Acerca de
        elif "acerca" in texto or "rgv" in texto:
            self.ui.btn_acercade.setChecked(True)
            self.ui.contendor_contenido.setCurrentWidget(self.ui.pagina_acercade)

        else:
            print("⚠️ No se encontró ninguna coincidencia.")

    # ========================== limpiar datos: alumno
    def limpiar_campos_alta_alumno(self):
        self.ui.input_nombre_alta.clear()
        self.ui.input_ap_paterno_alta.clear()
        self.ui.input_ap_materno_alta.clear()
        self.ui.input_fecha_nacimiento_alta.setDate(QtCore.QDate.currentDate())
        self.ui.input_direccion_alta.clear()
        self.ui.input_correo_alta.clear()
        self.ui.input_matricula_alta.clear()
        self.ui.combo_periodo_ingreso.setCurrentIndex(0)
        self.ui.check_activo_alta.setChecked(False)

    def dar_alta_alumno(self):
        nombre = self.ui.input_nombre_alta.text().strip().upper()
        apellido_paterno = self.ui.input_ap_paterno_alta.text().strip().upper()
        apellido_materno = self.ui.input_ap_materno_alta.text().strip().upper()
        fecha_nacimiento_qdate = self.ui.input_fecha_nacimiento_alta.date()
        fecha_nacimiento = fecha_nacimiento_qdate.toString("yyyy-MM-dd")
        direccion = self.ui.input_direccion_alta.text().strip().upper()
        correo = self.ui.input_correo_alta.text().strip().lower()
        matricula = self.ui.input_matricula_alta.text().strip().upper()
        periodo_ingreso = self.ui.combo_periodo_ingreso.currentText()
        activo = self.ui.check_activo_alta.isChecked()

        # Validación básica
        if not all(
            [
                nombre,
                apellido_paterno,
                apellido_materno,
                fecha_nacimiento,
                direccion,
                correo,
                matricula,
                periodo_ingreso,
            ]
        ):
            QtWidgets.QMessageBox.warning(
                self,
                "Campos incompletos",
                "Por favor, llena todos los campos antes de guardar.",
            )
            return

        datos_alumno = {
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion,
            "correo": correo,
            "matricula": matricula,
            "periodo_ingreso": periodo_ingreso,
            "activo": activo,
        }

        exito = insertar_registro("alumnos", datos_alumno, connect_db)

        if exito:
            QtWidgets.QMessageBox.information(
                self, "Éxito", "Alumno registrado correctamente."
            )
            self.limpiar_campos_alta_alumno()
        else:
            QtWidgets.QMessageBox.critical(
                self, "Error", "No se pudo registrar al alumno."
            )

    # combo baja
    def actualizar_combo_baja(self):
        texto = self.ui.input_buscar_baja.text().strip().upper()

        if not texto:
            self.ui.combo_baja_alumno.clear()
            return

        try:
            conexion = connect_db()
            cursor = conexion.cursor()
            query = """
                SELECT matricula, nombre, apellido_paterno, apellido_materno
                FROM alumnos
                WHERE
                    activo = TRUE AND (
                        matricula LIKE %s OR
                        nombre LIKE %s OR
                        apellido_paterno LIKE %s OR
                        apellido_materno LIKE %s
                    )
            """
            valores = (f"%{texto}%", f"%{texto}%", f"%{texto}%", f"%{texto}%")
            cursor.execute(query, valores)
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()

            self.ui.combo_baja_alumno.clear()
            for alumno in resultados:
                matricula = alumno[0]
                nombre = alumno[1]
                ap_paterno = alumno[2]
                ap_materno = alumno[3]

                nombre_completo = f"{nombre} {ap_paterno} {ap_materno}"
                etiqueta = f"{matricula} - {nombre_completo}"
                self.ui.combo_baja_alumno.addItem(etiqueta, matricula)

        except Exception as e:
            print("❌ Error al buscar alumnos:", e)

    # ========= Dar de baja alumno
    def dar_baja_alumno(self):
        criterio = self.ui.combo_baja_alumno.currentData()
        print("🧪 Matrícula seleccionada:", criterio)

        if not criterio:
            QtWidgets.QMessageBox.warning(
                self, "Campo vacío", "Ingresa nombre o matrícula."
            )
            return

        from data_access.insertar_datos_dao import (
            actualizar_campo,
            obtener_registro_por_campo,
        )

        alumno = obtener_registro_por_campo(
            "alumnos", "matricula", criterio, connect_db
        )

        if alumno is None:
            QtWidgets.QMessageBox.critical(
                self, "No encontrado", "No se encontró al alumno."
            )
            return

        if not alumno["activo"]:
            QtWidgets.QMessageBox.information(
                self, "Ya inactivo", "Este alumno ya está dado de baja."
            )
            return

        confirmacion = QtWidgets.QMessageBox.question(
            self,
            "Confirmar baja",
            f"¿Estás seguro de que deseas dar de baja a '{alumno['nombre']} {alumno['apellido_paterno']}'?",
            QtWidgets.QMessageBox.StandardButton.Yes
            | QtWidgets.QMessageBox.StandardButton.No,
        )

        if confirmacion == QtWidgets.QMessageBox.StandardButton.Yes:
            exito = actualizar_campo(
                tabla="alumnos",
                campo_objetivo="activo",
                nuevo_valor=False,
                campo_condicion="matricula",
                valor_condicion=criterio,
                connect_func=connect_db,
            )

            if exito:
                QtWidgets.QMessageBox.information(
                    self, "Éxito", "Alumno dado de baja correctamente."
                )
                self.ui.input_buscar_baja.clear()
            else:
                QtWidgets.QMessageBox.critical(
                    self, "Error", "No se pudo dar de baja al alumno."
                )

    # mostrar información de la baja
    def mostrar_info_baja(self):
        matricula = self.ui.combo_baja_alumno.currentData()
        if not matricula:
            self.ui.group_info_alumno.hide()
            return

        from data_access.insertar_datos_dao import obtener_registro_por_campo

        alumno = obtener_registro_por_campo(
            "alumnos", "matricula", matricula, connect_db
        )

        if alumno:
            self.ui.label_info_matricula.setText(f"Matrícula: {alumno['matricula']}")
            self.ui.label_info_nombre.setText(
                f"Nombre: {alumno['nombre']} {alumno['apellido_paterno']} {alumno['apellido_materno']}"
            )
            self.ui.label_info_direccion.setText(f"Dirección: {alumno['direccion']}")
            self.ui.label_info_correo.setText(f"Correo: {alumno['correo']}")
            self.ui.group_info_alumno.show()
        else:
            self.ui.group_info_alumno.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ✅ Cargar QSS desde archivo
    with open("./qss/estilos.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
