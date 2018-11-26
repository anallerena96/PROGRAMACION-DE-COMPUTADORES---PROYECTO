
"""IMPORTANDO LA INFORMACION DEL PEDIDO"""
import programaPedido
from programaPedido import *


"""Abre el archivo ventas.txt y agrega el siguiente encabezado"""
Ventas=open("ventas.txt", "w")
Ventas.write("  ···HISTORIAL DE VENTAS ELIZANA DESAYUNOS···\n")
Ventas.write("N° Factura" + "          Cantidad     "+"     Producto     "+"      Precio     \n")


"""Cierra el archivo ventas.txt"""
Ventas.close()


"""Le asigna a la variable p y le asigna la sub clase elegir."""
p=elegir()            

    
"""Ejecucion del programa"""       
while True:
    
    p.introduccion()
    p.__doc__
    p.introduccion.__doc__
    
    p.mostrar_productos()
    p.__doc__
    p.mostrar_productos.__doc__
    
    p.opcion()
    p.__doc__
    p.opcion.__doc__
    
    p.seleccion()
    p.__doc__
    p.seleccion.__doc__
    
    p.mostrar_sub()
    p.__doc__
    p.mostrar_sub.__doc__
    
    p.a_comprar()
    p.__doc__
    p.a_comprar.__doc__
    
    p.cantidad()
    p.__doc__
    p.cantidad.__doc__
    
    
    p.eleccion()
    p.__doc__
    p.eleccion.__doc__  
    

    

