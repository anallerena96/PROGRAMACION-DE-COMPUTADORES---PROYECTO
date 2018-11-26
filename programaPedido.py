#IMPORTANDO LOS DATOS DEL MENÚ PRINCIPAL

import menuPrincipal
from menuPrincipal import *

#class elegir: Sub clase de "Inicio" que se basa en las categorías, el producto y las cantdades que el usuario desea adquirir.

class elegir(Inicio):

    #Incluye una serie de condiciones relacionadas con la caletegoría de productos que el usuario seleccionó. Por otro lado, si el usuario selecciona la opción 8 (self.b==8),se imprimirá la factura
    # que incluye todos los productos que seleccionó anteriormente, la cantidad total de productos y el monto total a pagar.
    
    def seleccion(self):

        #self.b: Es la opcion que usuario ha seleccionado. No puede ser una letra. 
        #self.sub_prod: Incluye la lista de productos que coresponden a cada categoría.
        
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
            
            #self.e : Variable auxiliar que imprime los encabezados de la factura (cantidad, producto y precio)
            self.e=print("          Cantidad     "+"     Producto     "+"      Precio     ")
            
            #El "for" ayudará a que se imprima la factura
            for (x,y,z) in self.factura:
                 print("          "+str(x)+"        "+str(y)+"$ "+str(z))
                 
            print("     _____________________________________________________")
            print("        Total a pagar....................."+"$ " +str(self.total))
            print("        Cantidad de productos comprados........"+str(self.acumcant))
            print("                     GRACIAS POR SU COMPRA")
            print("")
            



            #Ventas: Abre el archivo de texto "Ventas.txt"
            Ventas=open('Ventas.txt','a')

            #Ventas.write: Escribe el número de factura y una lista de todos los pedidos.

            for (x,y,z) in self.factura:
                Ventas.write("  00"+str(self.k) + "                 " + str(x) + "            " + str(y) + "$ " + str(z)+"\n")



            #Cierra el archivo Ventas
            Ventas.close()


            #Luego de guardar la información de la factura en el archivo de texto, self.factura vuelve a ser una lista vacía, self.total y self.acumcant vuelven a tomar el valor de 0.
            self.factura=[]
            self.total=0
            self.acumcant=0     
   
        else: 
            None    

    #Muestra la lista de productos de cada categoría siempre y cuando self.b sea diferente a 8.
    def mostrar_sub(self):
        if not self.b==8:
            for (x,y,z) in self.sub_prod:
                print(str(x)+". "+str(y)+ "...." +"$ "+ str(z))
        else:
            return
        
    #Muestra la opción del producto que el usuario desea adquirir.

    def a_comprar(self):

        while True:
            try:
                if not self.b==8:
                    print("·······························································")
                    print("Para regresar al menú principal ingresa 0 (cero)")

                    #self.c : es el valor de la opción deseada.
                    self.c=int(input("Ingresa el número de la opción que deseas: "))
                    
                    break
                
                else:
                    return
                
            except ValueError:
                print("El valor ingresado es invalido. Intentelo nuevamente")
                
        if self.c==0:
            print("")

    #Muestra la cantidad de productors que el usuario desea adquirir.
    def cantidad(self):

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

    #Muestra la elección del producto que el usuario eligió y la agrega a la factura (self.factura).
    def eleccion(self):

        for (x,y,z) in self.sub_prod:
            
            while x==self.c and self.b!=8:
                #self.name : Refiere al nombre del producto
                self.name=y

                #self.precio :  Refiere al precio del producto
                self.precio=z

                #self.subtotal : Es el precio que pagará el usuario por comprar ciertas cantidades del producto a un determinado precio.
                self.subtotal=self.precio*self.cant

                #self.total : Es el valor total de la compra.
                self.total=self.subtotal+self.total

                #self.acumcant : Es la cantidad total de productos elegidos por el usuario.
                self.acumcant=self.cant+self.acumcant
                
                #Imprime el subtotal y cantidad
                print("Subtotal:   $" + str(self.subtotal))
                print("Cantidad:    " + str(self.cant))

                #Agregar cantidas, nombre del producto y subtotal a la lista factura.
                self.factura.append((self.cant,self.name,self.subtotal))
                
                break
            

       

