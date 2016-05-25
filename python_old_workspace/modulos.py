def bienvenidos():
    print("Bienvenido a la agenda")
    print("Seleccione una opción:\n1 - Añadir\n2 - Listar")

def escribir():
    agenda = open("documentos/agenda.csv",'a')
    agenda.write(input("Introduce el nombre del Contacto: "))
    agenda.write(",")
    agenda.write(input("Introduce su Telefono : "))
    agenda.write(",")
    agenda.write("\n")
    agenda.close()

def listar(fin):
    agenda = open("documentos/agenda.csv")
    for u in range(1,fin):
        lectura = agenda.readline()
        print(lectura.replace(",","\t"))        
    print("Ok")
    agenda.close()

def mierror():
    print("Opción no valida")
