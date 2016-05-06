nombre = "Youtube"

if nombre == "Arturo":   #Si el nombre es igual a "Arturo"
    nombre = "Arturo Rifa" #Guarda "Arturo Rifa" en nombre
elif nombre == "Youtube": #Si no se cumplio lo anterior pero el nombre es igual a "Youtube"
    nombre = "Hola Youtube" #Guarda "Hola Youtube" 
else:
    nombre = "Quien eres?" #Si nada de lo anterior se cumplio,guarda en nombre Quien eres?
    
#print nombre

'''
contador = 0
while contador < 5:
    print "numero %i" % contador
    contador += 1
'''
rango = range(10)

print rango    

for i in rango:
    print "Numero %i" %i 
    
    
for i in "Hola Mundo":
    print "%s" % i