# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'line_edit.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 350)
        self.lnEditNombre = QLineEdit(Form)
        self.lnEditNombre.setObjectName(u"lnEditNombre")
        self.lnEditNombre.setEnabled(False)
        self.lnEditNombre.setGeometry(QRect(130, 60, 130, 20))
        self.lnEditNombre.focusInEvent()
        
        self.lnEditApellido = QLineEdit(Form)
        self.lnEditApellido.setObjectName(u"lnEditApellido")
        self.lnEditApellido.setEnabled(False)
        self.lnEditApellido.setGeometry(QRect(130, 120, 190, 20))
        
        self.lnEditDireccion = QLineEdit(Form)
        self.lnEditDireccion.setObjectName(u"lnEditDireccion")
        self.lnEditDireccion.setEnabled(False)
        self.lnEditDireccion.setGeometry(QRect(130, 180, 380, 20))
        
        self.lblnombre = QLabel(Form)
        self.lblnombre.setObjectName(u"lblnombre")
        self.lblnombre.setGeometry(QRect(60, 60, 47, 13))
        
        self.lblapellidos = QLabel(Form)
        self.lblapellidos.setObjectName(u"lblapellidos")
        self.lblapellidos.setGeometry(QRect(60, 120, 47, 13))
        
        self.lbldireccion = QLabel(Form)
        self.lbldireccion.setObjectName(u"lbldireccion")
        self.lbldireccion.setGeometry(QRect(60, 180, 47, 13))
        
        self.btnInsertar = QPushButton(Form)
        self.btnInsertar.setObjectName(u"btnInsertar")
        self.btnInsertar.setGeometry(QRect(60, 240, 75, 23))
        self.btnInsertar.clicked.connect(self.btnInsertarClic)
        
        self.btnGrabar = QPushButton(Form)
        self.btnGrabar.setObjectName(u"btnGrabar")
        self.btnGrabar.setEnabled(False)
        self.btnGrabar.setGeometry(QRect(150, 240, 75, 23))
        
        self.btnReset = QPushButton(Form)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setEnabled(False)
        self.btnReset.setGeometry(QRect(240, 240, 75, 23))
        
        self.txResumen01 = QTextEdit(Form)
        self.txResumen01.setObjectName(u"txResumen01")
        self.txResumen01.setEnabled(False)
        self.txResumen01.setGeometry(QRect(360, 60, 150, 100))
        
        self.txResumen02 = QTextEdit(Form)
        self.txResumen02.setObjectName(u"txResumen02")
        self.txResumen02.setEnabled(False)
        self.txResumen02.setGeometry(QRect(560, 60, 150, 100))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lnEditNombre.setText(QCoreApplication.translate("Form", u"Introduzca el Nombre...", None))
        self.lnEditApellido.setText(QCoreApplication.translate("Form", u"Introduzca el Apellido...", None))
        self.lnEditDireccion.setText(QCoreApplication.translate("Form", u"Introduzca la Direccion...", None))
        self.lblnombre.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.lblapellidos.setText(QCoreApplication.translate("Form", u"Apellidos", None))
        self.lbldireccion.setText(QCoreApplication.translate("Form", u"Direccion", None))
        self.btnInsertar.setText(QCoreApplication.translate("Form", u"Insertar", None))
        self.btnGrabar.setText(QCoreApplication.translate("Form", u"Grabar", None))
        self.btnReset.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

    def btnInsertarClic(self):
        if not self.lnEditNombre.isEnabled():
            self.lnEditNombre.setEnabled(True)
            self.lnEditApellido.setEnabled(True)
            self.lnEditDireccion.setEnabled(True)
            
            self.btnReset.setEnabled(True)
            
            self.txResumen01.setEnabled(True)
            self.txResumen02.setEnabled(True)
            
            self.btnInsertar.setText("Cancelar")
            
            self.lnEditNombre.setText(QCoreApplication.translate("Form", u"", None))
            self.lnEditApellido.setText(QCoreApplication.translate("Form", u"", None))
            self.lnEditDireccion.setText(QCoreApplication.translate("Form", u"", None))
        else:
            self.lnEditNombre.setEnabled(False)
            self.lnEditApellido.setEnabled(False)
            self.lnEditDireccion.setEnabled(False)
            
            self.btnReset.setEnabled(False)
            
            self.txResumen01.setEnabled(False)
            self.txResumen02.setEnabled(False)
            
            self.lnEditNombre.setText(QCoreApplication.translate("Form", u"Introduzca el Nombre...", None))
            self.lnEditApellido.setText(QCoreApplication.translate("Form", u"Introduzca el Apellido...", None))
            self.lnEditDireccion.setText(QCoreApplication.translate("Form", u"Introduzca la Direccion...", None))
            
            self.btnInsertar.setText("Insertar")