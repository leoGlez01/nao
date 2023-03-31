import sys, carga
from PyQt5 import QtCore, QtGui, QtWidgets


class Inicio(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(777, 588)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 50, 731, 501))
        self.widget.setObjectName("widget")
        self.foto_carga = QtWidgets.QLabel(self.widget)
        self.foto_carga.setGeometry(QtCore.QRect(60, 40, 631, 421))
        self.foto_carga.setStyleSheet("border-image: url(:/carga/imagenes/logo.jpeg);\n"
"border-radius:50px;")
        self.foto_carga.setText("")
        self.foto_carga.setObjectName("foto_carga")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

# if __name__ == "__main__":
#         app = QtWidgets.QApplication(sys.argv)
#         Form = QtWidgets.QWidget()
#         mi_app = Inicio()
#         mi_app.setupUi(Form)
#         Form.show()
#         sys.exit(app.exec_())
