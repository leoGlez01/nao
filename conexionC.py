import mysql.connector

class Conexion():

    def __init__(self):    
        self.conexion = mysql.connector.connect(user = 'root', password =  '123456789',
                                            host='localHost',
                                            database = 'naodatabase',
                                            port = '3306')
                                            
         
    def mostrar_menu(self):
        cursor = self.conexion.cursor()
        sql = "SELECT Producto FROM menu"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def mostrar_mesa(self, mesa):
        cursor = self.conexion.cursor()
        for i in range(1,15):
            if mesa == str(i):
                sql= "SELECT Producto, Cantidad, Precio FROM MESA"+mesa
                cursor.execute(sql)
                datos = cursor.fetchall()
                return datos
    
    def selectPedido(self, pedido):
        cursor=self.conexion.cursor()
        sql = 'SELECT Producto FROM Menu WHERE Producto={}'.format(pedido)
        cursor.execute(sql)
        producto=cursor.fetchall()
        cursor.close()
        return producto
    
    def selectPrecio(self, pedido):
        cursor=self.conexion.cursor()
        sql = 'SELECT Precio FROM Menu WHERE Producto={}'.format(pedido)
        cursor.execute(sql)
        precio=cursor.fetchall()
        cursor.close()
        return precio



    def btnsMenuConsul(self, text):
        cur = self.conexion.cursor()
        sql ="SELECT PRODUCTO FROM menu WHERE TIPO ={}".format(text)
        cur.execute(sql)
        productos = cur.fetchall()
        cur.close()
        return productos

    def buscar_menu(self, nombre):
        cur = self.conexion.cursor()
        sql = "SELECT Producto FROM menu WHERE Producto LIKE"+nombre+""
        cur.execute(sql)
        producto = cur.fetchall()
        cur.close()
        return producto


    # PARA AGREAGAR LOS PEDIDOS A LA MESA POR HACER!!!!!!!!
    def insetarEnMesa(self, mesa, producto,precio,cantidad=0):
        cur = self.conexion.cursor()
        sql =""
        cur.close()