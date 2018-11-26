"""IMPORTANDO LA LISTA DE PRODUCTOS"""

import listasProductos
from listasProductos import *



class Inicio:
    """class Inicio: Es la clase principal del programa.

       ATRIBUTOS:
       self.prod: Este atributo incluye la lista de categoría de productos que se comercializan en la tienda.
       self.factura: Refiere a la factura de compra. Inicia como una lista vacía
       self.total: Refiere al total de la compra
       self.subtotal: Sub total de la compra.
       self.acumcant:  Es la cantidad acumulada de productos que el usuario ha seleccionado.
       self.k: Corresponde el número de la factura.
       self.b : Es la opcion que usuario ha seleccionado. No puede ser una letra. 
    """

    def __init__(self):

        self.prod=productos
        self.factura=[]
        self.total=0
        self.subtotal=0
        self.acumcant=0
        self.k=0



    def introduccion(self):
        """Encabezado principal"""

        
        print( "===============================================================")
        print( "              BIENVENIDO A ELIZANA DESAYUNOS                   ")
        print( "===============================================================")
        print( "LISTA DE PRODUCTOS")
        print( "_______________________________________________________________")


            
    def mostrar_productos(self):
        """Codigo que muestra todas las categorías de productos que se ofrecen"""
        
        for (v,w) in self.prod:
            print(str(v)+". "+str(w))

    
    
    def opcion(self):
        """Muestra la categoría que el usuario desea adquirir. Cada categoría tiene asignado un número."""

        while True:
            try:
                print("===============================================================")
                self.b=int(input("Ingresa el numero del producto que deseas: "))
                print("_______________________________________________________________")
                break
            except ValueError:
                print("El valor ingresado es invalido. Intentalo nuevamente")


