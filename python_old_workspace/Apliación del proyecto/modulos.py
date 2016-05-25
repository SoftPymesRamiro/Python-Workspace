def bienvenidos():
    print("Bienvenido a la agenda")
    print("Seleccione una opción:\n1 - Añadir\n2 - Listar\n3 - Buscar por nombre")

def escribir():
    agenda = open("documentos/agenda.csv")
    for n in range(1,40):
        linea = agenda.readline()
        #print(linea)
        lineapartida = linea.split(",")
        #print(lineapartida[0])
        if lineapartida[0] != "":
            memoria = lineapartida[0]
    #print (memoria)
    agenda.close()

    agenda = open("documentos/agenda.csv",'a')
    memonum = int(memoria)
    posicion = memonum + 1
    agenda.write(str(posicion))
    agenda.write(",")
    agenda.write(input("Introduce el nombre del Contacto: "))
    agenda.write(",")
    agenda.write(input("Introduce su Telefono : "))
    agenda.write(",")
    agenda.write("\n")
    agenda.close()
    print("Registro guardado correctamente")
    listar(15)

def listar(fin):
    agenda = open("documentos/agenda.csv")
    for u in range(1,fin):
        lectura = agenda.readline()
        print(lectura.replace(",","\t"))        
    print("Ok")
    agenda.close()

def buscador(nombrebuscado):
    print ("buscando"+nombrebuscado)
    agenda = open("documentos/agenda.csv")
    for u in range(1,30):
        lectura = agenda.readline()
        partido = lectura.split(',')
        if nombrebuscado == partido[1]:
            print(partido[2])        
    agenda.close()

def mierror():
    print("Opción no valida")
