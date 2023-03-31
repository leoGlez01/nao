from inicio import *
from inventario import *
from login import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexionA import Comunicacion


# # ejecutable invntario
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mi_app = VentanaPrincipal()
#     mi_app.show()
#     sys.exit(app.exec_())


# # ejecutable de login
# if __name__ == "__main__":
#         app = QtWidgets.QApplication(sys.argv)
#         Form = QtWidgets.QWidget()
#         mi_app = Registrar()
#         mi_app.setupUi(Form)
#         Form.show()
#         sys.exit(app.exec_())


# #ejecutable pantalla de carga
# if __name__ == "__main__":
#         app = QtWidgets.QApplication(sys.argv)
#         Form = QtWidgets.QWidget()
#         mi_app = Inicio()
#         mi_app.setupUi(Form)
#         Form.show()
#         sys.exit(app.exec_())
