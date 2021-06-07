from 1ef import *




print("EJERCICIO 1 calcular el IVA")


precio = int(input("Ingresa la cantidad de la factura sin IVA: $"))
iva = input("Ingresa el porcentage del IVA para aplicar: ")
print("")
if iva == "":
  iva = 21
facturacion(precio,iva)
print(f"La factuación agregando el {iva}% de IVA es: ${facturacion(precio,iva)}")


