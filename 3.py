#Crear un programa que a partir de un diccionario “supermercado” permita
#que el usuario ingrese N productos, compuestos por el nombre del producto
#(clave) y la cantidad del mismo (valor). Para finalizar, deberá ingresar
#un vacío (Enter). Al finalizar, deberá solicitar ingresar un valor numérico
#X y mostrar todos los nombres de productos ingresados con sus respectivas
#cantidades multiplicadas por X.

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