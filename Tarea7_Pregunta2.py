lista = []
x = 0
while True:
    nombre = input("Ingrese un nombre: ")
    if nombre == "":
        break
    else:
        lista.append(nombre)
        x = x + 1


palabra_con_a = []

for palabra in lista:
    print(palabra)
    total = 0
    for a in palabra:
        if a == "a" or a == "A":
            total+=1
    palabra_con_a.append(total)

y = 0
while y < x:
    print("La palabra", lista[y],"con",palabra_con_a[y],"caracter/es con a o A")
    y += 1
