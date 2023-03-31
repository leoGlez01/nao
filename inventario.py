import sys
import logo
from turtle import width 
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexionA import Comunicacion

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('GUI NAO.ui', self)

        self.boton_menu.clicked.connect(self.mover_menu)
        self.naodatabase = Comunicacion()

        #oculta el boton minSize
        self.boton_minSize.hide()
        
        #funciones de los botones de las paginas
        self.boton_refrescarInv.clicked.connect(self.mostrar_productos)
        self.boton_registrarInv.clicked.connect(self.insertar_productos)
        self.boton_borrar.clicked.connect(self.eliminar_productos)
        self.boton_act.clicked.connect(self.modificar_productos)
        self.boton_actBuscar.clicked.connect(self.buscar_nombre_actualizar)
        self.boton_buscarEliminar.clicked.connect(self.buscar_nombre_eliminar)

        #funciones de los botones de la ventana
        #self.boton_minimizar.clicked.connect(self.control_boton_minimizar)
        self.boton_minSize.clicked.connect(self.control_boton_minSize)
        self.boton_maxSize.clicked.connect(self.control_boton_maxSize)
        self.boton_cerrar.clicked.connect(lambda: self.close())

        #elimina barra de titulo -opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #mover la ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        #funciones botones del menu lateral
        self.boton_inventario.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_inventario))
        self.boton_mediosBasicos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_mediosBasicos))
        self.boton_utiles.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_utilidades))
        self.boton_registroEntrada.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_registrar))
        self.boton_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_actualizar))
        self.boton_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_eliminar))

        #ancho de columna adaptable
        self.tabla_eliminar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_inventario.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    
    # def control_boton_minimizar(self):
    #     self.showMaximized()

    def control_boton_minSize(self):
        self.showNormal()
        self.boton_minSize.hide()
        self.boton_maxSize.show()

    def control_boton_maxSize(self):
        self.showMaximized()
        self.boton_maxSize.hide()
        self.boton_minSize.show()

    #Size Grip ---Redimensionar
#    def resizeEvent(self, event):
#        rect = self.rect()
#        self.grip.move(rect.right() - self.gripSize, rect.bottom - self.gripSize)

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
            self.boton_maxSize.hide()
            self.boton_minSize.show()
        else:
            self.showNormal()
            self.boton_minSize.hide()
            self.boton_maxSize.show()

    #mover el menu lateral izquierdo
    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    #configurar pagina inventario
    def mostrar_productos(self):
        datos = self.naodatabase.mostrar_productos()
        i = len(datos)
        self.tabla_inventario.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.codigo = row[0]
            self.tabla_inventario.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1])) 
            self.tabla_inventario.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2])) 
            self.tabla_inventario.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3])) 
            self.tabla_inventario.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4])) 
            self.tabla_inventario.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5])) 
            self.tabla_inventario.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6])) 
            
            tablerow +=1
            
            self.signal_actualizar.setText("")
            self.signal_registro.setText("")
            self.signal_eliminar.setText("")

    def insertar_productos(self):
        ubicacion = self.entry_ubicacion.text().upper()
        producto = self.entry_producto.text().upper()
        unidad = self.entry_unidad.text().upper()
        cantidad = self.entry_cantidad.text().upper()
        cost_unid = self.entry_costUnid.text().upper()
        valor_inv = self.entry_valorInv.text().upper()

        if ubicacion != '' and producto != '' and unidad != '' and cantidad != '' and cost_unid != '' and valor_inv != '' :
            self.naodatabase.insertar_productos(ubicacion, producto, unidad, cantidad, cost_unid, valor_inv)
            self.signal_registro.setText('Producto Registrado')
            self.entry_ubicacion.clear()            
            self.entry_producto.clear()
            self.entry_unidad.clear()
            self.entry_cantidad.clear()
            self.entry_costUnid.clear()
            self.entry_valorInv.clear()
            
        else:
            self.signal_registro.setText('Hay espacios vacios')

    def buscar_nombre_actualizar(self):
        id_producto = self.entry_buscarProducto.text().upper()
        id_producto = str("'"+id_producto+"'")
        self.producto = self.naodatabase.buscar_productos(id_producto)
        if len(self.producto) != 0:
            self.codigo = self.producto[0][0]
            self.entry_actUbicacion.setText(self.producto[0][1])
            self.entry_actProducto.setText(self.producto[0][2])
            self.entry_actUnidad.setText(self.producto[0][3])
            self.entry_actCantidad.setText(self.producto[0][4])
            self.entry_actCostUnid.setText(self.producto[0][5])
            self.entry_actValorInv.setText(self.producto[0][6])
        else:
            self.signal_actualizar.setText('El producto no existe')

    def modificar_productos(self):
        if self.producto != '':
            ubicacion = self.entry_actUbicacion.text().upper()
            producto = self.entry_actProducto.text().upper()
            unidad = self.entry_actUnidad.text().upper()
            cantidad = self.entry_actCantidad.text().upper()
            cost_unid = self.entry_actCostUnid.text().upper()
            valor_inv = self.entry_actValorInv.text().upper()

            act = self.naodatabase.actualizar_productos(self.codigo, ubicacion, producto, unidad, cantidad, cost_unid, valor_inv)

            if act == 1:
                self.signal_actualizar.setText('Actualizado con Exito')
                self.entry_actUbicacion.clear()
                self.entry_actProducto.clear()
                self.entry_actUnidad.clear()
                self.entry_actCantidad.clear()
                self.entry_actCostUnid.clear()
                self.entry_actValorInv.clear()

                self.entry_buscarProducto.setText('')
            elif act ==0:
                self.signal_actualizar.setText('ERROR')
            else:
                self.signal_actualizar.setText('INCORRECTO')

    def buscar_nombre_eliminar(self):
        nombre_producto = self.entry_buscarEliminar.text().upper()
        nombre_producto = str("'"+ nombre_producto +"%'")
        producto = self.naodatabase.buscar_productos(nombre_producto)
        self.tabla_eliminar.setRowCount(len(producto))
        tablerow = 0
        for row in producto:
            self.tabla_eliminar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            tablerow +=1 
            

        if len(producto) == 0:
            self.signal_eliminar.setText(' El producto no existe')
        else:
            self.signal_eliminar.setText(' Producto Seleccionado')

        tablerow = 0
        for row in producto:
            self.producto_a_borrar = row[2]
            self.tabla_eliminar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1])) 
            self.tabla_eliminar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2])) 
            self.tabla_eliminar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3])) 
            self.tabla_eliminar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4])) 
            self.tabla_eliminar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5])) 
            self.tabla_eliminar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6])) 

            tablerow +=1

    def eliminar_productos(self):
        self.row_flag = self.tabla_eliminar.currentRow()
        if self.row_flag == 0:
            self.tabla_eliminar.removeRow(0)
            self.naodatabase.eliminar_productos("'"+ self.producto_a_borrar +"'")
            self.signal_eliminar.setText('Producto Eliminado')            
            self.entry_buscarEliminar.setText('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
    