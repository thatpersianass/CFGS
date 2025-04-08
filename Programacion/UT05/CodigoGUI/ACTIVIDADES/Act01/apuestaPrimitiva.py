# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apuestaPrimitiva.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import random

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_formEtiqueta(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        font = QFont()
        font.setPointSize(24)
        
        Form.resize(791, 480)
        self.lbl_titulo = QLabel(Form)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(240, 60, 301, 31))
        self.lbl_titulo.setFont(font)
        
        self.rad_auto = QRadioButton(Form)
        self.rad_auto.setObjectName(u"rad_auto")
        self.rad_auto.setEnabled(False)
        self.rad_auto.setGeometry(QRect(210, 140, 82, 17))  
        self.rad_auto.clicked.connect(self.numAuto)
        
        self.rad_manual = QRadioButton(Form)
        self.rad_manual.setObjectName(u"rad_manual")
        self.rad_manual.setEnabled(False)
        self.rad_manual.setGeometry(QRect(210, 200, 82, 17))
        self.rad_manual.clicked.connect(self.numManual)
        
        self.text_num1 = QPlainTextEdit(Form)
        self.text_num1.setObjectName(u"text_num1")
        self.text_num1.setEnabled(False)
        self.text_num1.setGeometry(QRect(320, 130, 71, 41))
        
        self.text_num2 = QPlainTextEdit(Form)
        self.text_num2.setObjectName(u"text_num2")
        self.text_num2.setEnabled(False)
        self.text_num2.setGeometry(QRect(410, 130, 71, 41))
        
        self.text_num3 = QPlainTextEdit(Form)
        self.text_num3.setObjectName(u"text_num3")
        self.text_num3.setEnabled(False)
        self.text_num3.setGeometry(QRect(500, 130, 71, 41))
        
        self.text_num4 = QPlainTextEdit(Form)
        self.text_num4.setObjectName(u"text_num4")
        self.text_num4.setEnabled(False)
        self.text_num4.setGeometry(QRect(320, 190, 71, 41))
        
        self.text_num5 = QPlainTextEdit(Form)
        self.text_num5.setObjectName(u"text_num5")
        self.text_num5.setEnabled(False)
        self.text_num5.setGeometry(QRect(410, 190, 71, 41))

        self.text_num6 = QPlainTextEdit(Form)
        self.text_num6.setObjectName(u"text_num6")
        self.text_num6.setEnabled(False)
        self.text_num6.setGeometry(QRect(500, 190, 71, 41))
        
        self.btn_crear = QPushButton(Form)
        self.btn_crear.setObjectName(u"btn_crear")
        self.btn_crear.setGeometry(QRect(220, 280, 100, 51))
        self.btn_crear.clicked.connect(self.btnCrear01)
        
        self.btn_validar = QPushButton(Form)
        self.btn_validar.setObjectName(u"btn_validar")
        self.btn_validar.setEnabled(False)
        self.btn_validar.setGeometry(QRect(340, 280, 100, 51))
        
        self.btn_cancelar = QPushButton(Form)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setEnabled(False)
        self.btn_cancelar.setGeometry(QRect(460, 280, 100, 51))
        self.btn_cancelar.clicked.connect(self.btnCancelar)
        
        self.btn_mostrar = QPushButton(Form)
        self.btn_mostrar.setObjectName(u"btn_mostrar")
        self.btn_mostrar.setGeometry(QRect(270, 350, 100, 51))
        
        self.btn_anterior = QPushButton(Form)
        self.btn_anterior.setObjectName(u"btn_anterior")
        self.btn_anterior.setEnabled(False)
        self.btn_anterior.setGeometry(QRect(390, 350, 61, 51))
        
        self.btn_siguiente = QPushButton(Form)
        self.btn_siguiente.setObjectName(u"btn_siguiente")
        self.btn_siguiente.setEnabled(False)
        self.btn_siguiente.setGeometry(QRect(450, 350, 61, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    def btnCrear01(self):
        '''
        Activa o desactiva la interacción con el resto de la interfaz
        '''
        if self.rad_auto.isEnabled() == False:
            self.rad_auto.setEnabled(True)
            self.rad_auto.setChecked(True)
            self.rad_manual.setEnabled(True)
            self.btn_validar.setEnabled(True)
            self.btn_cancelar.setEnabled(True)
            self.btn_anterior.setEnabled(True)
            self.btn_siguiente.setEnabled(True)
            self.btn_crear.setEnabled(False)
            self.numAuto()
        
    def btnCancelar(self):
        self.rad_auto.setEnabled(False)
        self.rad_manual.setEnabled(False)
        self.text_num1.setEnabled(False)
        self.text_num2.setEnabled(False)
        self.text_num3.setEnabled(False)
        self.text_num4.setEnabled(False)
        self.text_num5.setEnabled(False)
        self.text_num6.setEnabled(False)
        self.btn_validar.setEnabled(False)
        self.btn_cancelar.setEnabled(False)
        self.btn_anterior.setEnabled(False)
        self.btn_siguiente.setEnabled(False)
        self.btn_crear.setEnabled(True)
        self.limpiarTexto()
    
    def limpiarTexto(self):
        for text_edit in self.numAuto_getCampos():
                text_edit.clear()
    
    def numManual(self):
        self.limpiarTexto()
        self.text_num1.setEnabled(True)
        self.text_num2.setEnabled(True)
        self.text_num3.setEnabled(True)
        self.text_num4.setEnabled(True)
        self.text_num5.setEnabled(True)
        self.text_num6.setEnabled(True)
        
    def numAuto(self):
        self.text_num1.setEnabled(False)
        self.text_num2.setEnabled(False)
        self.text_num3.setEnabled(False)
        self.text_num4.setEnabled(False)
        self.text_num5.setEnabled(False)
        self.text_num6.setEnabled(False)
        numeros = random.sample(range(1,50),6)
        for i, text_edit in enumerate(self.numAuto_getCampos()):
            text_edit.setPlainText(str(numeros[i]))
            
    def numAuto_getCampos(self):
        return [self.text_num1,self.text_num2,self.text_num3,self.text_num4,self.text_num5,self.text_num6]
            
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_titulo.setText(QCoreApplication.translate("Form", u"APUESTA PRIMITIVA", None))
        self.rad_auto.setText(QCoreApplication.translate("Form", u"Autom\u00e1tico", None))
        self.rad_manual.setText(QCoreApplication.translate("Form", u"Manual", None))
        self.btn_crear.setText(QCoreApplication.translate("Form", u"CREAR", None))
        self.btn_validar.setText(QCoreApplication.translate("Form", u"VALIDAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Form", u"CANCELAR", None))
        self.btn_mostrar.setText(QCoreApplication.translate("Form", u"MOSTRAR", None))
        self.btn_anterior.setText(QCoreApplication.translate("Form", u"<", None))
        self.btn_siguiente.setText(QCoreApplication.translate("Form", u">", None))
    # retranslateUi