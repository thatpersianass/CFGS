# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '02_Label.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget, QPushButton)

class Ui_formEtiqueta(object):
    def setupUi(self, formEtiqueta):
        if not formEtiqueta.objectName():
            formEtiqueta.setObjectName(u"formEtiqueta")
            
        formEtiqueta.resize(400, 300)
        formEtiqueta.setWindowTitle(QCoreApplication.translate("formEtiqueta", u"Formulario de etiqueta", None))
        
        self.lbl01 = QLabel(formEtiqueta)
        self.lbl01.setObjectName(u"lbl01")
        self.lbl01.setGeometry(QRect(110, 70, 120, 20))
        self.lbl01.setText(QCoreApplication.translate("formEtiqueta", u"Etiqueta01", None))
        
        self.lbl02 = QLabel(formEtiqueta)
        self.lbl02.setObjectName(u"lbl02")
        self.lbl02.setGeometry(QRect(110, 110, 120, 20))
        self.lbl02.setText(QCoreApplication.translate("formEtiqueta", u"TextLabel", None))
        
        Font = QFont()
        Font.setPointSize(10)
        self.lbl03 = QLabel(formEtiqueta)
        self.lbl03.setObjectName(u"lbl03")
        self.lbl03.setGeometry(QRect(110, 150, 120, 20))
        self.lbl03.setText(QCoreApplication.translate("formEtiqueta", u"Etiqueta03", None))
        self.lbl03.setFont(Font)
        
        self.lbl04 = QLabel(formEtiqueta)
        self.lbl04.setObjectName(u"lbl04")
        self.lbl04.setGeometry(QRect(110, 190, 120, 20))
        self.lbl04.setText(QCoreApplication.translate("formEtiqueta", u"TextLabel", None))
        self.lbl04.setVisible(False)
        
        self.btn01 = QPushButton(formEtiqueta)
        self.btn01.setObjectName(u"Mostrar")
        self.btn01.setGeometry(120,270,80,30)
        self.btn01.setText("Mostrar")
        self.btn01.clicked.connect(self.clicBtn01)
        
        QMetaObject.connectSlotsByName(formEtiqueta)
            
    # setupUi
    def clicBtn01(self):
        '''
            Atiende señal de clic btn01 y cambia lbl04
        '''
        print('Ha hecho clic')
        if self.lbl04.isVisible():
            self.lbl04.setVisible(False)
            self.btn01.setText("Mostrar")
        else:
            self.lbl04.setVisible(True)
            self.btn01.setText("Ocultar")