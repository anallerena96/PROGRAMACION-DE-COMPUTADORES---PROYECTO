
#IMPORTANDO LA INFORMACION DEL PEDIDO
import programaPedido
from programaPedido import *

#Abre el archivo ventas.txt y agrega el siguiente encabezado
Ventas=open("ventas.txt", "w")
Ventas.write("  ···HISTORIAL DE VENTAS ELIZANA DESAYUNOS···\n")
Ventas.write("N° Factura" + "          Cantidad     "+"     Producto     "+"      Precio     \n")

#Cierra el archivo ventas.txt
Ventas.close()

#Le asigna a la variable p y le asigna la sub clase elegir.
p=elegir()            


#Ejecucion del programa       
while True:
    p.introduccion()
    p.mostrar_productos()
    p.opcion()
    p.seleccion()
    p.mostrar_sub()
    p.a_comprar()
    p.cantidad()
    p.eleccion()

