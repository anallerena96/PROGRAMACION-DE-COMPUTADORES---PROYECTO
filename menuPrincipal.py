#Importando LA LISTA DE PRODUCTOS

import listasProductos
from listasProductos import *

#class Inicio: Es la clase principal del programa.

class Inicio:
   
    def __init__(self):

        #self.prod: Este atributo incluye la lista de categoría de productos que se comercializan en la tienda.
        self.prod=productos

        #self.factura: Refiere a la factura de compra. Inicia como una lista vacía
        self.factura=[]

        #self.total: Refiere al total de la compra
        self.total=0

        #self.subtotal: Sub total de la compra.
        self.subtotal=0

        #self.acumcant:  Es la cantidad acumulada de productos que el usuario ha seleccionado.
        self.acumcant=0

        #self.k: Corresponde el número de la factura.
        self.k=0

    #Encabezado principal

    def introduccion(self):
        print( "===============================================================")
        print( "              BIENVENIDO A ELIZANA DESAYUNOS                   ")
        print( "===============================================================")
        print( "LISTA DE PRODUCTOS")
        print( "_______________________________________________________________")


    #Codigo que muestra todas las categorías de productos que se ofrecen
        
    def mostrar_productos(self):
        for (v,w) in self.prod:
            print(str(v)+". "+str(w))

    #Muestra la categoría que el usuario desea adquirir. Cada categoría tiene asignado un número.
    
    def opcion(self):

        #self.b : Es la opcion que usuario ha seleccionado. No puede ser una letra. 
        while True:
            try:
                print("===============================================================")
                self.b=int(input("Ingresa el numero del producto que deseas: "))
                print("_______________________________________________________________")
                break
            except ValueError:
                print("El valor ingresado es invalido. Intentalo nuevamente")


