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
        del(deudores[x])
print(deudores)

