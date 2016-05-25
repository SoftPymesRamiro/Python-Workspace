agenda = open("Documentos/agenda.csv",'a')
##W es para decir que se va a escribir en el
##A Actualizar

nombre = input("Introduce el nombre del contacto:")
telefono = input("Introduce su teléfono:")

print("Guardado: ",nombre," Tel: ",telefono)
agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write(",")
agenda.write("\n")

agenda.close()
