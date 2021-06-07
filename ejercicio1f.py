from 1ef import *




print("EJERCICIO 1 calcular el IVA")


precio = int(input("Ingresa la cantidad sin IVA: $"))
iva = input("Ingresa el porcentaje del IVA : ")
print("")
if iva == "":
  iva = 21
facturar(precio,iva)
print(f"La factuación con IVA es: ${facturar(precio,iva)}")


