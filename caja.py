import sys
from turtle import width 
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexionC import *


class Caja(QMainWindow):
    def __init__(self):
        super(Caja , self).__init__()
        loadUi('caja.ui', self)

        self.db = Conexion()
        self.entryBuscar.textChanged.connect(self.buscarMenu)

        # Menu lateral izquierdo
        self.botonMenu.clicked.connect(self.mover_menu)

        # Ocultar el boton de minZise
        self.botonMinSize.hide()

        # Botones de la ventana(navegacion)
        self.botonMinSize.clicked.connect(self.control_boton_minSize)
        self.botonMaximizar.clicked.connect(self.control_boton_maxSize)
        self.botonCerrar.clicked.connect(lambda: self.close())

        #ancho de columna adaptable
        self.tablaMesa.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tablaProducto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #elimina barra de titulo -opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #mover la ventana
        self.frameEstado.mouseMoveEvent = self.mover_ventana
        
        # Botones de mesas
        self.botonMesa1.clicked.connect(lambda: self.btnMesaAction('1'))
        self.botonMesa2.clicked.connect(lambda: self.btnMesaAction('2'))
        self.botonMesa3.clicked.connect(lambda: self.btnMesaAction('3'))
        self.botonMesa4.clicked.connect(lambda: self.btnMesaAction('4'))
        self.botonMesa5.clicked.connect(lambda: self.btnMesaAction('5'))
        self.botonMesa6.clicked.connect(lambda: self.btnMesaAction('6'))
        self.botonMesa7.clicked.connect(lambda: self.btnMesaAction('7'))
        self.botonMesa8.clicked.connect(lambda: self.btnMesaAction('8'))
        self.botonMesa9.clicked.connect(lambda: self.btnMesaAction('9'))
        self.botonMesa10.clicked.connect(lambda: self.btnMesaAction('10'))
        self.botonMesa11.clicked.connect(lambda: self.btnMesaAction('11'))
        self.botonMesa12.clicked.connect(lambda: self.btnMesaAction('12'))
        self.botonMesa13.clicked.connect(lambda: self.btnMesaAction('13'))
        self.botonMesa14.clicked.connect(lambda: self.btnMesaAction('14'))

        # Botones del menu 
        self.botonEEC.clicked.connect(lambda: self.botonesMenu("Entrando En Confianza"))
        self.botonHDN.clicked.connect(lambda: self.botonesMenu('Hablemos De Negocio'))
        self.botonAS.clicked.connect(lambda: self.botonesMenu('Algo Sencillo'))
        self.botonDA.clicked.connect(lambda: self.botonesMenu('De Acomodo'))
        self.botonCocteles.clicked.connect(lambda: self.botonesMenu('Cocteles'))
        self.botonLiquidos.clicked.connect(lambda: self.botonesMenu('Liquidos'))
        self.botonCafe.clicked.connect(lambda: self.botonesMenu('Cafe'))
        self.botonANC.clicked.connect(lambda: self.botonesMenu('Aun No Convencido'))
        # MenuTable Events
        self.tablaProducto.itemDoubleClicked.connect(self.doubleClick)


     #Size Grip ---Redimensionar
    def resizeEvent(self, event):
       rect = self.rect()
       self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)


    def control_boton_minSize(self):
        self.showNormal()
        self.botonMinSize.hide()
        self.botonMaximizar.show()

    def control_boton_maxSize(self):
        self.showMaximized()
        self.botonMaximizar.hide()
        self.botonMinSize.show()

    #mover ventana
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons()== QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_position)
                self.click_position = event.globalPos()
                event.accept()
        
        if event.globalPos().y() <=10:
            self.showMaximized()
            self.botonMaximizar.hide()
            self.botonMinSize.show()
        else:
            self.showNormal()
            self.botonMinSize.hide()
            self.botonMaximizar.show()

    #Mover el menu de opciones
    def mover_menu(self):
        if True:
            width = self.frameMenu.width()
            normal = 0
            if width == 0:
                extender = 185
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frameMenu, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    # Botones de las mesas
    def btnMesaAction(self, mesa):
        self.labelMesa.setText("Mesa "+ mesa)
        
        # Coneccion a tabla de mesa
        for i in range(1, 15):
            if mesa == str(i):
                datosTable = self.db.mostrar_mesa(str(i))
                i = len(datosTable)
                self.tablaMesa.setRowCount(i)
                tablerow = 0

                for row in datosTable:
                    self.tablaMesa.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tablaMesa.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tablaMesa.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    tablerow +=1
    #  mostrar el menu 
    def mostrarMenu(self, datosMenu=""):
        if datosMenu == "":
            datosMenu = self.db.mostrar_menu()
            
        i = len(datosMenu)
        self.tablaProducto.setRowCount(i)
        tablerow = 0

        for row in datosMenu:
            self.tablaProducto.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            tablerow +=1 
    
    # Botones de menu
    def botonesMenu(self, text):
       text = str("'"+text+"'") 
       result = self.db.btnsMenuConsul(text)
       self.mostrarMenu(result)


    #BUSCADOR DE PRODUCTOS
    def buscarMenu(self):
        nombreBuscar = self.entryBuscar.text().upper()
        nombreBuscar = str("'"+nombreBuscar+"%'")
        producto = self.db.buscar_menu(nombreBuscar)
        self.mostrarMenu(producto)




    # Selector de Tablas de Mesa
    def selectorMesa(self):
        select = self.labelMesa.text()
        select=select.replace("Mesa ","")
        # retorna el numero de la mesa
        return select

    # Evento de Doble Click
    def doubleClick(self, index):
        # el valueSlot es el nombre del Producto
        valueSlot=index.text()
        valueSlot=str("'"+valueSlot+"'")
        mesa=self.selectorMesa()

        precio = self.db.selectPrecio(valueSlot)
        pedido = self.db.selectPedido(valueSlot)

        self.btnMesaAction(mesa)        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Caja()
    mi_app.show()
    mi_app.mostrarMenu()
    sys.exit(app.exec_())
