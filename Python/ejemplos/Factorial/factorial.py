"""
factorial = 5
acum = 1
while factorial>0:
    acum = acum * factorial
    factorial = factorial -1
    print "%i" % acum
print "Resultado : %i" % acum
"""

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x -1)

print factorial(10)
        