#Agenda Telefónica
#V0.1
import modulos

def principal():

    modulos.bienvenidos()
    opcion = input("> ")

    if opcion == "1":
        modulos.escribir()
        principal()
    elif opcion == "2":
        registros = input("Dime cuantos registros quieres ver:\n> ")
        modulos.listar(int(registros))
        principal()
    elif opcion == "3":
        registros = input("Dime el nombre de la persona que estas buscando:\n> ")
        modulos.buscador(registros)
        principal()
    else:
        modulos.mierror()
        principal()

principal()
