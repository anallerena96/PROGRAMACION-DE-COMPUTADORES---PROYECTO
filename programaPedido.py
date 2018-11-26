import menuPrincipal
from menuPrincipal import *
"""Aquí se importa el menú principal que contiene los productos"""

class elegir(Inicio):  
    """class elegir: Sub clase de "Inicio" que se basa en las categorías, el producto y las cantdades que el usuario desea adquirir."""
    
    def seleccion(self):
        """Se muestran una serie de condiciones relacionadas con la caletegoría de productos que el usuario seleccionó. Por otro lado, si el usuario selecciona la opción 8 (self.b==8),se imprimirá la factura
           que incluye todos los productos que seleccionó anteriormente, la cantidad total de productos y el monto total a pagar.

           ATRIBUTOS:

           self.b: Es la opcion que usuario ha seleccionado. No puede ser una letra. 
           self.sub_prod: Incluye la lista de productos que coresponden a cada categoría.
           self.e : Imprime los encabezados de la factura (cantidad, producto y precio)
           Ventas: Abre el archivo de texto "Ventas.txt"
           Ventas.write: Escribe el número de factura y una lista de todos los pedidos.
           Ventas.close: Cierra el archivo Ventas

           PROCEDIMIENTO:
           Luego de que el usuario digita el producto que desea, se procede a imprimir a guardar la información del producto en un archivo de texto. Posteriormente, los variables self.precio, self.name y la lista self.factura vuelven a tomar el valor de cero."""
        
        if self.b==1:
            print("·····························WRAPS·····························")
            self.sub_prod=Wraps
            
        elif self.b==2:
            print("···························SANDWICHES··························")
            self.sub_prod=Sandwich
            
        elif self.b==3:
            print("····························HUEVOS·····························")
            self.sub_prod=Huev
            
        elif self.b==4:
            print("·······················BEBIDAS CALIENTES·······················")
            self.sub_prod=Bebi_cal
            
        elif self.b==5:
            print("························JUGOS DE FUTAS·························")
            self.sub_prod=frutas
            
        elif self.b==6:
            print("····················GASEOSAS Y JUGOS EMBOT·····················")
            self.sub_prod=Gase_jug
            
        elif self.b==7:
            print("··························ESPECIALES···························")
            self.sub_prod=Espe

            
        elif self.b==8:
            self.k=self.k+1

            print("····························FACTURA···················N° 00"+str(self.k))
            print("     _____________________________________________________")
            print("                       ELIZANA DESAYUNOS                  ")
            print("     _____________________________________________________")
            self.e=print("          Cantidad     "+"     Producto     "+"      Precio     ")
            
            for (x,y,z) in self.factura:
                 print("          "+str(x)+"        "+str(y)+"$ "+str(z))
                 
            print("     _____________________________________________________")
            print("        Total a pagar....................."+"$ " +str(self.total))
            print("        Cantidad de productos comprados........"+str(self.acumcant))
            print("                     GRACIAS POR SU COMPRA")
            print("")
            

            Ventas=open('Ventas.txt','a')

            for (x,y,z) in self.factura:
                Ventas.write("  00"+str(self.k) + "                 " + str(x) + "            " + str(y) + "$ " + str(z)+"\n")

            Ventas.close()

            self.factura=[]
            self.total=0
            self.acumcant=0     
   
        else: 
            None    

    
    def mostrar_sub(self):
        """Muestra la lista de productos de cada categoría siempre y cuando self.b sea diferente a 8."""

        if not self.b==8:
            for (x,y,z) in self.sub_prod:
                print(str(x)+". "+str(y)+ "...." +"$ "+ str(z))
        else:
            return
        
    

    def a_comprar(self):
        """Muestra la opción del producto que el usuario desea adquirir.

        ATRIBUTOS:
           self.c : es el valor de la opción deseada."""
             
        while True:
            try:
                if not self.b==8:
                    print("·······························································")
                    print("Para regresar al menú principal ingresa 0 (cero)")

                    
                    self.c=int(input("Ingresa el número de la opción que deseas: "))
                    
                    break
                
                else:
                    return
                
            except ValueError:
                print("El valor ingresado es invalido. Intentelo nuevamente")
                
        if self.c==0:
            print("")
            

    def cantidad(self):
        """Muestra la cantidad de productos que el usuario desea adquirir."""
        
        while True:

            try:
                if self.b==8:
                    return
                
                elif self.c!=0:
                    self.cant=int(input("¿Cuántas unidades deseas? "))
                    break
                
                else:
                    return
            except ValueError and IndexError:
                print("El valor ingresado es invalido. Intentalo nuevamente")


    def eleccion(self):
        """ Muestra la elección del producto que el usuario eligió y la agrega a la factura (self.factura).

           ATRIBUTOS
           self.name : Refiere al nombre del producto
           self.precio :  Refiere al precio del producto
           self.subtotal : Es el precio que pagará el usuario por comprar ciertas cantidades del producto a un determinado precio
           self.total : Es el valor total de la compra.
           self.acumcant : Es la cantidad total de productos elegidos por el usuario.

           PROCEDIMIENTO
           Se calcula e imprime el monto subtotal y la cantidad de productos que el usuario ha adquirido. Luego, se agregan todos los datos de la compra a la lista factura. """

        for (x,y,z) in self.sub_prod:
            
            while x==self.c and self.b!=8:
               
                self.name=y
                self.precio=z
                self.subtotal=self.precio*self.cant
                self.total=self.subtotal+self.total
                self.acumcant=self.cant+self.acumcant
                print("Subtotal:   $" + str(self.subtotal))
                print("Cantidad:    " + str(self.cant))
                self.factura.append((self.cant,self.name,self.subtotal))
                
                break
            

       




