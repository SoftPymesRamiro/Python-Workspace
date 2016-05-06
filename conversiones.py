#!/usr/bin/python
# -*- coding: UTF-8  -*-


print "Cambiar de float a int"

print 4.3 
print int(4.3)

print "Cambiar de float a str"
print 4.3
print str(4.3)

print "Cambiar un list a tuple"
print (4,3,4)
print list((4,3,4))

'''
funciones comunes :
'''

#len: nos ayuda a obtener el tamaño de una cadena
print len("hey")

#type: nos ayuda a saber el tipo de dato
print type(3)

#range(n): nos crea una lista con "n" elementos
print range(5)

#map: map ("funcion que queremos ejecutar", "A estos parametros"), ejemplo, convertir todos los datos enteros de una lista a valores de cadena map(str,[5,2,1])
print map(str,[5,2,1])

#sorterd: permite ordenar una lista
print sorted([5,2,1])

#round: permite redondear según el criterio que tu quieras. 
print round(6.432312,2)

#dir: nos ayuda a saber que podemos hacer con el tipo de dato, parametro, sentencia que estamos usando.
print dir([5,2,1])

#help: nos muestra la documentación de como usar alguna de las funciones comunes o palabras reservadas.
#print help(sorted)

print "Hola " * 5


#duck typing
'''
En los lenguajes de programación orientados a objetos, se conoce como duck typing
el estilo de tipificación dinámica de datos en que el conjunto actual de métodos
y propiedades determina la validez semántica, en vez de que lo hagan la herencia
de una clase en particular o la implementación de una interfaz específica.
'''