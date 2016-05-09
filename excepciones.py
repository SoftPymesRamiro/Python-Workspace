#!/usr/bin/env python
# -*-coding:utf-8-*-

'''try : 
    6 / 0
except :
    print "ERROR"
'''    

'''    
try : 
    6 / 0
except ZeroDivisionError:
    print "ERROR" 
'''


'''
try : 
    6 / 0
except Exception as e :
    print "%s" % e
'''

'''
try : 
    6 / 0
except Exception as e :
    pass
print "Despues"
'''

'''
try : 
    6 / 0
except Exception as e :
    print "%s" % e
    raise e
'''

#Evitar usar Try Exception y tratar mejor de validar el código 
numero = 0
if numero > 0:
    6/numero
else : 
    print "Solo valores mayores a cero"
    
    