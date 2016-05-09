#!/usr/bin/env python
# -*-coding:utf-8-*-

class Auto:
    name = ""
    kind = ""
    color = ""
    value = 100.00
    _numero_serie = "Hola!"
    
    def description(self):
        desc = "El %s es color %s %s. Vale $%.2f" % (self.name , self.color, self.kind , self.value)
        print desc
        
car1 = Auto()
car1.name = "Ford"
car1.color = "Rojo"
car1.kind = ", Tipo Camioneta"
car1.value = 1234.13234

print car1.description()

