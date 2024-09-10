# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaNuevoCliente.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_ventanaNuevoCliente(object):
    def setupUi(self, ventanaNuevoCliente):
        if not ventanaNuevoCliente.objectName():
            ventanaNuevoCliente.setObjectName(u"ventanaNuevoCliente")
        ventanaNuevoCliente.resize(772, 537)
        self.label = QLabel(ventanaNuevoCliente)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 30, 311, 81))
        font = QFont()
        font.setFamilies([u"Noto Sans Cond"])
        font.setPointSize(22)
        self.label.setFont(font)
        self.label_2 = QLabel(ventanaNuevoCliente)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 200, 55, 16))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(ventanaNuevoCliente)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 240, 191, 31))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(ventanaNuevoCliente)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 290, 111, 21))
        self.label_4.setFont(font1)
        self.txtid = QLineEdit(ventanaNuevoCliente)
        self.txtid.setObjectName(u"txtid")
        self.txtid.setGeometry(QRect(270, 200, 113, 22))
        self.txtNombre = QLineEdit(ventanaNuevoCliente)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(270, 250, 471, 22))
        self.txtDomicilio = QLineEdit(ventanaNuevoCliente)
        self.txtDomicilio.setObjectName(u"txtDomicilio")
        self.txtDomicilio.setGeometry(QRect(270, 300, 471, 22))
        self.btnGuardar = QPushButton(ventanaNuevoCliente)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(290, 390, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"Alef"])
        font2.setPointSize(14)
        self.btnGuardar.setFont(font2)
        self.btnCancelar = QPushButton(ventanaNuevoCliente)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setGeometry(QRect(470, 390, 111, 41))
        self.btnCancelar.setFont(font2)

        self.retranslateUi(ventanaNuevoCliente)

        QMetaObject.connectSlotsByName(ventanaNuevoCliente)
    # setupUi

    def retranslateUi(self, ventanaNuevoCliente):
        ventanaNuevoCliente.setWindowTitle(QCoreApplication.translate("ventanaNuevoCliente", u"Sistema BANKITO - Ingreso de Nuevos clientes", None))
        self.label.setText(QCoreApplication.translate("ventanaNuevoCliente", u"Sistema Bankito ", None))
        self.label_2.setText(QCoreApplication.translate("ventanaNuevoCliente", u"Id", None))
        self.label_3.setText(QCoreApplication.translate("ventanaNuevoCliente", u"Nombre y Apellido", None))
        self.label_4.setText(QCoreApplication.translate("ventanaNuevoCliente", u"Direccion", None))
        self.btnGuardar.setText(QCoreApplication.translate("ventanaNuevoCliente", u"Guardar", None))
        self.btnCancelar.setText(QCoreApplication.translate("ventanaNuevoCliente", u"Cancelar", None))
    # retranslateUi

