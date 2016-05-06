'''
factorial = 5
acum = 1
while factorial > 0:
    acum = acum * factorial
    factorial = factorial -1
    print "%i" % acum

print "%i" % acum
'''

#Otra forma de Solucionarlo
'''
5! = 5 * 4
10! = 10 * 9!
9! = 9 * 8!
...
2! = 2 * 1!
1! = 1 * 0 = 0

'''
def factorial(x):
    if x == 0:
        return 1
    else :
        return x * factorial(x-1)

print factorial(5)