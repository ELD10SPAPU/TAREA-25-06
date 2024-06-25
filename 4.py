"""
Crear un programa que permita crear un diccionario de datos “deudores”
con el RUT de 5 personas (Claves) y sus respectivas deudas en pesos 
(Valores). Posteriormente, dentro de un bucle permitir ingresar el abono 
a las deudas de alguna persona identificándolo con su RUT y el monto del 
abono. Si la persona queda con un saldo de deuda 0, se eliminará del 
diccionario. Se finaliza el bucle si es que se ingresa un vacío. Al 
finalizar, se deberá mostrar las personas que quedaron deudoras y sus 
respectivos saldos de deuda.
"""
deudores = {}

for x in range(5):
    rut = input("Ingrese el rut: ")
    deuda = int(input("Ingrese la deuda: "))
    deudores[rut] = deuda

print(deudores)

# ABONOS

while True:
    print("¿Desea realizar un abono a su rut?")
    print("1) Si")
    y = input("Presione Enter para finalizar")
    if y != "":
        rut = input("Ingrese el rut: ")
        abono = int(input("Ingrese el abono: "))
        for x in deudores:
            deudores[x] = deudores[x] - abono
    else:
        break

# ELIMINAR LOS DEUDORES

for x in deudores:
    if deudores [x] == 0:
        deudores[x] = ""
print(deudores)

