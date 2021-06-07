#3from 3efimport *

print(" EJERCICIO 3  calcular la media de cinco numeros")

print("")

lista = [0,0,0,0,0]

lista[0] = int(input("Ingresa el primer número: "))
lista[1] = int(input("Ingresa el segundo número: "))
lista[2] = int(input("Ingresa el tercer número: "))
lista[3] = int(input("Ingresa el cuarto número: "))
lista[4] = int(input("Ingresa el quinto número: "))
print("")
print(f"La media de los números {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]} y {lista[4]}, es {calculo_media(lista)}")
