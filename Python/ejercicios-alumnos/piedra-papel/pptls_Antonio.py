#librerias a importar
import time
from time import sleep
import random

#Program code
separacion = '~' * 100
eleccion = ('pd', 'pl', 't', 'l', 's')
#eleccion_pc = ('piedra', 'papel', 'tijeras', 'lagarto', 'spock')
while True:
#    def juego()
    item = input('Elije uno: piedra(pd), papel(pl), tijera(t), lagarto(l), spock(s): ')
    if item not in eleccion:
        print ('Tu eleccion no existe')
        continue

    com = random.choice(eleccion)
    sleep(1)

    print (("La maquina eligio {}.").format(com))

    if item == com:
        sleep(1)
        print (("\nEmpataste con la pc.\n{}").format(separacion))
    elif item == "pd" and com == "t":
        sleep(1)
        print (("\nGanaste.piedra aplasta a tijeras\n{}").format(separacion))
    elif item == "pd" and com == "l":
        sleep(1)
        print (("\nGanaste.piedra aplasta a lagarto\n{}").format(separacion))
    elif item == "pl" and com == "pd":
        sleep(1)
        print (("\nGanaste.papel cubre piedra\n{}").format(separacion))
    elif item == "pl" and com == "s":
        sleep(1)
        print (("\nGanaste.papel desautoriza spock\n{}").format(separacion))
    elif item == "t" and com == "pl":
        sleep(1)
        print (("\nGanaste.tijeras cortan papel\n{}").format(separacion))
    elif item == "t" and com == "l":
        sleep(1)
        print (("\nGanaste.tijeras decapitan lagarto\n{}").format(separacion))
    elif item == "l" and com == "pl":
        sleep(1)
        print (("\nGanaste.lagarto devora papel\n{}").format(separacion))
    elif item == "l" and com == "s":
        sleep(1)
        print (("\nGanaste.lagarto envenena a spock\n{}").format(separacion))
    elif item == "s" and com == "p":
        sleep(1)
        print (("\nGanaste.spock vaporiza piedra\n{}").format(separacion))
    elif item == "s" and com == "t":
        sleep(1)
        print (("\nGanaste.spock rompe tijeras\n{}").format(separacion))        
    else:
        sleep(1)
        print (("\nPerdiste. {} acaba con {}\n{}").format(com,item,separacion))
"""
continue = input("¿Deseas volver a jugar? (y/n)")
    if continue ==y:
        juego
"""