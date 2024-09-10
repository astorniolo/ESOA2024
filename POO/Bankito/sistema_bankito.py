import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from capa_vista.VentanaPpal import *



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())