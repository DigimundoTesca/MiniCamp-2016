sucesion=[0,1]
n0=0
n1=1
nx = int(input("Cuantos elementos conforman tu sucesion : "))
for n in range(nx):
    sucesion.append(n0+n1)
    #cambio y suma mediante variable auxiliar
    varaux = n0 + n1
    n0 = n1
    n1 = varaux
print(sucesion)