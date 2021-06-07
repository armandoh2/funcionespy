#3from 8ef import *

print("EJERCICIO 8 conteo de palabras")

print("")

text = input("Ingresa el texto: ")
print("")
print(f"El resultado del contador de palabras y su frecuencia es: {count_words(text)}")
print(f"La palabra más repetida en el texto ingresado es: {most_repeated(count_words(text))}")
print("")
