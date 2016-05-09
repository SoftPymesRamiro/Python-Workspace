#!/usr/bin/env python
# -*-coding:utf-8-*-

import string 
import random

class Archivos(object):
    def __init__(self , nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    def crear_archivo(self , texto):
        fo = open(self.nombre_archivo , "wb")
        fo.write(texto)
        fo.close()
        print "archivo creado exitosamente"
        
    def leer_archivo(self):
        fo = open(self.nombre_archivo , "r+")
        print fo.read()
        fo.close()
        

#texto = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
#print texto

arc = Archivos("texto_aleatorio.txt")
texto = ""
for i in range(100):
    texto += ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
arc.crear_archivo(texto)
arc.leer_archivo()

'''
arc = Archivos("hola.txt")
arc.crear_archivo("Python es el mejor lenguaje. \n Es genial!!\n")
arc.leer_archivo()
'''