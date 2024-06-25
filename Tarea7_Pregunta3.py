supermercado = {}

while True:
    producto = input("Ingrese el nombre del producto(presione Enter para finalizar): ")
    if producto != "":
        valor = int(input("Ingrese el precio del producto: "))
        supermercado[producto] = valor
    else:
        break

cantidad = int(input("Ingrese la cantidad de producto: "))

for x in supermercado:
    supermercado[x] *= cantidad

print(supermercado)
