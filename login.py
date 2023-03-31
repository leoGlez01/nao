import sys, fondo_log
from PyQt5 import QtCore, QtGui, QtWidgets
from conexionA import *


class Registrar(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(590, 600)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.wid_general = QtWidgets.QWidget(Form)
        self.wid_general.setGeometry(QtCore.QRect(30, 20, 501, 561))
        self.wid_general.setStyleSheet("QPushButton#boton_entrar{\n"
"border:2px solid rgb(40,180,135);\n"
"color:rgba(255,255,255,230);\n"
"border-radius:20px;\n"
"}\n"
"QPushButton#boton_entrar:hover{\n"
"background-color:rgb(40,180,135);\n"
"color:rgb(0,0,0);\n"
"}\n"
"QPushButton#boton_cerrar{\n"
"background-color:rgba(0,0,0,0);\n"
"color:rgb(40,180,135);\n"
"border:none;\n"
"}\n"
"QPushButton#boton_cerrar:hover{\n"
"color:rgb(255,0,0);\n"
"}\n"
"")
        self.wid_general.setObjectName("wid_general")
        self.label_fondo = QtWidgets.QLabel(self.wid_general)
        self.label_fondo.setGeometry(QtCore.QRect(20, 30, 441, 501))
        self.label_fondo.setStyleSheet("border-image: url(:/fondo/imagenes/logo1.jpeg);\n"
"border-radius:20px;")
        self.label_fondo.setText("")
        self.label_fondo.setObjectName("label_fondo")
        self.label_fondo2 = QtWidgets.QLabel(self.wid_general)
        self.label_fondo2.setGeometry(QtCore.QRect(40, 40, 411, 481))
        self.label_fondo2.setStyleSheet("background-color:rgba(0,0,0,0.7);\n"
"border-radius:20px;")
        self.label_fondo2.setText("")
        self.label_fondo2.setObjectName("label_fondo2")
        self.label_contenido = QtWidgets.QLabel(self.wid_general)
        self.label_contenido.setGeometry(QtCore.QRect(50, 79, 380, 441))
        self.label_contenido.setStyleSheet("background-color:rgba(0,0,0,0.1);\n"
"border-radius:15px;")
        self.label_contenido.setObjectName("label_contenido")
        self.titulo = QtWidgets.QLabel(self.wid_general)
        self.titulo.setGeometry(QtCore.QRect(120, 80, 241, 51))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color:rgb(40,180,135);\n"
"font:Harrington;")
        self.titulo.setObjectName("titulo")
        self.entry_usuario = QtWidgets.QLineEdit(self.wid_general)
        self.entry_usuario.setGeometry(QtCore.QRect(120, 180, 241, 41))
        self.entry_usuario.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(40,180,135);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:1px;")
        self.entry_usuario.setObjectName("entry_usuario")
        self.entry_contra = QtWidgets.QLineEdit(self.wid_general)
        self.entry_contra.setGeometry(QtCore.QRect(120, 290, 241, 41))
        self.entry_contra.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(40,180,135);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:1px;")
        self.entry_contra.setObjectName("entry_contra")
        self.boton_entrar = QtWidgets.QPushButton(self.wid_general)
        self.boton_entrar.setGeometry(QtCore.QRect(120, 400, 231, 41))
        self.boton_entrar.setObjectName("boton_entrar")
        self.boton_entrar.clicked.connect(lambda: self.crear())
        self.boton_cerrar = QtWidgets.QPushButton(self.wid_general)
        self.boton_cerrar.setGeometry(QtCore.QRect(420, 40, 21, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.boton_cerrar.setFont(font)
        self.boton_cerrar.setObjectName("boton_cerrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_contenido.setText(_translate("Form", "TextLabel"))
        self.titulo.setText(_translate("Form", "Bienvenidos a Bordo!!!"))
        self.entry_usuario.setPlaceholderText(_translate("Form", "   Nombre de Usuario"))
        self.entry_contra.setPlaceholderText(_translate("Form", "   Contraseña"))
        self.boton_entrar.setText(_translate("Form", "ENTRAR"))
        self.boton_cerrar.setText(_translate("Form", "X"))

    def crear(self):
        self.db = Comunicacion()
        self.db.crearMesas() 


# if __name__ == "__main__":
#         app = QtWidgets.QApplication(sys.argv)
#         Form = QtWidgets.QWidget()
#         mi_app = Registrar()
#         mi_app.setupUi(Form)
#         Form.show()
#         sys.exit(app.exec_())
