agenda = open("documentos/agenda.csv")

##print(agenda.read())

##print(agenda.readline())#1
##print(agenda.readline())#2
##print(agenda.readline())#3


#for i in range(0,3):
#    print(agenda.readline())

numero = 0
while numero < 4:
    print(agenda.readline())
    numero += 1

print("Ok")
