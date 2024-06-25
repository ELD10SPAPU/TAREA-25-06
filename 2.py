lista = []
x = 0
while True:
    nombre = input("Ingrese un nombre: ")
    if nombre == "":
        break
    else:
        lista.append(nombre)
        x = x + 1


total_letra = 0
for palabra in lista:
    if palabra == "a" or palabra == "A":
        total_letra += 1

print("El total de letras a o A es:", total_letra)