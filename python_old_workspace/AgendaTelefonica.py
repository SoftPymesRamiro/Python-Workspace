#Agenda Telefónica
#V0.1
import modulos

modulos.bienvenidos()
opcion = input("> ")

if opcion == "1":
    modulos.escribir()
elif opcion == "2":
    registros = input("Dime cuantos registros quieres ver:\n> ")
    modulos.listar(int(registros))
else:
    modulos.mierror()



