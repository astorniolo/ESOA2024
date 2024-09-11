# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaListado2.ui'
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
from PySide6.QtWidgets import (QApplication, QColumnView, QComboBox, QDial,
    QDialog, QHeaderView, QLCDNumber, QLabel,
    QListView, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_VentanaListadoDeClientes(object):
    def setupUi(self, VentanaListadoDeClientes):
        if not VentanaListadoDeClientes.objectName():
            VentanaListadoDeClientes.setObjectName(u"VentanaListadoDeClientes")
        self.tableView = QTableView(VentanaListadoDeClientes)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(100, 100, 591, 192))
        self.label = QLabel(VentanaListadoDeClientes)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 130, 101, 16))
        self.dial = QDial(VentanaListadoDeClientes)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(360, 590, 50, 64))
        self.lcdNumber = QLCDNumber(VentanaListadoDeClientes)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(490, 520, 181, 41))
        self.columnView = QColumnView(VentanaListadoDeClientes)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setGeometry(QRect(100, 310, 256, 192))
        self.label_3 = QLabel(VentanaListadoDeClientes)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 320, 101, 16))
        self.listView = QListView(VentanaListadoDeClientes)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(420, 310, 256, 192))
        self.label_4 = QLabel(VentanaListadoDeClientes)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 320, 101, 16))
        self.pushButton_4 = QPushButton(VentanaListadoDeClientes)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(120, 10, 371, 28))
        self.pushButton_5 = QPushButton(VentanaListadoDeClientes)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(120, 50, 371, 28))
        self.comboBox = QComboBox(VentanaListadoDeClientes)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 540, 221, 22))
        self.valorDIAL = QLabel(VentanaListadoDeClientes)
        self.valorDIAL.setObjectName(u"valorDIAL")
        self.valorDIAL.setGeometry(QRect(100, 610, 161, 16))
        font = QFont()
        font.setFamilies([u"Viner Hand ITC"])
        font.setPointSize(12)
        self.valorDIAL.setFont(font)

        self.retranslateUi(VentanaListadoDeClientes)

        QMetaObject.connectSlotsByName(VentanaListadoDeClientes)
    # setupUi

    def retranslateUi(self, VentanaListadoDeClientes):
        VentanaListadoDeClientes.setWindowTitle(QCoreApplication.translate("VentanaListadoDeClientes", u"Listado de Clientes  ", None))
        self.label.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"table view", None))
        self.label_3.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"column view", None))
        self.label_4.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"list view", None))
        self.pushButton_4.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"PushButton", None))
        self.valorDIAL.setText(QCoreApplication.translate("VentanaListadoDeClientes", u"TextLabel", None))
    # retranslateUi

