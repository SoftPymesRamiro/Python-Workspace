#!/usr/bin/env python
# -*-coding:utf-8-*-

class Persona(object): 
    def saludo_general(self):
            return "Hola Personas"

#Clases en Mayuscula y heredan de object (Aunque automaticamente lo hará)
class  Estudiante(Persona):
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def hola(self):
        print 'Mi nombre es %s' % self.nombre
    
e = Estudiante("Ramiro", 23)
print e.saludo_general()
e.hola()

