#3from 4ef import *
print(" EJERCICIO 4")
print("calcular el cuadrado de 5 numeros")


listanc = [0,0,0,0,0]
listarc = [0,0,0,0,0]

listanc[0] = int(input("Ingresa el primer número: "))
listanc[1] = int(input("Ingresa el segundo número: "))
listanc[2] = int(input("Ingresa el tercer número: "))
listanc[3] = int(input("Ingresa el cuarto número: "))
listanc[4] = int(input("Ingresa el quinto número: "))

calculo_cuadrados(listanc,listarc)

print("")
print(f"El cuadrado del primer número ingresado, es {listarc[0]}")
print(f"El cuadrado del segundo número ingresado, es {listarc[1]}")
print(f"El cuadrado del tercer número ingresado, es {listarc[2]}")
print(f"El cuadrado del cuarto número ingresado,  es {listarc[3]}")
print(f"El cuadrado del quinto número ingresado, es {listarc[4]}")
