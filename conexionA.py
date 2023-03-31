from xml.dom.expatbuilder import parseString
import mysql.connector

class Comunicacion():

    def __init__(self):    
        self.conexion = mysql.connector.connect(user = 'root', password =  '123456789',
                                            host='localHost',
                                            database = 'naodatabase',
                                            port = '3306')
                                            

    def insertar_productos(self, ubicacion, producto, unidad, cantidad, cost_unid, valor_inv):
        cur = self.conexion.cursor()
        sql = ''' INSERT INTO inventario (UBICACION, PRODUCTO, UNIDAD, CANTIDAD, COST_UNID, VALOR_INV)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(ubicacion, producto, unidad, cantidad, cost_unid, valor_inv)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM inventario"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def buscar_productos(self, nombre_articulo):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM inventario WHERE CODIGO or PRODUCTO LIKE"+nombre_articulo+""
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def eliminar_productos(self,nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM inventario WHERE CODIGO or PRODUCTO = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def actualizar_productos(self, ubicacion, producto, unidad, cantidad, cost_unid, valor_inv):
        cursor = self.conexion.cursor()
        sql = '''UPDATE inventario SET (UBICACION, PRODUCTO, UNIDAD, CANTIDAD, COST_UNID, VALOR_INV)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(ubicacion, producto, unidad, cantidad, cost_unid, valor_inv)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a
