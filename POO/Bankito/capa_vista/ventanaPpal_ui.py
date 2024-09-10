# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaPpal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1105, 680)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-image: url(C:/workspace/python2024/POO/Bankito/imagenes/banco.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.actionNuevo_Cliente = QAction(MainWindow)
        self.actionNuevo_Cliente.setObjectName(u"actionNuevo_Cliente")
        self.actionActualizar_Cliente = QAction(MainWindow)
        self.actionActualizar_Cliente.setObjectName(u"actionActualizar_Cliente")
        self.actionBorrar_Cliente = QAction(MainWindow)
        self.actionBorrar_Cliente.setObjectName(u"actionBorrar_Cliente")
        self.actionBuscar_Cliente = QAction(MainWindow)
        self.actionBuscar_Cliente.setObjectName(u"actionBuscar_Cliente")
        self.actionListar_todos_los_clientes = QAction(MainWindow)
        self.actionListar_todos_los_clientes.setObjectName(u"actionListar_todos_los_clientes")
        self.actionNuevo_Prestamo = QAction(MainWindow)
        self.actionNuevo_Prestamo.setObjectName(u"actionNuevo_Prestamo")
        self.actionSALIR = QAction(MainWindow)
        self.actionSALIR.setObjectName(u"actionSALIR")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1105, 26))
        self.menuCliente = QMenu(self.menubar)
        self.menuCliente.setObjectName(u"menuCliente")
        self.menuCuenta = QMenu(self.menubar)
        self.menuCuenta.setObjectName(u"menuCuenta")
        self.menuPrestamo = QMenu(self.menubar)
        self.menuPrestamo.setObjectName(u"menuPrestamo")
        self.menuSalida = QMenu(self.menubar)
        self.menuSalida.setObjectName(u"menuSalida")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCliente.menuAction())
        self.menubar.addAction(self.menuCuenta.menuAction())
        self.menubar.addAction(self.menuPrestamo.menuAction())
        self.menubar.addAction(self.menuSalida.menuAction())
        self.menuCliente.addAction(self.actionNuevo_Cliente)
        self.menuCliente.addAction(self.actionActualizar_Cliente)
        self.menuCliente.addSeparator()
        self.menuCliente.addAction(self.actionBorrar_Cliente)
        self.menuCliente.addSeparator()
        self.menuCliente.addAction(self.actionBuscar_Cliente)
        self.menuCliente.addAction(self.actionListar_todos_los_clientes)
        self.menuPrestamo.addAction(self.actionNuevo_Prestamo)
        self.menuSalida.addAction(self.actionSALIR)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Control de Bankito", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"ventana de inicio", None))
#endif // QT_CONFIG(tooltip)
        self.actionNuevo_Cliente.setText(QCoreApplication.translate("MainWindow", u"Nuevo Cliente", None))
        self.actionActualizar_Cliente.setText(QCoreApplication.translate("MainWindow", u"Actualizar Cliente", None))
        self.actionBorrar_Cliente.setText(QCoreApplication.translate("MainWindow", u"Borrar Cliente", None))
        self.actionBuscar_Cliente.setText(QCoreApplication.translate("MainWindow", u"Buscar Cliente", None))
        self.actionListar_todos_los_clientes.setText(QCoreApplication.translate("MainWindow", u"Listar todos los clientes", None))
        self.actionNuevo_Prestamo.setText(QCoreApplication.translate("MainWindow", u"Nuevo Prestamo", None))
        self.actionSALIR.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.menuCliente.setTitle(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.menuCuenta.setTitle(QCoreApplication.translate("MainWindow", u"Cuenta", None))
        self.menuPrestamo.setTitle(QCoreApplication.translate("MainWindow", u"Prestamo", None))
        self.menuSalida.setTitle(QCoreApplication.translate("MainWindow", u"Salida", None))
    # retranslateUi

