# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaListado.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_VentanaListadoDeClientes(object):
    def setupUi(self, VentanaListadoDeClientes):
        if not VentanaListadoDeClientes.objectName():
            VentanaListadoDeClientes.setObjectName(u"VentanaListadoDeClientes")
        VentanaListadoDeClientes.resize(904, 397)
        self.tablaClientes = QTableWidget(VentanaListadoDeClientes)
        self.tablaClientes.setObjectName(u"tablaClientes")
        self.tablaClientes.setGeometry(QRect(90, 20, 441, 231))
        self.label_2 = QLabel(VentanaListadoDeClientes)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 101, 16))
        self.pushButton = QPushButton(VentanaListadoDeClientes)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 60, 93, 28))
        self.pushButton_2 = QPushButton(VentanaListadoDeClientes)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 110, 93, 28))
        self.pushButton_3 = QPushButton(VentanaListadoDeClientes)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(610, 160, 93, 28))

        self.retranslateUi(VentanaListadoDeClientes)

        QMetaObject.connectSlotsByName(VentanaListadoDeClientes)
    # setupUi

    def retranslateUi(self, VentanaListadoDeClientes):
        VentanaListadoDeClientes.setWindowTitle(QCoreApplication.translate("VentanaListadoDeClientes", u"Listado de Clientes  ", None))
        self.label_2.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"table widgets", None))
        self.pushButton.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"PushButton", None))
    # retranslateUi

