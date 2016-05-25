#Agenda Telefónica
#V0.1

print("Bienvenido a la agenda")
print("Seleccione una opción:\n1 - Añadir\n2 - Listar")

opcion = input("> ")

if opcion == "1":
    agenda = open("documentos/agenda.csv",'a')
    agenda.write(input("Introduce el nombre del Contacto: "))
    agenda.write(",")
    agenda.write(input("Introduce su Telefono : "))
    agenda.write(",")
    agenda.write("\n")
    agenda.close()
elif opcion == "2":
    agenda = open("documentos/agenda.csv")
    numero = 0
    while numero < 4:
        print(agenda.readline())
        numero += 1
    print("Ok")
    agenda.close()
else:
    print("Opción no valida")
