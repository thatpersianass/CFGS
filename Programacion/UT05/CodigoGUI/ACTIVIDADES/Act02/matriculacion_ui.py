# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'matriculacion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QIntValidator)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget,QMessageBox)

class Ui_Matriculacion(object):
    def setupUi(self, Matriculacion):
        if not Matriculacion.objectName():
            Matriculacion.setObjectName(u"Matriculacion")
        Matriculacion.resize(631, 419)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Matriculacion.sizePolicy().hasHeightForWidth())
        self.validar = QIntValidator(self)
        
        Matriculacion.setSizePolicy(sizePolicy)
        Matriculacion.setMinimumSize(QSize(631, 419))
        Matriculacion.setMaximumSize(QSize(631, 419))
        
        self.lnEdit_Matricula = QLineEdit(Matriculacion)
        self.lnEdit_Matricula.setObjectName(u"lnEdit_Matricula")
        self.lnEdit_Matricula.setEnabled(True)
        self.lnEdit_Matricula.setGeometry(QRect(110, 48, 171, 20))
        self.lnEdit_Matricula.setValidator(self.validar)
        
        self.lnEdit_Nombre = QLineEdit(Matriculacion)
        self.lnEdit_Nombre.setObjectName(u"lnEdit_Nombre")
        self.lnEdit_Nombre.setEnabled(False)
        self.lnEdit_Nombre.setGeometry(QRect(110, 108, 241, 20))
        
        self.lnEdit_Apellidos = QLineEdit(Matriculacion)
        self.lnEdit_Apellidos.setObjectName(u"lnEdit_Apellidos")
        self.lnEdit_Apellidos.setEnabled(False)
        self.lnEdit_Apellidos.setGeometry(QRect(110, 168, 241, 20))
        
        self.lnEdit_Curso = QLineEdit(Matriculacion)
        self.lnEdit_Curso.setObjectName(u"lnEdit_Curso")
        self.lnEdit_Curso.setEnabled(False)
        self.lnEdit_Curso.setGeometry(QRect(110, 228, 241, 20))
        self.lnEdit_Curso.setValidator(self.validar)
        
        self.lnEdit_Ciclo = QLineEdit(Matriculacion)
        self.lnEdit_Ciclo.setObjectName(u"lnEdit_Ciclo")
        self.lnEdit_Ciclo.setEnabled(False)
        self.lnEdit_Ciclo.setGeometry(QRect(110, 288, 241, 20))
        
        self.lbl_Matricula = QLabel(Matriculacion)
        self.lbl_Matricula.setObjectName(u"lbl_Matricula")
        self.lbl_Matricula.setGeometry(QRect(30, 51, 71, 16))
        
        self.lbl_Nombre = QLabel(Matriculacion)
        self.lbl_Nombre.setObjectName(u"lbl_Nombre")
        self.lbl_Nombre.setGeometry(QRect(60, 111, 47, 13))
        
        self.lbl_Apellidos = QLabel(Matriculacion)
        self.lbl_Apellidos.setObjectName(u"lbl_Apellidos")
        self.lbl_Apellidos.setGeometry(QRect(60, 170, 47, 13))
        
        self.lbl_Curso = QLabel(Matriculacion)
        self.lbl_Curso.setObjectName(u"lbl_Curso")
        self.lbl_Curso.setGeometry(QRect(70, 230, 47, 13))
        
        self.lbl_Ciclo = QLabel(Matriculacion)
        self.lbl_Ciclo.setObjectName(u"lbl_Ciclo")
        self.lbl_Ciclo.setGeometry(QRect(70, 290, 47, 13))
        
        self.verticalLayoutWidget = QWidget(Matriculacion)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setDisabled(False)
        self.verticalLayoutWidget.setGeometry(QRect(410, 90, 160, 80))
        
        self.vertLay_Sexo = QVBoxLayout(self.verticalLayoutWidget)
        self.vertLay_Sexo.setObjectName(u"vertLay_Sexo")
        self.vertLay_Sexo.setContentsMargins(10, 0, 0, 0)
        
        self.rad_Masculino = QRadioButton(self.verticalLayoutWidget)
        self.rad_Masculino.setObjectName(u"rad_Masculino")
        self.rad_Masculino.setEnabled(False)

        self.vertLay_Sexo.addWidget(self.rad_Masculino)

        self.rad_Femenino = QRadioButton(self.verticalLayoutWidget)
        self.rad_Femenino.setObjectName(u"rad_Femenino")
        self.rad_Femenino.setEnabled(False)

        self.vertLay_Sexo.addWidget(self.rad_Femenino)

        self.verticalLayoutWidget_2 = QWidget(Matriculacion)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setDisabled(False)
        self.verticalLayoutWidget_2.setGeometry(QRect(410, 230, 160, 80))
        
        self.vertLay_Situacion = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vertLay_Situacion.setObjectName(u"vertLay_Situacion")
        self.vertLay_Situacion.setContentsMargins(10, 0, 0, 0)
        
        self.check_Estudia = QCheckBox(self.verticalLayoutWidget_2)
        self.check_Estudia.setObjectName(u"check_Estudia")
        self.check_Estudia.setEnabled(False)

        self.vertLay_Situacion.addWidget(self.check_Estudia)

        self.check_Trabaja = QCheckBox(self.verticalLayoutWidget_2)
        self.check_Trabaja.setObjectName(u"check_Trabaja")
        self.check_Trabaja.setEnabled(False)

        self.vertLay_Situacion.addWidget(self.check_Trabaja)

        self.lbl_Sexo = QLabel(Matriculacion)
        self.lbl_Sexo.setObjectName(u"lbl_Sexo")
        self.lbl_Sexo.setGeometry(QRect(410, 70, 71, 16))
        
        self.lbl_Aviso = QLabel(Matriculacion)
        self.lbl_Aviso.setObjectName(u"lbl_Aviso")
        self.lbl_Aviso.setGeometry(QRect(70, 325, 600, 16))
        self.lbl_Aviso.setVisible(False)
        
        self.lbl_Situacion = QLabel(Matriculacion)
        self.lbl_Situacion.setObjectName(u"lbl_Situacion")
        self.lbl_Situacion.setGeometry(QRect(410, 210, 71, 16))
        
        self.btn_Modificar = QPushButton(Matriculacion)
        self.btn_Modificar.setObjectName(u"btn_Modificar")
        self.btn_Modificar.setEnabled(False)
        self.btn_Modificar.setGeometry(QRect(270, 360, 75, 23))
        self.btn_Modificar.clicked.connect(self.btnModificar)
        
        self.btn_Buscar = QPushButton(Matriculacion)
        self.btn_Buscar.setObjectName(u"btn_Buscar")
        self.btn_Buscar.setEnabled(True)
        self.btn_Buscar.setGeometry(QRect(180, 360, 75, 23))
        self.btn_Buscar.clicked.connect(self.verificarMatricula)
        
        self.btn_Borrar = QPushButton(Matriculacion)
        self.btn_Borrar.setObjectName(u"btn_Borrar")
        self.btn_Borrar.setEnabled(False)
        self.btn_Borrar.setGeometry(QRect(360, 360, 75, 23))
        self.btn_Borrar.clicked.connect(self.btnBorrar)

        self.retranslateUi(Matriculacion)

        QMetaObject.connectSlotsByName(Matriculacion)
    # setupUi


    def retranslateUi(self, Matriculacion):
        Matriculacion.setWindowTitle(QCoreApplication.translate("Matriculacion", u"Matriculacion", None))
        self.lbl_Matricula.setText(QCoreApplication.translate("Matriculacion", u"Nro. Matricula:", None))
        self.lbl_Nombre.setText(QCoreApplication.translate("Matriculacion", u"Nombre:", None))
        self.lbl_Apellidos.setText(QCoreApplication.translate("Matriculacion", u"Apellidos:", None))
        self.lbl_Curso.setText(QCoreApplication.translate("Matriculacion", u"Curso:", None))
        self.lbl_Ciclo.setText(QCoreApplication.translate("Matriculacion", u"Ciclo:", None))
        self.rad_Masculino.setText(QCoreApplication.translate("Matriculacion", u"Hombre", None))
        self.rad_Femenino.setText(QCoreApplication.translate("Matriculacion", u"Mujer", None))
        self.check_Estudia.setText(QCoreApplication.translate("Matriculacion", u"Estudia", None))
        self.check_Trabaja.setText(QCoreApplication.translate("Matriculacion", u"Trabaja", None))
        self.lbl_Sexo.setText(QCoreApplication.translate("Matriculacion", u"Sexo:", None))
        self.lbl_Aviso.setText(QCoreApplication.translate("Matriculacion", u"AVISO: Si no desea modificar la matricula, presione el boton Modificar sin cambiar ningun dato", None))
        self.lbl_Situacion.setText(QCoreApplication.translate("Matriculacion", u"Situaci\u00f3n:", None))
        self.btn_Modificar.setText(QCoreApplication.translate("Matriculacion", u"Modificar", None))
        self.btn_Borrar.setText(QCoreApplication.translate("Matriculacion", u"Borrar", None))
        self.btn_Buscar.setText(QCoreApplication.translate("Matriculacion", u"Buscar", None))
    # retranslateUi

